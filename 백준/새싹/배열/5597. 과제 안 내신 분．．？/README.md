# [Bronze III] 과제 안 내신 분..? - 5597

[문제 링크](https://www.acmicpc.net/problem/5597)

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현

### 제출 일자

2025년 3월 13일 23:26:54

### 문제 설명

<p>X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.</p>

<p>교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.</p>

### 입력

 <p>입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.</p>

### 출력

 <p>출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.</p>

<br>

---

### 사용 언어

- python 3

### 제출

```python
import sys

n = list(map(int, sys.stdin.read().split()))

for i in range(1, 31) :
    n.sort()
    if n.count(i) == False :
        print(i)
```

### 메모

- sort()

  - 리스트를 정렬하는 내장 메서드

    - 새로운 정렬된 리스트 반환 X

    - 기존 리스트 자체를 변경함(직접 정렬)

  - 반환값이 None 임

    - sort() 호출 -> 리스트 정렬

    - 결과를 변수에 저장 -> None이 들어감

  - key와 reverse 옵션 제공

    - reverse=True → 내림차순 정렬
    - key=function → 특정 기준에 따라 정렬

      ```python
      words = ["apple", "banana", "cherry", "date"]
      words.sort(key=len)  # 단어 길이 기준 정렬
      print(words)  # ['date', 'apple', 'cherry', 'banana']

      ```

- split() - 공백 기준으로 나눠줌
  - 공백(스페이스, tab, 개행문자(\n)) 로 나눠줘서 strip() 함께 안 써도 됨

<br>

---

### 다른 답

```python
answer = list(range(1,31))
for i in range(28):
    answer.remove(int(input()))

print(*answer)
```

```python
s = []
for i in range(28):
    s.append(int(input()))

for i in range(1, 31):
    if i not in s:
        print(i)
```
