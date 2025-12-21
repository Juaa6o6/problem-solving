# [D3] [S/W 문제해결 기본] 4일차 - 거듭 제곱 - 1217 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14dUIaAAUCFAYD) 

### 성능 요약

메모리: 51,328 KB, 시간: 59 ms, 코드길이: 249 Bytes

### 제출 일자

2025-12-21 15:10

### 기록

#### 재귀함수의 계산 타이밍에 따른 연산 속도
20ms(약 25% 단축)라는 차이는 알고리즘 문제 풀이에서 꽤 유의미한 수치이기 때문에 흥미로워 기록함.

#### 1. 꼬리 재귀(Tail Recursion)' 형태의 로직 vs 일반 재귀 형태의 로직
- 계산을 언제 하느냐(타이밍)와 돌아올 때 할 일이 있느냐(Return Path)의 차이 때문임.

> <strong>"갈 때 계산" vs "올 때 계산"</strong>

#### [갈 때 계산] (59ms)
```python
def recur(num, cnt):
    global d, n
    if cnt == d:
        return num

    total = num
    return recur(total*n, cnt+1)

for _ in range(10):
    T = int(input())
    n, d = map(int, input().split())
    res = recur(n, 1)

    print(f'#{T} {res}')
```

1. **호출 전:** 곱셈(`total * n`)을 **먼저 수행**해서 값을 만듦.
2. **호출:** 계산된 값을 들고 다음 방으로 들어감.
3. **반환(Return):** 가장 깊은 곳에서 답이 나오면, 중간 단계의 함수들은 그 값을 **그냥 뒤로 전달만(Pass)** 함
* 할 일: `return (받은 값)` → **단순 배달**



#### [올 때 계산] (79ms)
```python
def recur(n, d):
    if d == 0:
        return 1
 
    return n * recur(n, d-1)
 
 
for _ in range(10):
    t = int(input())
    n, d = map(int, input().split())
 
    res = recur(n, d)
    print(f'#{t} {res}')
```

1. **호출:** 일단 다음 방을 먼저 호출. (계산 아직 안 함)
2. **반환(Return):** 가장 깊은 곳에서 `1`을 들고 나오면, 그때부터 일이 시작됨.
3. **계산:** 돌아온 값에 `n`을 곱하는 연산을 수행함.
* 할 일: `return n * (받은 값)` → **계산 후 배달**



---

#### 2. 왜 [갈 때 계산]이 더 빠를까?

컴퓨터(인터프리터) 입장에서 **'돌아오는 길(Unwinding)'**의 부담이 다름.

* **[갈 때 계산] 코드 (Tail Recursion Style):**
함수가 리턴될 때, 스택 프레임에서 추가적인 연산 없이 값만 툭 던져주면 됨. 파이썬 바이트코드 입장에서 `RETURN_VALUE` 명령만 실행하면 되는 구조에 가까움. 이미 계산이 끝난 상태(Accumulator)로 내려갔기 때문임.
* **[올 때 계산] 코드 (General Recursion):**
함수가 리턴되어 돌아왔을 때, **CPU를 다시 써야 합니다.**
1. 돌아온 값을 받는다.
2. 메모리에 있는 `n`을 꺼낸다.
3. 둘을 곱한다(`BINARY_MULTIPLY`).
4. 그 결과를 리턴한다.


즉, **돌아오는 길마다 멈춰서 곱셈 숙제를 하고 오는 것**과 같음. 이 미세한 연산 비용과 메모리 접근 비용이 쌓여서 20ms의 차이를 만든 것.

#### 3. 요약 및 결론

[갈 때 계산] 코드는 **'누산기(Accumulator)'** 패턴을 사용한 방식.

* **[올 때 계산] 코드:** 수학적 점화식()을 그대로 옮겨서 가독성이 좋음.
* **[갈 때 계산] 코드:** 결과를 인자로 계속 전달()하여, 함수가 끝날 때 추가 연산이 없도록 최적화함.

**결론적으로,**
파이썬은 함수 호출 비용이 비싼 언어인데, [갈 때 계산] 방식은 **"함수가 리턴할 때 추가 연산을 하지 않도록"** 로직을 짰기 때문에, 인터프리터가 조금 더 수월하게 처리한 것임.


> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
