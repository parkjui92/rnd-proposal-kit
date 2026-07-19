# rnd-proposal-kit

정부 R&D 과제 제안서(연구개발계획서) 초안을 쓰는 **5인 에이전트 팀** 플러그인. 공고문(RFP)을 넣으면 요구사항·평가지표·배점을 구조화하고, **평가대응표**로 배점 커버리지를 관리하며, 최종 `.hwpx`까지 산출한다.

## 파이프라인

```
RFP 분석(rfp-analyst: 요구·평가지표·배점·※단서 급소, 과제유형 4분류)
  → 목차·평가대응표 설계 → 설계검토 게이트(reviewer 모드1: RFP↔목차 매핑·고배점 커버리지)
  → ★목차 사용자 승인 → 근거조사(investigator: 시장·기술·선행연구·정책배경)
  → 집필(writer: 평가지표 정조준) → 초안검수(reviewer 모드2) → 한글 변환(hwpx-exporter)
```

- **평가대응표**: "평가위원이 어떤 항목에 몇 점을 주는가"를 목차와 1:1로 매핑해 고배점 항목이 빈약해지는 사고를 구조적으로 막는다 — 한국 공고 대응 특유의 장치.
- **집필 references 내장**: 계획형 3단 골격(추진방향 두괄식·방법론 4요소·결과예시 3원매핑), 부호·종결형·방어 태그 등 문체 장치, 팀 공동 제안서의 담당 모듈 모드까지 실전에서 추출한 약 60개 패턴을 문서화했다.
- **실전 기록**: 실제 위탁연구 RFP 1건 완주(7장·표 11종 hwpx 산출).

## 구성

| 에이전트 | 역할 | 스킬 |
|---|---|---|
| rfp-analyst | RFP 구조화·목차·평가대응표 설계 | rnd-rfp-analysis |
| proposal-reviewer | 설계 게이트(모드1) + 초안 검수(모드2) | rnd-proposal-review |
| research-investigator | 시장·기술·선행연구 근거 수집 | rnd-research (+geo-search 내장) |
| proposal-writer | 필요성→목표→내용→전략→기대효과 집필 | rnd-proposal-writing (+references 3종) |
| hwpx-exporter | `.hwpx` 변환 (지정 양식 폼필 우선) | rnd-hwpx-export |

오케스트레이터 스킬 `rnd-proposal-orchestrator`가 조율한다. "제안서", "연구개발계획서", "사업계획서" 요청에 자동 반응.

## 설치·사용

```
# 이 저장소 단독 설치
/plugin marketplace add parkjui92-tech/rnd-proposal-kit
/plugin install rnd-proposal-kit@rnd-proposal-kit
```

3킷(정책연구·R&D 제안서·논문)을 한 번에 쓰려면 통합 허브를 등록해도 된다:

```
/plugin marketplace add parkjui92-tech/policy-research-kits
/plugin install rnd-proposal-kit@policy-research-kits
```

```
"첨부한 공고문으로 제안서 초안을 만들어줘. 우리 기관 강점 메모 첨부."
"평가대응표 기준으로 4장이 배점 대비 부실한지 점검해줘"
```

## 요구사항·폴백

- 발주처 지정 양식(.hwp/.hwpx)이 있으면 kordoc 폼 채우기 경로를 우선한다. 독점 양식은 저장소에 포함하지 않으며(BYO-template), 사용자가 런타임에 제공한다.
- 팀 API 부재 시 순차 Agent 폴백 — 오케스트레이터의 "공개판 실행 노트" 참조.

## 문서·예제 (이 저장소 동봉)

- [examples/](examples/) — 전 과정 산출물: 설계 → 게이트 판정 → 근거 → 초안 → 검수 → 최종 파일
- [docs/verification-gates.md](docs/verification-gates.md) — 2단계 검증 게이트 설계 방법론
- [docs/runtime-notes.md](docs/runtime-notes.md) — 팀 API 폴백·kordoc 설치·geo-search 키·모델 선택

## 시리즈

통합 허브(3킷 + 검증 스킬 시리즈 안내): **[policy-research-kits](https://github.com/parkjui92-tech/policy-research-kits)** · 단독 검증 스킬: [fact-verify](https://github.com/parkjui92-tech/fact-verify) · [paper-proofread](https://github.com/parkjui92-tech/paper-proofread) · [form-tailor](https://github.com/parkjui92-tech/form-tailor) · [report-to-brief](https://github.com/parkjui92-tech/report-to-brief)

## 라이선스

Apache-2.0. 독점 기관 양식·실제 과제 산출물은 포함하지 않는다(BYO-template 원칙).
