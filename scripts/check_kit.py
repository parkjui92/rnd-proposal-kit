#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_kit.py — 킷 문서들의 정합성 점검 (저장소 관리용)

이 킷은 실행 코드가 아니라 서로를 가리키는 문서 묶음이라, 한 곳을 고치면 다른 곳이
조용히 어긋난다. 실제로 났던 사고를 검사로 박아 둔 것이다:
  - 같은 번호가 런타임과 예제에서 다른 단계를 가리킴(파일 번호 체계)
  - 버전·라이선스 표기가 파일마다 다름
  - 단독 설치하면 없는 스킬·파일을 읽으라는 지시
  - 제작자 개인 환경에 묶인 서술, 통합 저장소 시절 문구
  - 내용 없는 제목, 개수 표기와 실제 개수 불일치

사용:  python3 scripts/check_kit.py          (저장소 루트에서)
종료 코드: 0 = 문제 없음, 1 = 문제 있음.  표준 라이브러리만 사용.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── 단일 출처: _workspace 산출물 파일 계약 ─────────────────────────
WORKSPACE_FILES = {
    "01_rfp_analysis.md", "02_design_gate.md", "03_evidence.md", "04_proposal.md",
    "04b_for_hwpx.md", "04c_notes.md", "05_review.md", "06_proposal.hwpx",
}
WORKSPACE_PATTERNS = [r"03_evidence_[a-z]+\.md", r"03_evidence\*\.md"]      # 분할 조사
# 공용 에이전트(hwpx-exporter)가 예시로 드는 자매 킷 파일명
SIBLING_FILES = {"04_report_draft.md", "06_report.hwpx"}

MODELS = {"inherit", "sonnet", "haiku", "opus"}

# ── 공개판에 남으면 안 되는 문구 ──────────────────────────────────
FORBIDDEN = [
    (r"/Users/[A-Za-z]", "개인 경로"),
    (r"~/Desktop|데스크탑|바탕화면", "개인 폴더"),
    (r"사용자 구독\)", "제작자 구독 서비스"),
    (r"로 설정돼 있", "제작자 환경 단정"),
    (r"사용자 지시로 확립", "내부 지시 흔적"),
    (r"parkjui92-tech", "옛 계정명"),
    (r"policy-research-designer|paper-research\b|조사 스킬 3종|모든 킷", "통합 저장소 시절 문구"),
    (r"01b_|02_research|03_proposal_draft|04_review_report|05_proposal\.hwpx|02_design_review|05_draft_review", "구 파일 번호"),
    (r"^(<<<<<<<|>>>>>>>) ", "병합 충돌 표시"),
]
FORBIDDEN_SKIP = {"CHANGELOG.md", "LICENSE", "scripts/check_kit.py"}

problems = []


def bad(path, msg, line=None):
    problems.append("%s%s — %s" % (path, ":%d" % line if line else "", msg))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def text_files():
    out = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("__pycache__", "_workspace")]
        for fn in files:
            if fn.endswith((".md", ".json", ".py", ".yml")):
                out.append(os.path.relpath(os.path.join(base, fn), ROOT))
    return sorted(out)


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for ln in m.group(1).split("\n"):
            k, sep, v = ln.partition(":")
            if sep:
                fm[k.strip()] = v.strip().strip('"')
    return fm


# ── 1. 버전·라이선스 ─────────────────────────────────────────────
def check_versions():
    plugin = json.loads(read(".claude-plugin/plugin.json"))
    market = json.loads(read(".claude-plugin/marketplace.json"))
    v = plugin.get("version")
    seen = {"plugin.json": v, "marketplace.json": market["plugins"][0].get("version")}
    m = re.search(r"^## v(\d+\.\d+\.\d+)", read("CHANGELOG.md"), re.M)
    seen["CHANGELOG.md 최상단"] = m.group(1) if m else None
    for rd in ("README.md", "README.en.md"):
        if os.path.exists(os.path.join(ROOT, rd)):
            m = re.search(r"badge/version-(\d+\.\d+\.\d+)-", read(rd))
            seen[rd + " 배지"] = m.group(1) if m else None
    if len(set(seen.values())) != 1:
        bad(".claude-plugin/plugin.json", "버전 불일치: " + ", ".join("%s=%s" % kv for kv in seen.items()))
    lic = plugin.get("license", "")
    head = read("LICENSE").strip().split("\n")[0]
    if lic.split("-")[0].lower() not in head.lower():
        bad("LICENSE", "plugin.json의 license(%s)와 LICENSE 첫 줄(%s)이 다름" % (lic, head))
    for rd in ("README.md", "README.en.md"):
        if os.path.exists(os.path.join(ROOT, rd)) and lic and ("License-%s" % lic.split("-")[0]) not in read(rd).replace("License:_", "License-"):
            if lic not in read(rd):
                bad(rd, "라이선스 표기에 %s가 없음" % lic)


