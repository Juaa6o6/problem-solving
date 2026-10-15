# Python 정리

코딩테스트용 파이썬 문법·알고리즘 정리 노트.

## 문서

| 문서 | 내용 |
| --- | --- |
| [내장함수와 메서드](내장함수와%20메서드.md) | divmod, enumerate, map, filter, zip, sum, join, int, min/max, input, sorted, eval, ord/chr |
| [정렬 메서드 람다 활용법](정렬%20메서드(sort,%20sorted)%20람다%20활용법.md) | sort/sorted의 key, 람다 |
| [BFS](BFS.md) | 너비 우선 탐색 |
| [DFS](DFS.md) | 깊이 우선 탐색 |
| [구현](구현.md) | 구현 문제 유형 |

---

## 문서 정리 계획

`내장함수와 메서드.md`가 2300줄을 넘어가면서 목차가 길고 순서가 뒤섞였다.
타입·주제별로 파일을 나누고, 하루에 한 단계씩 진행한다.

### 목표 구조

```
Python/
├── README.md            ← 전체 목차 + 한 줄 치트시트
├── 문법/
│   ├── 내장함수.md        ← 숫자 / 이터러블 처리 / 문자 / 기타로 묶기
│   ├── 입출력.md          ← input, sys.stdin, print
│   ├── str 메서드.md
│   ├── list 메서드.md
│   ├── dict·set 메서드.md
│   ├── 정렬.md            ← sorted/sort + 정렬 람다 활용법 합치기
│   └── 표준 라이브러리.md
└── 알고리즘/
    └── BFS.md, DFS.md, 구현.md
```

### 진행 상황

| 단계 | 작업 | 상태 | 완료일 |
| --- | --- | --- | --- |
| 1 | `Python/README.md` 만들기 (문서 목록 + 정리 계획) | ✅ | 2026-10-15 |
| 2 | 오류 2개 수정: divmod 확인 공식 예시, `sum(리스트, [])` 설명 | ⬜ | |
| 3 | `문법/`, `알고리즘/` 폴더 만들고 기존 파일 이동 | ⬜ | |
| 4 | `input() / sys.stdin` → `입출력.md`로 분리 | ⬜ | |
| 5 | `sorted() / list.sort()` + 정렬 람다 문서 → `정렬.md`로 합치기 | ⬜ | |
| 6 | `str.join` → `str 메서드.md`로 분리 | ⬜ | |
| 7 | 남은 내용을 `내장함수.md`로 이름 바꾸고 숫자 / 이터러블 / 문자 / 기타 순으로 재배치 | ⬜ | |
| 8 | lazy iterator 공통 설명을 한 섹션으로 모으고 enumerate·map·filter·zip의 중복 설명 정리 | ⬜ | |
| 9 | 헤딩 이름 통일 (같은 이름 헤딩 때문에 앵커가 `-1`, `-2`로 밀리는 문제) | ⬜ | |
| 10 | README에 `\| 함수 \| 한 줄 요약 \| 링크 \|` 치트시트 표 추가 | ⬜ | |

### 이후 추가할 내용

정리가 끝난 뒤 하나씩 추가한다.

- **내장 함수**: `print(sep, end)`, `range`, `any`/`all`, `abs`/`round`/`pow`, `bin`/`oct`/`hex`, `reversed`, `iter`/`next`
- **str 메서드**: `split`/`strip`, `replace`, `find`/`index`/`count`, `startswith`/`endswith`, `isdigit`/`isalpha`, `zfill`/`rjust`, f-string 포맷
- **list 메서드**: `append`/`extend`/`insert`, `pop`/`remove`, 복사와 2차원 배열 얕은 복사 함정
- **dict·set 메서드**: `get`, `setdefault`, `items`, 집합 연산자 `| & - ^`
- **표준 라이브러리**: `collections`(Counter, deque, defaultdict), `heapq`, `bisect`, `itertools`, `math`, `functools`

### 기록

- **2026-10-15** 1단계: README 만들고 정리 계획 작성
