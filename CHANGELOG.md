# Changelog

## v0.10.0 (2026-08-10) — 성능 폴백 장치

무거운 세션 모델(opus/sonnet)로 전 단계가 돌아 제안서 한 편에 오래 걸리는 문제 대응. 4겹 구조:

- ① 단계별 모델 티어 기본값: 조사 `sonnet`·변환 `haiku`, RFP분석·집필·검수는 세션 상속 유지
- ② 쾌속 프로파일("빨리"·마감 임박 시): 조사 분할 병렬, 집필 섹션 배치 분할(배점 높은 섹션 우선·체크포인트), 수정 루프 2→1회, 출처 검증은 고배점 전수+주변 표본(미개봉 출처 명시)
- ③ 지연 폴백 래더: `_workspace/_run_log.md`에 단계별 시각 기록, 안내 예산 초과 시 분할·병렬화 → 다운시프트 → 루프 축소 → 사용자 범위 협상 순 적용
- ④ 실패 시 업시프트: 하위 모델 단계가 자체 검증에 실패하면 한 단계 위 모델로 1회 재스폰. 발주처 지정 양식은 자격 요건이므로 여기서 물러서지 않는다
- 검증 게이트(proposal-reviewer)는 어떤 프로파일·래더 단계에서도 경량화하지 않는다.

자매 킷 [policy-research-kit](https://github.com/parkjui92/policy-research-kit) v1.1.0과 동일 설계이며, 공용 에이전트 `hwpx-exporter`의 모델 티어를 두 저장소에서 일치시켰다.

### 그 밖의 변경

- **라이선스 Apache-2.0 → MIT.** 이 저장소의 내용은 프롬프트·마크다운 자산이라 Apache-2.0의 핵심 이점인 특허 실시권 조항에 실익이 없고, §4(b)의 "변경 사실 고지" 의무가 이 저장소의 의도된 사용(각자 분야·기관에 맞게 고쳐 쓰기)과 오히려 충돌한다. Claude Code 스킬·플러그인 생태계의 사실상 표준도 MIT다. MIT는 Apache-2.0보다 제약이 적으므로 기존 이용자의 권리는 축소되지 않는다.
- README를 국문·영문 2종으로 전면 개편 — 제작 배경과 활용 시나리오 보강 (`README.md` / `README.en.md`)

## v0.9.0 (2026-07-20) — 공개 후보(Release Candidate)

- 통합 저장소(policy-research-kits)에서 **단독 저장소로 분리** — 이 저장소 하나로 마켓플레이스 등록·설치 가능.
- 전 과정 예제(examples/)·검증 게이트 방법론(docs/) 동봉.
- 공개판 조정: `model: inherit` 기본, 팀 API 부재 시 순차 Agent 폴백, BYO-template, geo-search 내장.

다른 킷: https://github.com/parkjui92/policy-research-kit · https://github.com/parkjui92/socsci-paper-kit
