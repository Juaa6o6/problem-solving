# 람다(lambda) 함수를 활용해 데이터를 정렬하는 방법

## 1. 정렬 메서드 비교: `list.sort()` vs `sorted()`

두 방식의 차이를 명확히 하기 위해 동일한 데이터를 기준으로 비교합니다.

```python
# 원본 데이터
numbers = [3, -1, -5, 2, 4]

# 1. sorted() 함수: 새로운 리스트를 반환, 원본 유지
new_list = sorted(numbers, key=lambda x: abs(x))
print(f"sorted() 결과: {new_list}")
print(f"원본 데이터: {numbers}")

# 2. list.sort() 메서드: 원본 리스트를 직접 수정, 반환값 없음
numbers.sort(key=lambda x: abs(x))
print(f"list.sort() 결과: {numbers}")
```

---

## 2. 단순 리스트 정렬 (Simple List)

단일 요소로 구성된 리스트에서 람다를 활용해 정렬 기준을 변경하는 예시입니다.

```python
words = ['apple', 'banana', 'kiwi', 'cherry']

# 문자열 길이를 기준으로 정렬
length_sorted = sorted(words, key=lambda x: len(x))
# 결과: ['kiwi', 'apple', 'banana', 'cherry']

# 대소문자 구분 없이 알파벳순 정렬
mixed_words = ['banana', 'Apple', 'cherry']
case_insensitive = sorted(mixed_words, key=lambda x: x.lower())
# 결과: ['Apple', 'banana', 'cherry']
```

---

## 3. 중첩 구조 정렬 (Nested Structure)

리스트 내에 튜플이나 딕셔너리가 포함된 경우, 람다를 통해 특정 요소를 지목합니다.



### 튜플(Tuple) 리스트 정렬
```python
students = [('김철수', 88), ('이영희', 95), ('박민수', 82)]

# 두 번째 요소인 '점수'를 기준으로 오름차순 정렬
score_sorted = sorted(students, key=lambda x: x[1])
# 결과: [('박민수', 82), ('김철수', 88), ('이영희', 95)]
```

### 딕셔너리(Dictionary) 리스트 정렬
```python
products = [
    {'name': 'laptop', 'price': 1200},
    {'name': 'mouse', 'price': 50},
    {'name': 'monitor', 'price': 300}
]

# 'price' 키의 값을 기준으로 정렬
price_sorted = sorted(products, key=lambda x: x['price'])
# 결과: [{'name': 'mouse', 'price': 50}, {'name': 'monitor', 'price': 300}, ...]
```

---

## 4. 다양한 정렬 조건 및 다중 조건 (Multi-level Sorting)

복합적인 정렬 기준이 필요할 때 람다에서 튜플을 반환하여 우선순위를 정합니다.

```python
# (이름, 학년, 성적)
data = [('A', 2, 90), ('B', 1, 95), ('C', 2, 85), ('D', 1, 90)]

# 1차 기준: 성적 내림차순 (-)
# 2차 기준: 학년 오름차순
complex_sorted = sorted(data, key=lambda x: (-x[2], x[1]))

# 결과 해석:
# 성적 95점이 1위 -> ('B', 1, 95)
# 성적 90점이 두 명 -> 학년이 낮은 1학년이 먼저 -> ('D', 1, 90), ('A', 2, 90)
# 성적 85점이 마지막 -> ('C', 2, 85)
```



---

# 내림차순 정렬 `reverse=True` vs `마이너스(-) 기호`

내림차순 정렬을 위해 `reverse=True`를 사용하는 것과 람다 식 내에 마이너스(`-`) 기호를 붙이는 것은 결과적으로 비슷해 보일 수 있지만, **적용 범위**와 **데이터 타입**, 특히 **다중 조건 정렬**에서 결정적인 차이가 발생합니다.


## 1. 주요 차이점 비교

| 구분 | `reverse=True` 옵션 | 람다 식 마이너스(`-`) 부호 |
| :--- | :--- | :--- |
| **적용 대상** | 정렬 결과 **전체** | 람다로 지정한 **특정 요소** |
| **데이터 타입** | 모든 타입 (문자열, 숫자 등) | **숫자형**(int, float)만 가능 |
| **다중 조건** | 모든 기준을 한꺼번에 뒤집음 | 기준마다 정렬 방향을 다르게 설정 가능 |

---

## 2. 상세 설명

### 전체를 뒤집는 `reverse=True`
이 옵션은 정렬이 완료된 최종 결과물의 순서를 통째로 거꾸로 바꿉니다. 
* 문자열, 리스트, 숫자 등 정렬 가능한 모든 데이터 타입에 사용할 수 있습니다.
* 다중 조건 정렬 시, 모든 기준에 대해 내림차순이 적용됩니다.

### 특정 요소만 뒤집는 `-` (Unary Minus)
람다 함수 내에서 특정 수치 데이터 앞에 마이너스를 붙여 값의 부호를 반전시킵니다.
* **숫자 데이터**에만 사용할 수 있습니다. 문자열 앞에는 마이너스를 붙여 정렬할 수 없습니다.
* 다중 조건 정렬 시, 어떤 기준은 오름차순으로, 어떤 기준은 내림차순으로 정렬하고 싶을 때 핵심적으로 사용됩니다.

---

## 3. 코드 예시를 통한 차이 확인

### 예시 1: 문자열 정렬 시
문자열은 마이너스 연산이 불가능하므로 반드시 `reverse=True`를 사용해야 합니다.

```python
words = ['apple', 'banana', 'cherry']

# 가능: 전체 내림차순
sorted_words = sorted(words, reverse=True) 

# 불가능: TypeError 발생
# sorted_words = sorted(words, key=lambda x: -x) 
```

### 예시 2: 다중 조건 정렬 시 (가장 큰 차이점)
성적은 높은 순(내림차순)으로, 이름은 사전 순(오름차순)으로 정렬해야 하는 상황을 가정해 보겠습니다.

```python
# (이름, 성적)
students = [('A', 80), ('B', 90), ('C', 80), ('D', 95)]

# 방법 A: reverse=True 사용
# 결과: 성적 내림차순은 되지만, 성적이 같을 때 이름도 'C' -> 'A' 순인 내림차순이 됨
result_a = sorted(students, key=lambda x: (x[1], x[0]), reverse=True)

# 방법 B: 람다 마이너스(-) 사용
# 결과: 성적(x[1])은 내림차순으로, 이름(x[0])은 오름차순으로 개별 제어 가능
result_b = sorted(students, key=lambda x: (-x[1], x[0]))

print(f"전체 역순: {result_a}")
print(f"개별 제어: {result_b}")
```

---

## 요약

1. 단순하게 하나의 기준을 내림차순으로 정렬할 때는  `reverse=True` 가 가독성이 좋고 모든 타입에 안전합니다.
2. 여러 기준을 섞어서 정렬할 때(예: 날짜는 최신순, 가격은 낮은순), 숫자 데이터에 한해  람다 마이너스(`-`) 를 사용하면 정렬 방향을 정교하게 제어할 수 있습니다.