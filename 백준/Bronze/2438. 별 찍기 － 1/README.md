# [Bronze V] 별 찍기 - 1 - 2438

[문제 링크](https://www.acmicpc.net/problem/2438)

### 성능 요약

메모리: 32544 KB, 시간: 32 ms

### 분류

구현

### 제출 일자

2025년 3월 8일 22:34:21

### 문제 설명

<p>첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제</p>

### 입력

 <p>첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.</p>

### 출력

 <p>첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.</p>

### 예제 입력

```
5
```

### 예제 출력

```
*
**
***
****
*****
```

<br>

---

### 사용 언어

- python 3

### 제출

```python
n = int(input())
for i in range(1, n+1) :
    print('*' * i)
```

<br>

---

### 다른 답

```python
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1, n + 1):
    sys.stdout.write('*' * i + '\n')
```