# ── 2. 에이전트·스킬 ─────────────────────────────────────────────
def check_agents_skills():
    agents, skills = {}, {}
    for fn in sorted(os.listdir(os.path.join(ROOT, "agents"))):
        if fn.endswith(".md"):
            rel = "agents/" + fn
            fm = frontmatter(read(rel))
            agents[fn[:-3]] = fm
            if fm.get("name") != fn[:-3]:
                bad(rel, "frontmatter name(%s)이 파일명과 다름" % fm.get("name"))
            if fm.get("model") not in MODELS:
                bad(rel, "model 값이 %s 중 하나가 아님: %s" % (sorted(MODELS), fm.get("model")))
            if not fm.get("description"):
                bad(rel, "description 없음")
    for d in sorted(os.listdir(os.path.join(ROOT, "skills"))):
        rel = "skills/%s/SKILL.md" % d
        if not os.path.exists(os.path.join(ROOT, rel)):
            bad("skills/" + d, "SKILL.md 없음")
            continue
        fm = frontmatter(read(rel))
        skills[d] = fm
        if fm.get("name") != d:
            bad(rel, "frontmatter name(%s)이 폴더명과 다름" % fm.get("name"))

    orch = read("skills/rnd-proposal-orchestrator/SKILL.md")
    # 오케스트레이터의 팀 구성표에 나온 에이전트·스킬이 실재하는가
    for a, s in re.findall(r"^\| ([a-z-]+) \| [a-z-]+ \| [^|]+ \| ([a-z-]+) \|", orch, re.M):
        if a not in agents:
            bad("skills/rnd-proposal-orchestrator/SKILL.md", "구성표의 에이전트 %s가 agents/에 없음" % a)
        if s not in skills:
            bad("skills/rnd-proposal-orchestrator/SKILL.md", "구성표의 스킬 %s가 skills/에 없음" % s)
    # 티어 표의 기본 모델이 에이전트 정의와 같은가
    for names, model in re.findall(r"^\| [^|]+ \| ([a-z /-]+) \| `([a-z]+)`", orch, re.M):
        for a in (x.strip() for x in names.split("/")):
            if a in agents and agents[a].get("model") != model:
                bad("agents/%s.md" % a, "model=%s인데 오케스트레이터 티어 표는 %s" % (agents[a].get("model"), model))
    # 검수관은 편집 도구가 막혀 있어야 한다
    if "Edit" not in agents.get("proposal-reviewer", {}).get("disallowedTools", ""):
        bad("agents/proposal-reviewer.md", "disallowedTools에 Edit가 없음(READ-ONLY 보장 깨짐)")

    # 문서가 "`이름` 스킬"로 부르는 것은 킷 안에 있거나 외부 의존성 표에 선언돼 있어야 한다
    declared = set(re.findall(r"^\| (?:\[)?([a-z][a-z0-9-]+)(?:\]\([^)]*\))? \| (?:스킬|MCP 서버)", read("docs/runtime-notes.md"), re.M))
    for rel in text_files():
        if not rel.endswith(".md") or rel in ("CHANGELOG.md",) or rel.startswith(("examples/", "tests/")):
            continue
        for i, ln in enumerate(read(rel).split("\n"), 1):
            for name in re.findall(r"`([a-z][a-z0-9]*(?:-[a-z0-9]+)+)`\s*스킬|스킬\s*`([a-z][a-z0-9]*(?:-[a-z0-9]+)+)`", ln):
                name = name[0] or name[1]
                if name not in skills and name not in declared:
                    bad(rel, "스킬 `%s`는 킷에도 외부 의존성 표(docs/runtime-notes.md)에도 없음" % name, i)
    return agents, skills


