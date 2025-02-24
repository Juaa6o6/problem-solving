# [Bronze V] 오늘 날짜 - 10699 

[문제 링크](https://www.acmicpc.net/problem/10699) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현

### 제출 일자

2025년 2월 25일 00:44:10

### 문제 설명

서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.

### 입력 

입력은 없다.

### 출력 

서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.

### 힌트

<p>채점 서버는 시간대(Timezone)는 UTC+0 이다.</p>
<p>다음은 채점 서버에서 KST 시간으로 2018년 3월 21일 오후 2시 7분 38초에 date 명령어를 실행시킨 결과이다.</p>

``` 
Wed Mar 21 05:07:38 UTC 2018
```
---

### 제출
```python
print("2025-02-25")
```

### 배운 내용
* datetime.datetime.now() 사용 시 오류 남<br>

  - 2025-02-25일 오전 12시 45분에 풀었지만 2025-02-24일 로 출력됨<br>
  - 입력 시간과 출력 시간이 -9 시간 차이가 나서 발생<br>
  - timezone, timedelta 사용
 

---
### 다른 답
```python
# datetime.datetime.now() 사용

import datetime

now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d")

print(formatted_date)
```

```python
# timezone, timedelta 사용

from datetime import datetime, timezone, timedelta

kst = timezone(timedelta(hours=9))

print(datetime.now(kst).strftime('%Y-%m-%d'))
```


