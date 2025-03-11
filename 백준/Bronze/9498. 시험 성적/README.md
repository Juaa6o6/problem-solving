# [Bronze V] 시험 성적 - 9498

[문제 링크](https://www.acmicpc.net/problem/9498)

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현

### 제출 일자

2025년 3월 4일 23:05:51

### 문제 설명

<p>시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.</p>

### 출력

 <p>시험 성적을 출력한다.</p>

<br>

---

### 사용 언어

- python 3

### 제출

```python
score = int(input())

if 90 <= score :
    print("A")
elif 80 <= score :
    print("B")
elif 70 <= score :
    print("C")
elif 60 <= score :
    print("D")
else :
    print("F")
```

### 메모

- if, elif, else 문

---

### 다른 답

```python
print('FFFFFFDCBAA'[int(input())//10])
# 인덱스로 반환
```
