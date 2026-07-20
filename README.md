# rnd-proposal-kit

[![Version](https://img.shields.io/badge/version-0.9.0-blue.svg)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin-purple.svg)

**한국어** · [English](README.en.md)

정부 R&D 과제 제안서(연구개발계획서)를 공고문 분석부터 한글 `.hwpx` 제출본까지 쓰는 **5인 에이전트 팀** [Claude Code](https://claude.com/claude-code) 플러그인.
다른 문서 작성 도구와 갈리는 지점은 문장이 아니라 표 하나다 — **평가대응표**가 "평가위원이 어느 항목에 몇 점을 주는가"를 목차와 1:1로 묶어, 고배점 항목이 얇아지는 사고를 구조로 막는다.

<!-- 데모 GIF 자리 -->

## 중심 장치 — 평가대응표

공고문을 읽고 나서 **집필에 들어가기 전에** 이 표부터 만든다.

| 평가항목 | 배점 | 대응 제안서 섹션 | 대응 핵심 논거 | 조사 필요 근거 |
|---|---|---|---|---|
| 기술개발성 | **30** | §3 개발내용·차별성 | 도메인특화 + 온프레미스 보안 | 유사 플랫폼 기능·한계 비교 |
| 사업화가능성 | **30** | §4 사업화 전략 | 구독 BM + 보급기관 연계 확산 | 시장규모·수요, 확산경로 |
| 추진체계 | 20 | §5.1 로드맵 + §5.2 수행역량 | 단계별 마일스톤 + 기관 역량 | [보강 필요] 수행기관 실적 |

**빈칸이 보이면 목차가 잘못된 것이다.** 대응 섹션이 없는 평가항목은 그 점수를 통째로 버린다는 뜻이고, "~을 강조" 수준으로만 적힌 칸은 아직 득점 논거가 없다는 뜻이다. 배점과 지면 비중을 나란히 놓으면 "30점 항목이 20점 항목과 지면이 같다"는 사실도 집필 전에 눈에 보인다.
표는 파이프라인 내내 다시 쓰인다 — 조사관은 마지막 열을 작업 지시로 받고, 작성가는 이 표를 옆에 두고 쓰며, 검수관은 게이트 두 곳에서 이 표를 기준으로 판정한다.

→ [왜 만들었나·상세 사용법](docs/why.md) · [표 발췌 원본](examples/rnd-proposal-demo/01_rfp_analysis.md)

## 파이프라인

```
RFP 분석 → 목차+평가대응표 → 🚦게이트1(설계검토) → ★목차 승인 → 조사 → 집필 → 🚦게이트2(5축 검수) → hwpx
```

게이트1은 **비용**을 막고(목차가 틀린 채로 조사와 집필이 끝나면 마감 안에 되돌릴 방법이 없다), 게이트2는 **과신**을 막는다.
검수관은 집필자와 **다른 에이전트**이고 READ-ONLY라, 자기가 쓴 것을 자기가 통과시킬 수 없다. 판정은 파일로 남는다.

동봉 데모에서 실제 적발: 필수요구인 개인정보·보안이 독립 소절도 평가대응표 행도 없던 것 → §5.3 승격 · 30점 항목 지면이 20점 항목과 3%p밖에 차이 나지 않던 배분 → 재조정 · 차별성 대비표가 공고가 말한 "유사 플랫폼"이 아니라 범용 AI 도구·대기업 자체구축을 비교하던 것. 판정 원문은 [`02_design_gate.md`](examples/rnd-proposal-demo/02_design_gate.md)·[`05_review.md`](examples/rnd-proposal-demo/05_review.md)에 그대로 있다.

## 설치

```
/plugin marketplace add parkjui92/rnd-proposal-kit
/plugin install rnd-proposal-kit@rnd-proposal-kit
```

## 쓰는 법

```
첨부한 공고문으로 제안서 초안을 만들어줘. 기관 강점 메모도 첨부했어    ← 백지에서
이건 기술개발이 아니라 수립지원 용역이야. 계획형으로 써줘             ← 위탁·수립형
팀 제안서인데 내 담당은 2-3 파트야. 팀원 원고에 맞춰 써줘             ← 팀 모듈 모드
사업화 배점이 30점인데 지면이 너무 적다                              ← 목차 승인 게이트에서
```

공고를 읽고 **과제유형 4분류**(기술개발형 / 위탁·정책수립형 / 지원사업 신청형 / 팀 공동 제안서 모듈)를 먼저 판정한다 — 유형마다 목차 기준과 집필 골격이 다르기 때문이다. 발주처 지정 양식(.hwp/.hwpx)을 `_workspace/00_input/`에 넣어 두면 서식 항목 순서 그대로 목차를 잡는다.
두 번 멈춰 선다(게이트1 후 목차 승인, 게이트2 후 최종 보고). 그사이 자리를 비워도 된다.

## 무엇이 남는가

문서 하나가 아니라 **감사 가능한 기록 한 벌** — RFP 분석·평가대응표·게이트1 판정·근거장부·본문 초안·게이트2 검수·최종 hwpx.
떨어졌을 때 "왜 떨어졌나"를 되짚을 수 있다는 뜻이고, 다음 공고에 같은 근거를 재사용할 수 있다는 뜻이다.

동봉 예제: [전 과정 산출물](examples/rnd-proposal-demo/) — 가상 공고를 쓴 합성 데모이고 규모도 축약본이다. 대신 근거는 핵심 수치만 실검증해 URL을 병기하고 나머지는 `[보강 필요]`로 남겼다.

## 요구사항·한계

- `.hwpx` 변환에 [kordoc](https://github.com/chrisryugj/kordoc) MCP 필요 (없으면 마크다운까지 진행)
- **게이트는 오류를 줄이지 없애지 못한다.** 검수관도 집필자와 같은 계열 모델이라 같은 맹점을 공유할 수 있다
- **이 저장소에는 순정 대비 A/B 실측이 없다.** 자매 킷 [policy-research-kit의 감사 기록](https://github.com/parkjui92/policy-research-kit/blob/main/docs/vanilla-vs-kit.md)을 참고하되, 그 수치는 그 킷의 것이다
- 공고에 배점표가 없으면 일반 평가 관점을 잠정 적용하고 그 사실을 명기한다 — 이때 평가대응표의 정확도는 떨어진다
- 한국 정부 R&D 공고 관행(평가표 배점제, hwpx 제출, 지정 양식)에 맞춰져 있다
- [폴백·의존성·키 설정](docs/runtime-notes.md) · [게이트 설계 방법론](docs/verification-gates.md)

## 시리즈

**에이전트 팀 킷** — [policy-research-kit](https://github.com/parkjui92/policy-research-kit) (정책연구보고서) · [socsci-paper-kit](https://github.com/parkjui92/socsci-paper-kit) (사회과학 논문)

**제작·편집 킷** — [lecture-deck-kit](https://github.com/parkjui92/lecture-deck-kit) (강의자료 HTML 덱 · 브라우저 라이브 편집)

**단독 스킬** — [fact-verify](https://github.com/parkjui92/fact-verify) (출처 검증) · [paper-proofread](https://github.com/parkjui92/paper-proofread) (한국어 학술 교정교열) · [form-tailor](https://github.com/parkjui92/form-tailor) (기관 양식 맞춤) · [report-to-brief](https://github.com/parkjui92/report-to-brief) (보고서 압축)

## 라이선스

[MIT](LICENSE). 독점 기관 양식과 실제 수탁 과제 산출물은 포함하지 않는다(BYO-template 원칙).