# ── 3. 파일 번호 체계 ────────────────────────────────────────────
def check_workspace_names():
    token = re.compile(r"(?<![\w/.-])(\d\d[a-z]?_[A-Za-z][A-Za-z_*]*\.(?:md|hwpx))")
    for rel in text_files():
        if not rel.endswith(".md") or rel in ("CHANGELOG.md",) or rel.startswith("tests/"):
            continue
        for i, ln in enumerate(read(rel).split("\n"), 1):
            for name in token.findall(ln):
                if name in WORKSPACE_FILES or name in SIBLING_FILES:
                    continue
                if any(re.fullmatch(p, name) for p in WORKSPACE_PATTERNS):
                    continue
                bad(rel, "파일 계약에 없는 산출물 이름: %s" % name, i)
    demo = os.path.join(ROOT, "examples", "rnd-proposal-demo")
    for fn in sorted(os.listdir(demo)):
        if not fn.startswith(".") and fn not in WORKSPACE_FILES:
            bad("examples/rnd-proposal-demo/" + fn, "파일 계약에 없는 예제 파일")


# ── 4. 금지 문구 ─────────────────────────────────────────────────
def check_forbidden():
    for rel in text_files():
        if rel in FORBIDDEN_SKIP or rel.startswith("tests/"):
            continue
        for i, ln in enumerate(read(rel).split("\n"), 1):
            for pat, why in FORBIDDEN:
                if re.search(pat, ln):
                    bad(rel, "%s: %s" % (why, ln.strip()[:70]), i)


# ── 5. 문서 구조 ─────────────────────────────────────────────────
def check_structure():
    for rel in text_files():
        if not rel.endswith(".md") or rel.startswith(("examples/", "tests/")):
            continue
        lines = read(rel).split("\n")
        in_code = False
        prev = None                                       # (줄번호, 수준) — 직전 제목 뒤에 내용이 없었으면 유지
        for i, ln in enumerate(lines, 1):
            if ln.strip().startswith("```"):
                in_code = not in_code
                prev = None
                continue
            if in_code:
                continue
            m = re.match(r"(#{1,6})\s+\S", ln)
            if m:
                level = len(m.group(1))
                if prev and level <= prev[1]:
                    bad(rel, "내용 없는 제목", prev[0])
                prev = (i, level)
            elif ln.strip():
                prev = None
            # 상대 링크가 실제 파일을 가리키는가
            for target in re.findall(r"\]\((?!https?://|#|mailto:)([^)#\s]+)", ln):
                path = os.path.normpath(os.path.join(ROOT, os.path.dirname(rel), target))
                if not os.path.exists(path):
                    bad(rel, "깨진 링크: %s" % target, i)

    # "N대 검수 영역" 제목의 N과 실제 하위 절 수, 에이전트가 말하는 N
    rev = read("skills/rnd-proposal-review/SKILL.md")
    m = re.search(r"^## (\d+)대 검수 영역\n(.*?)(?=^## )", rev, re.M | re.S)
    if not m:
        bad("skills/rnd-proposal-review/SKILL.md", "'N대 검수 영역' 절을 찾지 못함")
    else:
        n, actual = int(m.group(1)), len(re.findall(r"^### \d+\. ", m.group(2), re.M))
        if n != actual:
            bad("skills/rnd-proposal-review/SKILL.md", "제목은 %d대인데 하위 절은 %d개" % (n, actual))
        agent = read("agents/proposal-reviewer.md")
        for k in re.findall(r"초안검수 (\d+)영역", agent):
            if int(k) != n:
                bad("agents/proposal-reviewer.md", "초안검수 %s영역이라 적었으나 스킬은 %d영역" % (k, n))
        for word, num in (("다섯", 5), ("여섯", 6), ("일곱", 7)):
            if re.search(word + r" 영역으로 점검", agent) and num != n:
                bad("agents/proposal-reviewer.md", "'%s 영역'이라 적었으나 스킬은 %d영역" % (word, n))


def main():
    check_versions()
    check_agents_skills()
    check_workspace_names()
    check_forbidden()
    check_structure()
    if problems:
        print("문제 %d건" % len(problems))
        for p in problems:
            print("  ✗ " + p)
        return 1
    print("문제 없음 — 버전·라이선스, 에이전트·스킬 참조, 파일 번호 체계, 금지 문구, 문서 구조")
    return 0


if __name__ == "__main__":
    sys.exit(main())
