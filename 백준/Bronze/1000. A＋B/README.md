# [Bronze V] A+B - 1000 

[문제 링크](https://www.acmicpc.net/problem/1000) 

### 성능 요약

메모리: 32412 KB, 시간: 44 ms

### 분류

구현, 사칙연산, 수학

### 제출 일자

2025년 2월 26일 02:48:47

### 문제 설명

<p>두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)</p>

### 출력 

 <p>첫째 줄에 A+B를 출력한다.</p>

---

### 사용 언어
* python 3

### 제출
```python
i = input() #str
i = i.split(' ')
ii = int(i[0]) + int(i[1])
print(ii)
```

### 배운 내용
* input() <br>
 - input : 함수
 - () : 호출
 - 문자열 반환
* input().split() <br>
  - 문자열에서만 가능한 함수
  - 리스트로 반환
* int() <br>
  - int : 함수
  - 하나의 값만 정수로 반환
  - 문자를 인식 못함 int('1, 2'), int('1 2') 다 에러
    
* map((함수)int, (리스트)input().split()) <br>
  - map : 함수 (*호출할 수 있으면 다 함수)
  - 인자에도 함수가 들어감 -> 고차 함수 (함수를 쓰는 함수)
 
---

### 다른 답
```python
# 변수 두 개 = 입력도 두 개
a, b = map(int, input().split())
print(a+b)
```

```python
print(sum(map(int, input().split())))
```
