# [Silver V] 집합 - 11723

[문제 링크](https://www.acmicpc.net/problem/11723)

### 성능 요약

메모리: 128340 KB, 시간: 2892 ms

### 분류

구현, 비트마스킹

### 제출 일자

2025년 5월 8일 22:21:18

### 문제 설명

<p>비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.</p>

<ul>
	<li><code>add x</code>: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.</li>
	<li><code>remove x</code>: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.</li>
	<li><code>check x</code>: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)</li>
	<li><code>toggle x</code>: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)</li>
	<li><code>all</code>: S를 {1, 2, ..., 20} 으로 바꾼다.</li>
	<li><code>empty</code>: S를 공집합으로 바꾼다.</li>
</ul>

### 입력

 <p>첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.</p>

<p>둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.</p>

### 출력

 <p><code>check</code> 연산이 주어질때마다, 결과를 출력한다.</p>

### 메모

[파이썬 집합(Set) 사용법](https://ctkim.tistory.com/entry/Python-%EC%9E%85%EB%AC%B8-%EA%B0%95%EC%A2%8C-12-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%91%ED%95%A9Set-%EC%A0%95%EB%A6%AC-%EB%B0%8F-%EC%82%AC%EC%9A%A9%EB%B2%95)

[리스트 컴프리헨션](https://wikidocs.net/22#_1)

[딕셔너리(Dictionary)와 집합(Set)](https://dev-studyingblog.tistory.com/14)

- 파이썬 시간 최적화(GPT)
