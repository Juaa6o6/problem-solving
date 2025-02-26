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

### 힌트
[여기](https://help.acmicpc.net/language/info) 를 누르면 1000번 예제 소스를 볼 수 있습니다.

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
* 함수() : 함수 호출
  - [함수의 구조](https://wikidocs.net/24#_5)
    + 입력값을 주었을 때 어떤 처리를 하여 결괏값을 리턴 <br>
    
      ```python
      def 함수_이름(매개변수):
          수행할_문장1 <br>
          수행할_문장2 <br>
          ...
          return 리턴값
      
      변수 = 함수_이름(인수)
      print(변수)
      >>> 리턴값
      ```
    + 매개변수(parameter): 함수에 입력으로 전달되는 값을 받는 변수
    + 인수(arguments): 함수를 호출할 때 전달하는 입력값
      ```python
      def add(a, b):  # a, b는 매개변수
          return a+b
      
      print(add(3, 4))  # 3, 4는 인수
      ```
  - 입력값과 리턴값이 있는 함수의 사용법 <br>
  
     + 리턴값을_받을_변수 = 함수_이름(입력_인수1, 입력_인수2, ...) <br>
       
       ```python
       def 함수_이름(a, b):  # 매개변수
           result = a + b   # 수행할_문장
           ...
           return result    # 리턴값
       a = 함수_이름(3, 4)
       print(a)
       >>> 7
       ```
  - 입력값이 없는 함수 <br>
     + 리턴값을_받을_변수 = 함수_이름() <br>
     
       -> 변수에 리턴값이 대입됨 <br>
       
       -> 매개 변수가 없기 때문에 인수도 없어야 작동함
          ```python
          def 함수_이름():   
              ...
              return 리턴값 (e.g., 'Hi')
          a = 함수_이름()
          print(a)
          >>> Hi
          ```
  - 리턴값이 없는 함수 <br>
     + 함수_이름(입력_인수1, 입력_인수2, ...) <br>
     
       -> 리턴값을 변수에 대입하고 변수를 출력해 보면 리턴값이 None 으로 나옴
       ```python
       def 함수_이름(a, b):
           수행할_문장 (e.g., print("%d, %d의 합은 %d입니다." % (a, b, a+b))
       a = 함수_이름(3, 4))
       print(a)
       >>> 3, 4의 합은 7입니다.
       >>> None
       ```
   - 입력값, 리턴값 모두 없는 함수
      + 함수_이름() <br>
      
        -> 매개변수, return 문도 없는 함수
        ```python
        def 함수_이름():
            수행할_문장 (e.g., print('Hi)
        함수_이름()
        >>> Hi
        ```
* input()
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
  - 여러 개의 데이터를 받아서 각각의 요소에 함수를 적용한 결과를 반환하는 내장 함수
  - 인자에도 함수가 들어감 -> 고차 함수 (함수를 쓰는 함수)
  ([출처](https://dotiromoook.tistory.com/28))
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
