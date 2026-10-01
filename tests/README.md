# tests — 무엇을 어떻게 검사하나

이 킷은 두 층으로 검사한다. 기계가 판정할 수 있는 것은 CI가 매번 돌리고, 모델이 판정해야 하는 것은 결함을 심은 픽스처로 필요할 때 돌린다.

## 1. 결정적 검사 (CI — `.github/workflows/check.yml`)

```
python3 scripts/check_kit.py                                    # 문서 정합성
python3 skills/rnd-hwpx-export/scripts/verify_hwpx.py --selftest # 검증기 자체검사
python3 skills/rnd-hwpx-export/scripts/verify_hwpx.py examples/rnd-proposal-demo/04b_for_hwpx.md examples/rnd-proposal-demo/06_proposal.hwpx
```

`check_kit.py`가 보는 것: 버전·라이선스 표기 일치, 에이전트·스킬 참조의 실재, 모델 티어 표와 에이전트 정의 일치, `_workspace` 파일 번호 체계, 공개판에 남으면 안 되는 문구, 내용 없는 제목, 깨진 링크, 검수 영역 개수 표기.

스킬·에이전트 문서를 고쳤으면 푸시 전에 첫 줄을 돌린다.

## 2. 게이트 적발 검사 (`gate-fixtures/`) — 모델 실행, CI 아님

게이트는 이 킷의 존재 이유인데, 문서를 고칠 때마다 "여전히 잡는가"를 확인할 방법이 없으면 조용히 무뎌진다. 픽스처는 **답을 아는 결함**이 들어 있는 작업 폴더다. 검수관을 돌려 그 결함을 잡는지 본다.

| 픽스처 | 심어진 결함 | 정답지 |
|---|---|---|
| `gate-fixtures/source-defects/` | 출처 2건(다른 기사를 가리키는 URL, 10년 전 전망치) + 필수 요구 부분 충족 1건 + 고배점 항목 공란 1건 | `expected.md` |

돌리는 법:

1. 픽스처의 `workspace/`를 빈 작업 폴더에 `_workspace/`라는 이름으로 복사한다(픽스처 원본에 `05_review.md`가 생기지 않게. 저장소의 `.gitignore`가 `_workspace/`를 무시하므로 픽스처 폴더는 밑줄 없이 둔다).
2. 검수관을 모드 2로 스폰한다. 프롬프트에는 작업 폴더와 "모드 2, 검수 회차 1"만 준다. **무엇이 심어져 있는지 알려주지 않는다.** `examples/`와 `tests/`는 읽지 말라고 적는다(같은 주제의 답이 있다).
3. 나온 `05_review.md`를 `expected.md`의 합격 기준과 대조한다.

스킬·에이전트 문서 가운데 검수에 닿는 것(`rnd-proposal-review`, `proposal-reviewer`, 오케스트레이터의 Phase 5)을 고쳤을 때 돌린다. 실행 기록은 `expected.md` 말미에 한 줄씩 덧붙인다.

픽스처의 출처는 실제 웹 문서다. 페이지가 사라지거나 바뀌면 정답도 바뀐다 — 열리지 않으면 〔미개봉〕이 맞는 판정이고, 그때는 `expected.md`를 고친다.
