# 왜 만들었나 · 상세 사용법

**한국어** · [English](#english)

README에서 덜어낸 배경과 사용 시나리오를 여기 둔다.

---

## 왜 만들었나

정부 R&D 공고에 대응해 본 사람은 안다. 제안서는 **잘 쓴 글이 아니라 배점을 득점하는 글**이다.

평가위원은 정해진 평가표를 들고 앉는다. 항목이 있고, 항목마다 배점이 있고, 그 배점 안에서만 점수가 나온다. 그래서 문장이 아무리 좋아도 30점짜리 항목이 한 페이지 반으로 끝나 있으면 그 30점은 회수되지 않는다. 20점짜리 항목을 공들여 스무 쪽 쓰면, 잘 쓴 만큼 손해다.

이걸 알면서도 매번 같은 자리에서 미끄러진다.

**배점은 공고문에 있고, 제안서는 다른 파일에 쓴다.** 배점표를 읽을 때는 분명히 알고 있었다. 그런데 문서를 열고 몇 시간 쓰다 보면 지면은 자기가 잘 아는 쪽으로 쏠린다. 다 쓰고 나서 배점표를 다시 열면 결론이 늘 같다 — 제일 배점 높은 항목이 제일 얇다.

**실격 요건은 굵은 글씨로 오지 않는다.** 사람을 떨어뜨리는 문장은 본문이 아니라 ※ 뒤에, 괄호 안에, "~되어야 하며" 같은 조건절에 숨어 있다. "직접 근거가 되어야", "착수 전제 조건으로 설계"— 이런 단서 하나를 흘리면 나머지가 아무리 훌륭해도 요구 미충족으로 깎인다. 그런데 이건 정독의 문제가 아니다. **추출과 대조**의 문제다. 사람은 30쪽짜리 공고문을 두 번째 읽을 때, 첫 번째 읽은 기억으로 읽는다.

**마감은 짧고 목차는 되돌릴 수 없다.** 공고가 뜨고 제출까지 몇 주다. 목차를 잘못 잡은 채로 조사하고 집필까지 끝내면, 그걸 발견하는 시점에는 이미 고칠 시간이 없다. 목차 한 줄이 며칠치 조사와 집필을 좌우한다.

여기에 LLM을 붙이면 문장 문제는 확실히 줄어든다. 그런데 위의 셋은 하나도 해결되지 않는다. 오히려 나빠지는 구석이 있다 — 매끄러운 초안이 빨리 나오니까, **목차를 의심할 계기가 사라진다.**

한 가지가 더 있었다. 제안서는 **아직 하지 않은 일의 계획서**인데, 초안은 자꾸 완성된 설계 결과처럼 써진다. 주제별로 완성된 내용을 나열해 놓으면 "이미 다 한 것"처럼 읽혀서, 정작 배점이 걸린 *수행 방법*을 못 보여준다. 이건 문장력이 아니라 골격의 문제라 다 쓴 뒤에는 손보기 어렵다.

그래서 필요했던 것은 더 좋은 문장이 아니라 **순서와 장치**였다.

1. 공고문에서 배점과 ※단서를 **구조화해서 뽑아내는** 단계
2. 그 배점을 목차와 **1:1로 묶어두는 표** — 평가대응표
3. 조사·집필에 착수하기 **전에** 그 매핑에 구멍이 없는지 판정하는 게이트
4. 다 쓴 뒤 공고문과 초안을 **나란히 놓고** 대조하는 게이트

이 킷은 실제로 정부 R&D 제안서를 쓰면서 그 장치들을 하나씩 붙여 만든 개인 하네스를 정리한 것이다. 집필 규칙([references](../skills/rnd-proposal-writing/references/))도 이론에서 온 게 아니라 실제 공동 제안서 모듈을 쓰고 고치는 과정에서 뽑아낸 것으로, 문체·부호·방어 태그·표 규격 등 약 60개 패턴이 문서로 남아 있다.

마지막으로 한국 공고 대응에는 해외 도구가 건드리지 않는 조건이 둘 더 있다. **제출 형식이 한글(`.hwpx`)**이고 발주처가 지정 양식을 주면 그 서식 항목이 곧 목차가 된다는 것, 그리고 여럿이 나눠 쓰는 **공동 제안서**에서는 "내 모듈이 남의 모듈과 어울려 한 문서로 읽히는가"가 별도의 품질 기준이 된다는 것. 이 킷은 그 둘도 다룬다.

---

## 중심 장치 — 평가대응표 (전문)

이 킷이 다른 문서 작성 도구와 갈리는 지점은 문장이 아니라 이 표 하나다. 공고문을 읽고 나서 **집필에 들어가기 전에** 다음 표를 먼저 만든다.

| 평가항목 | 배점 | 대응 제안서 섹션 | 대응 핵심 논거 | 조사 필요 근거 |
|---|---|---|---|---|
| 필요성 | 20 | §1 필요성 | 도입률 저조·도입 애로 → 지원 당위 | 도입률·애로요인 통계 |
| 기술개발성 | **30** | §3 개발내용·차별성 | 도메인특화 + 온프레미스 보안 | 유사 플랫폼 기능·한계 비교 |
| 사업화가능성 | **30** | §4 사업화 전략 | 구독 BM + 보급기관 연계 확산 | 시장규모·수요, 확산경로 |
| 추진체계 | 20 | §5.1 로드맵 + §5.2 수행역량 | 단계별 마일스톤 + 기관 역량 | [보강 필요] 수행기관 실적 |

*(동봉 예제 [`examples/rnd-proposal-demo/01_rfp_analysis.md`](../examples/rnd-proposal-demo/01_rfp_analysis.md)에서 발췌)*

표가 하는 일은 단순하다. **빈칸이 보이면 목차가 잘못된 것이다.** 대응 섹션이 없는 평가항목은 그 점수를 통째로 버린다는 뜻이고, "~을 강조" 수준으로만 적힌 칸은 아직 득점 논거가 없다는 뜻이다. 배점과 지면 비중을 나란히 놓으면 "30점 항목이 20점 항목과 지면이 같다"는 사실도 집필 전에 눈에 보인다.

그리고 이 표는 파이프라인 내내 다시 쓰인다. 조사관은 "조사 필요 근거" 열을 작업 지시로 받고, 작성가는 이 표를 옆에 두고 쓰며, 검수관은 게이트 두 곳에서 이 표를 기준으로 판정한다.

**실제로 게이트가 잡아낸 것** — 동봉 데모에서, 게이트1은 필수요구인 개인정보·보안이 추진체계 절에 뭉뚱그려져 독립 소절도 평가대응표 행도 없다는 점을 [필수]로 걸어 §5.3으로 승격시켰고, 고배점 30점 항목의 지면이 20점 항목과 5%p밖에 차이 나지 않는다는 점을 지적해 배분을 다시 잡게 했다. 집필이 끝난 뒤에는 게이트2가 차별성 대비표의 비교 대상이 공고가 말한 "유사 플랫폼"이 아니라 범용 AI 도구·대기업 자체구축이라는 점을 잡아냈다 — 표는 그럴듯하게 채워져 있었지만 요구를 빗나간 표였다. 판정 원문은 [`02_design_gate.md`](../examples/rnd-proposal-demo/02_design_gate.md)·[`05_review.md`](../examples/rnd-proposal-demo/05_review.md)에 그대로 있다.

> **A/B 실측에 대해.** 이 저장소에는 순정 Claude Code와의 대조 감사가 아직 없다. 같은 설계 철학으로 만든 자매 킷에는 있으므로, 게이트 구조가 실제로 무엇을 바꾸는지 수치로 보고 싶다면 [policy-research-kit의 감사 기록](https://github.com/parkjui92/policy-research-kit/blob/main/docs/vanilla-vs-kit.md)을 참고하면 된다. 그쪽 수치를 이 킷의 성능으로 옮겨 읽지는 말 것.

---

## 파이프라인 상세

```
RFP 분석 (rfp-analyst — 필수요구·평가지표·배점·※단서 급소, 과제유형 4분류)
  → 목차 + 평가대응표 설계
  → 🚦 게이트1: 설계검토 (reviewer 모드1 — 승인 / 조건부 / 반려)
  → ★ 목차·평가대응표 사용자 승인  ← 여기서 당신이 개입한다
  → 근거조사 (investigator — 신뢰도 3단 표기, 출처 전건 병기)
  → 집필 (writer — 과제유형별 골격 + 평가지표 정조준)
  → 🚦 게이트2: 초안검수 (reviewer 모드2 — 5축)
  → 한글 변환 (hwpx-exporter — 표 행수 1:1 대조 검증)
```

**게이트가 두 번인 이유.** 게이트1은 *비용*을 막는다 — 목차가 틀린 채로 조사와 집필이 끝나면 마감 안에 되돌릴 방법이 없다. 게이트2는 *과신*을 막는다 — 다 쓴 초안은 그럴듯해 보여서 자기 글을 의심하기 어렵다. 검수관은 **집필자와 다른 에이전트**이고 READ-ONLY라, 자기가 쓴 것을 자기가 통과시키는 구조가 원천적으로 성립하지 않는다. 판정은 파일로 남는다.

무한 차단도 막아 둔다. 같은 항목을 두 번 지적해도 미해결이면 "잔여 리스크"로 기록하고 진행한다. 마감이 있는 문서에서는 완벽보다 제출이 먼저다. 다만 이 면제는 **점수를 잃는 결함(득점형)에만** 적용된다. 필수 요구 미충족이나 원문과 다른 수치처럼 **이대로 제출하면 안 되는 결함(자격형)**은 횟수가 찼다고 넘어가지 않고, 사용자에게 올려 보강·삭제·위험 수용 중 하나를 고르게 한 뒤 그 결정을 파일에 남긴다.

게이트2는 출처도 직접 연다. 조사 파일과 초안을 맞춰 보는 것만으로는 조사 단계에서 잘못 옮긴 수치를 잡지 못한다 — 두 파일이 서로 일치하기 때문이다. 동봉 데모에서도 조사 단계가 "검증 완료"로 적은 출처 두 건이 원문 대조에서 걸렸다. 하나는 URL이 가리키는 기사에 그 수치가 없었고, 하나는 10년 전 전망치였다.

**과제유형 4분류.** 공고를 읽고 유형을 먼저 판정한다 — 유형마다 목차 기준과 집필 골격이 다르기 때문이다.

| 유형 | 골격 |
|---|---|
| 기술개발형 (TRL·성능지표·사업화) | 표준 6섹션 (필요성 / 목표·내용 / 추진전략·체계·일정 / 기대효과·활용 / 수행역량 / 예산) |
| 위탁·정책수립형 (수립지원·위탁연구·용역) | 계획형 3단 (추진방향 → 수행방법론·추진과정 → 결과예시) |
| 지원사업 신청형 (지정 신청서식 있음) | 서식 항목이 곧 목차 — 서식을 파싱해 순서 그대로 |
| 팀 공동 제안서의 담당 모듈 | 계획형 3단 + 팀 서식 정합 |

---

## 상세 사용법

설치 후 Claude Code를 재시작하면 오케스트레이터가 "제안서", "연구개발계획서", "사업계획서" 같은 요청에 자동 반응한다.

### 시나리오 1 — 공고문 하나로 백지에서

```
첨부한 공고문으로 제안서 초안을 만들어줘.
우리 기관 강점이랑 기존 실적 메모도 같이 첨부했어.
```

공고문(.hwpx/.pdf/.docx/URL)을 파싱해 필수요구·배점·※단서·양식 제약을 뽑고, 과제유형을 판정한 뒤 목차와 평가대응표를 만든다. 게이트1이 매핑 구멍을 점검하고, **그다음 멈춰서 당신에게 목차를 보여준다.** 승인하면 조사 → 집필 → 게이트2 → hwpx로 이어진다.

파이프라인은 두 번 멈춘다(목차 승인, 그리고 최종 보고). 그사이는 자리를 비워도 된다. 검수에서 자격형 결함이 끝내 풀리지 않았을 때만 한 번 더 멈춰 어떻게 할지 묻는다.

### 시나리오 2 — 위탁연구·수립지원 과제

```
이건 기술개발이 아니라 수립지원 용역이야. 계획형으로 써줘.
```

이 유형은 배점이 "무엇을 만들 것인가"가 아니라 **"어떻게 수행할 것인가"**에 걸려 있다. 그래서 골격이 바뀐다 — 추진방향(과업 목표 두괄식 + 설계 원칙) → 수행방법론(단계 프로세스 표·N축 분석틀·자문 계획·품질관리 원칙) → 결과예시(산출물 미리보기 + 확정 경로를 밝힌 면책문). 완성 결과를 서술하는 대신 수행 과정을 보여주는 문체로 고정된다.

실제 위탁연구 RFP 1건을 이 경로로 끝까지 돌려 7장·표 11종의 hwpx를 산출한 기록이 있다.

### 시나리오 3 — 팀 공동 제안서에서 내 모듈만

```
팀 제안서인데 내 담당은 2-3 파트야.
팀원들이 쓴 원고 첨부할 테니 이거랑 어울리게 써줘.
```

혼자 쓰는 제안서와 요구가 다르다. 목표가 "잘 쓰는 것"이 아니라 **"남이 쓴 것과 어울려 한 문서로 읽히는 것"**이기 때문이다. 모듈 모드로 들어가면 팀원 원고를 문체 표본으로 먼저 읽고, 마크다운 헤딩 대신 □◯－ 유니코드 글머리 위계로 쓰고, 종결형을 팀 통합본 규격(명사형)으로 맞추고, 금지체(~한다/~합니다/~된다)를 전수 검사한다. 내부 작업 마커·타 모듈 담당자명·볼드는 제출본에서 제거하되 별도 노트로 전수 보존한다. 옆 모듈과의 교차참조("1-N에서 도출한 …를 근거로")도 명시한다.

### 시나리오 4 — 이미 쓴 초안을 배점 기준으로 점검

```
평가대응표 기준으로 4장이 배점 대비 부실한지 점검해줘
```

처음부터 다시 쓰지 않는다. 검수관만 다시 등판해 공고문과 초안을 나란히 놓고 대조한다 — 필수요구 충족 체크표, 배점 높은 순서로 정렬한 평가지표별 점검, 그리고 위치·문제·해결을 갖춘 수정 요청. "근거가 약하다" 같은 지적은 나오지 않는다. "3.2절 목표의 '성능 30% 향상'에 현재값과 출처 없음 → 조사파일의 시장 벤치마크 수치를 현재값으로 인용" 형태로 나온다.

### ★ 목차 승인 게이트에서 개입하는 법

파이프라인이 멈추고 목차와 평가대응표를 보여줄 때가 **가장 값싸게 방향을 바꿀 수 있는 지점**이다. 그냥 말하면 된다.

```
3장을 차별성 중심으로 다시 잡아줘
사업화 배점이 30점인데 지면이 너무 적다
공고문 ※ 단서 중에 "착수 전제조건" 부분이 어느 절에도 안 걸려 있는데
과제명 후보 몇 개 더 줘 — 간결한 쪽으로
```

과제명·추진배경처럼 방향을 결정하는 핵심 문안은 애초에 단일 확정안이 아니라 **강조점을 병기한 복수 후보**로 제시된다(간결한 안이 위). 고르면 된다.

### 지정 양식이 있을 때

발주처 양식(.hwp/.hwpx)을 `_workspace/00_input/`에 넣어 두면 서식을 파싱해 **항목 순서 그대로** 목차를 잡고, 마지막에 폼 채우기 경로로 변환한다. 독점 기관 양식은 저장소에 포함하지 않는다(BYO-template) — 런타임에 당신이 제공한다.

### 근거가 미덥지 않을 때

```
2장 시장 근거가 약해. 통계 원문까지 확인해줘
이 수치 출처 다시 확인해줘
```

조사관은 모든 수치에 출처와 **신뢰도 등급**을 붙인다 — ★1차(정부·국제기구 공식 원문) / ★2차(학술·언론·평가기관) / ▲집계·추정(제3자 집계 — "공식 원표 대조 권장" 각주 의무). 확인한 것과 확인하지 못한 것은 〔검증완료〕/〔미검증〕으로 갈라 두고, 남은 것은 "잔여 검증 계획"으로 명시한다. 못 찾은 근거는 지어내지 않고 "근거 미확보 항목"에 모아, 작성가가 `[보강 필요]`로 이어받는다.

---

## 무엇이 남는가 — 산출 파일

| 파일 | 내용 |
|---|---|
| `01_rfp_analysis.md` | RFP 구조화 — 필수요구·평가배점·※단서 급소·유형 판정·목차·**평가대응표** |
| `02_design_gate.md` | 게이트1 판정 — 무엇을 왜 [필수]로 걸었는지 |
| `03_evidence.md` | 근거장부 — 사실별 출처·신뢰도 등급·미확보 항목 |
| `04_proposal.md` | 본문 초안 |
| `05_review.md` | 게이트2 검수 — 차단 기준·요구사항 충족 체크표·평가지표별 점검·출처 대조표·수정요청·잔여 리스크·사용자 판단 기록 |
| `06_proposal.hwpx` | 최종 제출본 |

*(번호는 동봉 예제 폴더 기준. 실행하면 작업 디렉토리의 `_workspace/`에 같은 순서로 쌓인다.)*

떨어졌을 때 "왜 떨어졌나"를 되짚을 수 있다는 뜻이고, 다음 공고에 같은 근거를 재사용할 수 있다는 뜻이다.

**동봉된 예제** — [examples/rnd-proposal-demo/](../examples/rnd-proposal-demo/)에 설계부터 최종 `.hwpx`까지 전 과정이 들어 있다. 가상 공고를 쓴 **합성 데모**이고 규모도 축약본이다(실제 수탁 과제 산출물은 포함하지 않는다). 대신 근거는 핵심 수치만 실검증해 URL을 병기하고 나머지는 `[보강 필요]`로 남겼다 — 데모에서까지 이 정직성 규율을 지키는 것 자체가 킷의 일부다. 예제 안에는 "도입률 5.3%"와 "활용률 52.7%"가 서로 다른 지표임을 명시하고 혼용을 금지한 대목도 그대로 남아 있다. 전 과정 산출물과 읽는 순서는 [examples/](../examples/)에 정리해 두었다.

---

## 구성

| 에이전트 | 역할 | 스킬 |
|---|---|---|
| `rfp-analyst` | 공고 5대 추출 · 과제유형 4분류 · 목차·평가대응표 설계 | `rnd-rfp-analysis` |
| `proposal-reviewer` | 설계 게이트(모드1) + 초안 검수(모드2) · **READ-ONLY** | `rnd-proposal-review` |
| `research-investigator` | 시장·기술·선행연구·경쟁 근거 수집 | `rnd-research` (+geo-search 내장) |
| `proposal-writer` | 유형별 골격에 맞춘 본문 집필 | `rnd-proposal-writing` (+references 4종) |
| `hwpx-exporter` | `.hwpx` 변환 (지정 양식 폼 채우기 우선) | `rnd-hwpx-export` |

오케스트레이터 `rnd-proposal-orchestrator`가 전체를 조율한다. 부분 재실행("설계 다시", "5장만 다시", "hwpx만 재생성")도 같은 스킬이 받아 해당 단계만 갱신한다.

**집필 references** — 작성가가 필요할 때 읽어 적용하는 규칙집이다.

- [`plan-style-module.md`](../skills/rnd-proposal-writing/references/plan-style-module.md) — 계획형 3단 골격. 과업 목표 두괄식, 방법론 4요소, 결과예시 3원 매핑표와 미리보기 면책문, 논증 패턴 3종
- [`style-devices.md`](../skills/rnd-proposal-writing/references/style-devices.md) — 부호 역할 고정(「」〈〉〔〕), 종결형 3모드, 방어 태그 7종, 표 카탈로그, 〔삽도 프롬프트〕 규격, 수치·출처 규율
- [`team-module-mode.md`](../skills/rnd-proposal-writing/references/team-module-mode.md) — 팀 공동 제안서 모듈 모드. 글머리 유니코드 위계, 금지체 검사, 마커 3단 격리, 통합 노트 의무
- [`proposal-structure.md`](../skills/rnd-proposal-writing/references/proposal-structure.md) — 기술개발형 표준 섹션 상세

> **geo-search 내장.** 해외 사례·기술 동향을 조사할 때 기본 웹검색은 미국 로케일에 고정된다. 내장 래퍼는 대상국 언어·지역으로 검색해(일본 사례는 일본어로) 현지 1차 자료에 닿게 한다. 키가 없으면 기본 검색으로 자동 폴백하므로 필수는 아니다.

---

## 요구사항·폴백·한계 (전문)

- **`.hwpx` 변환**에는 [kordoc](https://github.com/chrisryugj/kordoc) MCP가 필요하다. 없으면 마크다운 산출까지 진행하고 변환만 보류한다.
- **실행 방식**: 메인 세션이 에이전트를 단계 순서대로 불러 쓰고 전달을 중계한다. 따로 켤 기능이 없다. 에이전트 팀 API(실험 기능)로도 돌릴 수 있으나 그쪽은 완주 검증 기록이 없다. Phase 순서와 산출물 계약은 같다.
- 설치·키 설정·모델 선택 상세는 [runtime-notes.md](runtime-notes.md).
- **게이트는 오류를 줄이지 없애지 못한다.** 검수관도 집필자와 같은 계열 모델이라 같은 맹점을 공유할 수 있다. 최종 책임은 사람에게 있다.
- **이 저장소에는 순정 대비 A/B 실측이 없다.** 자매 킷 [policy-research-kit](https://github.com/parkjui92/policy-research-kit/blob/main/docs/vanilla-vs-kit.md)의 감사 기록을 참고하되, 그 수치는 그 킷의 것이다.
- **공고에 배점표가 없으면** 일반 평가 관점을 잠정 적용하고 그 사실을 명기한다. 이때 평가대응표의 정확도는 떨어진다.
- **지정 양식 파싱이 실패하면** 표준 hwpx 생성으로 전환한다 — 이 경우 서식 준수는 수동 확인이 필요하다.
- **팀 `.hwp` 문서에 붙여 넣는 마지막 구간은 수동이다.** hwpx에서 복사해 넣으면 표가 소실될 수 있어, 표 HTML과 교체 가이드를 함께 산출해 그 구간을 메운다.
- 이 킷은 **한국 정부 R&D 공고 관행**(평가표 배점제, hwpx 제출, 지정 양식)에 맞춰져 있다. 다른 맥락에서는 목차 골격과 검수 축을 손봐야 한다.
- [verification-gates.md](verification-gates.md) — 2단계 검증 게이트 설계 방법론(직접 만들 때 참고)

---
---

<a name="english"></a>

# Why I built this · Detailed usage

[한국어](#왜-만들었나--상세-사용법) · **English**

Background and usage scenarios trimmed out of the README.

---

## Context for readers outside Korea

Korean government R&D funding is awarded through a *gonggo* — a public call document that ships with an itemized scoring rubric. A review panel scores your proposal against that published rubric, item by item, with fixed point weights. Submissions are made in **HWP/HWPX** (Hangul Word Processor), the de facto standard document format for Korean government paperwork, and agencies frequently mandate a specific form template. This kit is built for that regime.

---

## Why I built this

Anyone who has responded to a Korean government R&D call knows the thing that matters most: a proposal is not writing that reads well. It is **writing that collects points**.

The reviewer sits down with a fixed rubric. There are items, each item has a point weight, and no score comes from anywhere else. So it does not matter how good the prose is — if the 30-point item runs a page and a half, those 30 points are not coming back. And if you lavish twenty pages on a 20-point item, the quality of that writing is working against you.

Knowing this does not stop you from slipping in the same three places.

**The point weights live in the call document; you write the proposal in a different file.** You definitely knew the weights when you read the rubric. But a few hours into drafting, the page count drifts toward whatever you personally know best. Open the rubric again after finishing and the conclusion is always the same — the highest-weighted item is the thinnest one.

**Disqualifying conditions do not arrive in bold.** The sentence that sinks you is usually not in the body text. It's after a ※, inside a parenthetical, buried in a conditional clause: "must serve as direct grounds for," "shall be designed as a precondition for commencement." Miss one of those and the rest of the proposal, however excellent, gets marked down as non-responsive. And this is not a problem of reading carefully. It is a problem of **extraction and cross-checking**. On the second pass through a thirty-page call document, a human reads it through the memory of the first pass.

**The deadline is short and an outline cannot be undone.** You get a few weeks between the call and submission. If you research and draft against a wrong outline, by the time you notice, there is no time left to fix it. One line of the outline decides days of research and writing.

Adding an LLM reliably fixes the prose problem. It fixes none of the three above. In one respect it makes things worse — a smooth draft arrives so fast that **the occasion to doubt the outline disappears.**

There was one more thing. A proposal is a **plan for work not yet done**, but drafts keep coming out as if they described a finished design. Lay out completed content topic by topic and it reads as "already done," which loses exactly the *methodology* points the rubric was holding. That's a skeleton problem, not a prose problem, and skeletons are hard to fix after the fact.

So what was needed was not better sentences. It was **an order of operations, and some fixtures**:

1. A step that **extracts** point weights and ※ conditions out of the call document, structurally
2. A table binding those weights **one-to-one** to the outline — the evaluation-response map
3. A gate that rules on whether that mapping has holes **before** research and drafting begin
4. A gate that puts the call document and the finished draft **side by side** afterward

This kit is a personal harness — built by bolting those pieces on, one at a time, while actually writing Korean government R&D proposals — cleaned up and published. The writing rules in [references/](../skills/rnd-proposal-writing/references/) likewise didn't come from theory; they were extracted from drafting and revising real joint-proposal modules, and roughly 60 patterns of style, notation, hedging tags, and table conventions are written down there.

Finally, Korean proposal work has two conditions that international tools don't touch. **Submission is in Hangul (`.hwpx`)**, and when the agency supplies a mandated form template, that template's field order *is* your outline. And on a **joint proposal** split across several authors, "does my module read as one document alongside everyone else's" becomes a separate quality bar. This kit handles both.

---

## The central fixture — the evaluation-response map (full)

What separates this kit from a general document-writing tool is not prose. It's this one table, produced after reading the call document and **before any drafting begins**.

| Rubric item | Points | Proposal section | Core scoring argument | Evidence to gather |
|---|---|---|---|---|
| Need | 20 | §1 Need | Low adoption + adoption barriers → case for support | Adoption-rate and barrier statistics |
| Technical development | **30** | §3 Content & differentiation | Domain-specific + on-premise security | Feature/limitation comparison vs. similar platforms |
| Commercialization | **30** | §4 Commercialization strategy | Subscription BM + diffusion via public agencies | Market size, demand, diffusion channels |
| Execution capacity | 20 | §5.1 Roadmap + §5.2 Capability | Staged milestones + institutional capability | [needs sourcing] track record |

*(excerpted from the bundled example, [`examples/rnd-proposal-demo/01_rfp_analysis.md`](../examples/rnd-proposal-demo/01_rfp_analysis.md))*

What the table does is simple. **A blank cell means the outline is wrong.** A rubric item with no corresponding section means you are discarding that item's points outright, and a cell that only says "emphasize X" means there is no scoring argument yet. Putting weights and page shares side by side also makes "a 30-point item gets the same space as a 20-point item" visible *before* anyone writes a word.

The table then gets reused throughout the pipeline. The investigator receives the "evidence to gather" column as a work order, the writer keeps the table open while drafting, and the reviewer rules against it at both gates.

**What the gates actually caught.** In the bundled demo, gate 1 flagged as [required] that a mandatory requirement — personal-data protection and security — had been folded into the execution-capacity section with neither its own subsection nor a row in the response map, and had it promoted to §5.3. It also flagged that the 30-point items had only a 5-percentage-point page advantage over the 20-point items, forcing the allocation to be redone. After drafting, gate 2 caught that the differentiation comparison table was benchmarking against general-purpose AI tools and in-house enterprise builds rather than the "similar platforms" the call actually specified — the table was plausibly filled in, but aimed at the wrong target. The rulings are preserved verbatim in [`02_design_gate.md`](../examples/rnd-proposal-demo/02_design_gate.md) and [`05_review.md`](../examples/rnd-proposal-demo/05_review.md).

> **On A/B measurement.** This repository does not yet contain a head-to-head audit against vanilla Claude Code. A sister kit built on the same design philosophy does, so if you want numbers on what the gate structure actually changes, see [the policy-research-kit audit](https://github.com/parkjui92/policy-research-kit/blob/main/docs/vanilla-vs-kit.md). Those figures belong to that kit — don't read them as this one's performance.

---

## Pipeline in detail

```
Call/RFP analysis (rfp-analyst — requirements, rubric, weights, ※ conditions; 4-way project typing)
  → Outline + evaluation-response map
  → 🚦 Gate 1: design review (reviewer mode 1 — approve / conditional / reject)
  → ★ You approve the outline and the response map  ← your intervention point
  → Evidence gathering (investigator — 3-tier source grading, every fact sourced)
  → Drafting (writer — skeleton per project type, aimed at the rubric)
  → 🚦 Gate 2: draft review (reviewer mode 2 — five axes)
  → Korean conversion (hwpx-exporter — table row counts verified 1:1)
```

**Why two gates.** Gate 1 protects *cost* — once research and drafting finish against a wrong outline, there is no way back inside the deadline. Gate 2 protects against *overconfidence* — a finished draft looks convincing, and doubting your own text is hard. The reviewer is a **different agent from the writer** and is read-only, so a structure where someone signs off on their own work simply cannot form. Rulings persist as files.

Deadlock is also prevented. If an item has been raised twice and is still unresolved, it is recorded as "residual risk" and the pipeline proceeds. For a document with a deadline, submitting beats perfecting. This waiver applies **only to defects that cost points**. Defects that make the proposal unfit to submit — an unmet mandatory requirement, a figure that differs from its source — are not waived by the loop limit; they go to the user, who chooses to supply material, delete or soften the claim, or accept the risk, and that decision is written to the review file.

Gate 2 also opens the sources. Comparing the draft against the evidence file cannot catch a figure that was copied wrongly during research, because the two files agree with each other. In the bundled demo, two sources the research stage had marked "verified" failed the check: one URL pointed to an article that did not contain the figure, the other was a ten-year-old forecast.

**4-way project typing.** The type is determined from the call before anything else, because the outline standard and the drafting skeleton differ by type.

| Type | Skeleton |
|---|---|
| Technology development (TRL, performance targets, commercialization) | Standard 6 sections (need / objectives & content / strategy, structure, schedule / impact & utilization / capability / budget) |
| Commissioned research or policy-formulation service | Plan-form 3 parts (direction → methodology & process → sample outputs) |
| Application-form programs (mandated form supplied) | The form's fields *are* the outline — parse the form, keep its order |
| One module of a joint team proposal | Plan-form 3 parts + conformity to the team's house format |

---

## Detailed usage

Restart Claude Code after installing and the orchestrator picks up requests about proposals, R&D plans, and project applications automatically.

### Scenario 1 — From scratch, with just the call document

```
Draft a proposal from the attached call document.
I've also attached notes on our institution's strengths and prior track record.
```

The call document (.hwpx/.pdf/.docx/URL) is parsed for mandatory requirements, point weights, ※ conditions, and format constraints; the project type is determined; then the outline and evaluation-response map are built. Gate 1 checks the mapping for holes, and **then it stops and shows you the outline.** Approve, and it continues into research → drafting → gate 2 → hwpx.

The pipeline pauses twice (outline approval, then the final report). You can step away in between. It pauses one more time only if a disqualifying defect is still open after review.

### Scenario 2 — A commissioned-research or policy-formulation project

```
This isn't technology development — it's a policy-formulation service contract.
Use the plan-form skeleton.
```

For this type the points hang on **how you will carry the work out**, not on what you will build. So the skeleton changes: direction (objective stated up front + design principles) → methodology (staged process table, an N-axis analytical framework, an expert-consultation plan, quality-control principles) → sample outputs (a preview of deliverables plus a disclaimer naming exactly how the final figures get fixed). The register locks to describing execution rather than asserting finished results.

One real commissioned-research RFP has been run end to end through this path, producing a 7-chapter hwpx with 11 tables.

### Scenario 3 — Only my module of a joint team proposal

```
It's a team proposal and I'm responsible for part 2-3.
I'll attach my teammates' drafts — make mine fit alongside theirs.
```

The requirement here differs from solo authoring. The goal isn't "write well," it's **"read as one document alongside what other people wrote."** In module mode the kit first reads teammates' drafts as a style sample, then writes with □◯－ Unicode bullet hierarchy instead of Markdown headings, matches sentence endings to the team's integrated-document convention (nominal endings), and runs an exhaustive check for banned verb forms. Internal working markers, other authors' names, and bold are stripped from the submission copy but preserved in full in a separate note. Cross-references to adjacent modules ("on the basis of what was derived in 1-N…") are stated explicitly.

### Scenario 4 — Audit an existing draft against the point weights

```
Check chapter 4 against the evaluation-response map — is it thin relative to its weight?
```

Nothing gets rewritten from scratch. Only the reviewer is called back in, placing the call document and the draft side by side: a requirement-satisfaction checklist, a rubric-by-rubric check sorted by point weight, and revision requests that each carry location, problem, and fix. You will not get "the evidence is weak." You get "§3.2's '30% performance improvement' has no baseline value and no source → cite the market benchmark figure from the evidence file as the baseline."

### ★ How to intervene at the outline approval gate

When the pipeline stops and shows you the outline and the response map, that is **the cheapest point at which to change direction**. Just say it:

```
Rebuild chapter 3 around differentiation
Commercialization is worth 30 points and it's getting far too little space
The ※ note about "preconditions for commencement" isn't mapped to any section
Give me more title options — lean toward the shorter ones
```

Direction-setting language like the project title and the background statement is presented as **multiple candidates with their emphases noted** rather than a single fixed version (concise ones listed first). You pick.

### When the agency supplies a mandated form

Drop the agency's form (.hwp/.hwpx) into `_workspace/00_input/` and the kit parses it, builds the outline **in the form's own field order**, and converts at the end via the form-filling path. Proprietary institutional templates are not included in this repository (bring-your-own-template) — you supply yours at runtime.

### When the evidence doesn't convince you

```
Chapter 2's market evidence is thin. Verify it against the original statistics
Re-check the source for this figure
```

The investigator attaches both a source and a **confidence grade** to every figure — ★primary (official government or international-organization documents) / ★secondary (academic, press, evaluation bodies) / ▲aggregated or estimated (third-party aggregators, which carry a mandatory "verify against the official source table" footnote). What was checked and what wasn't are separated as 〔verified〕/〔unverified〕, and whatever remains is written up as a "residual verification plan." Evidence that couldn't be found is not invented; it is collected under "unsourced items," which the writer picks up as `[needs sourcing]`.

---

## What you get — output files

| File | Contents |
|---|---|
| `01_rfp_analysis.md` | Structured call analysis — requirements, point weights, ※ conditions, project type, outline, **evaluation-response map** |
| `02_design_gate.md` | Gate 1 ruling — what was flagged as [required] and why |
| `03_evidence.md` | Evidence ledger — source and confidence grade per fact, plus unsourced items |
| `04_proposal.md` | Body draft |
| `05_review.md` | Gate 2 review — blocking criteria, requirement checklist, rubric-by-rubric check, source check table, revision requests, residual risk, user decision record |
| `06_proposal.hwpx` | Final submission file |

*(Numbering follows the bundled example folder. On a real run these accumulate in the same order under `_workspace/` in your working directory.)*

Which means that if you lose, you can reconstruct why — and that the same evidence is reusable for the next call.

**A worked example is bundled** — [examples/rnd-proposal-demo/](../examples/rnd-proposal-demo/) contains the whole run from design through the final `.hwpx`. It is a **synthetic demo** against a fictional call, at reduced scale (no real client deliverables are included). But the evidence discipline is real: only the key figures were actually verified, with URLs attached, and everything else was left as `[needs sourcing]` — holding that honesty rule even in a demo is itself part of the kit. The example also preserves the point where "5.3% adoption rate" and "52.7% usage rate" are flagged as two different indicators that must not be conflated. The full artifact set and the order to read it in are laid out in [examples/](../examples/).

---

## The team

| Agent | Role | Skill |
|---|---|---|
| `rfp-analyst` | Five-part extraction from the call · 4-way project typing · outline and response map | `rnd-rfp-analysis` |
| `proposal-reviewer` | Design gate (mode 1) + draft review (mode 2) · **READ-ONLY** | `rnd-proposal-review` |
| `research-investigator` | Market, technology, prior work, competitive evidence | `rnd-research` (+ built-in geo-search) |
| `proposal-writer` | Body drafting on the type-appropriate skeleton | `rnd-proposal-writing` (+ 4 references) |
| `hwpx-exporter` | `.hwpx` conversion (mandated-form filling takes priority) | `rnd-hwpx-export` |

The orchestrator `rnd-proposal-orchestrator` coordinates them. Partial re-runs ("redo the design," "just chapter 5 again," "regenerate the hwpx only") go through the same skill and update only the affected stage.

**Writing references** — rule sets the writer reads and applies as needed.

- [`plan-style-module.md`](../skills/rnd-proposal-writing/references/plan-style-module.md) — the plan-form 3-part skeleton: objective stated up front, four required methodology elements, the three-way mapping table for sample outputs with its preview disclaimer, and three argumentation patterns
- [`style-devices.md`](../skills/rnd-proposal-writing/references/style-devices.md) — fixed roles for notation (「」〈〉〔〕), three sentence-ending modes, seven hedging tags, a table catalogue, the 〔figure prompt〕 specification, and rules for figures and sources
- [`team-module-mode.md`](../skills/rnd-proposal-writing/references/team-module-mode.md) — joint-proposal module mode: Unicode bullet hierarchy, banned-form checking, three-stage marker isolation, mandatory integration note
- [`proposal-structure.md`](../skills/rnd-proposal-writing/references/proposal-structure.md) — detail on the standard sections for technology-development projects

> **Built-in geo-search.** Default web search is pinned to a US locale. The bundled wrapper searches in the target country's language and region (Japanese cases in Japanese), which is what it takes to reach local primary material. Without an API key it falls back to standard search, so it is optional.

---

## Requirements, fallbacks, limitations (full)

- **`.hwpx` conversion** requires the [kordoc](https://github.com/chrisryugj/kordoc) MCP server. Without it, the pipeline still runs and stops at Markdown.
- **How it runs**: the main session spawns the agents in phase order and relays between them — nothing experimental needs to be enabled. It can also run on the agent-team API (experimental), but that path has no end-to-end verification record. The phase order and the artifact file contract are identical.
- Setup, keys, and model selection: [runtime-notes.md](runtime-notes.md).
- **Gates reduce errors; they don't eliminate them.** The reviewer runs on a model from the same family as the writer and can share its blind spots. Final responsibility stays with a human.
- **This repository has no measured A/B against vanilla.** See the sister kit's [audit record](https://github.com/parkjui92/policy-research-kit/blob/main/docs/vanilla-vs-kit.md) — but those figures are that kit's, not this one's.
- **If the call publishes no rubric**, a generic evaluation frame is applied provisionally and labeled as such. The response map is correspondingly less reliable.
- **If a mandated form fails to parse**, conversion falls back to standard hwpx generation — format compliance then needs manual checking.
- **The last stretch into a team's `.hwp` file is manual.** Pasting out of hwpx can drop tables, so the kit also emits the tables as HTML plus a replacement guide to cover that gap.
- This kit is shaped by **Korean government R&D conventions** (weighted rubric scoring, hwpx submission, mandated forms). In other contexts you'll want to adjust the outline skeletons and review axes.
- [verification-gates.md](verification-gates.md) — the two-stage gate design methodology, if you want to build your own
