# BFS (너비 우선 탐색) 정리

##   1. BFS란?

**BFS (Breadth-First Search, 너비 우선 탐색)** 는 그래프나 트리를 탐색하는 알고리즘 중 하나로, **시작 노드에서 가까운 노드부터 차례대로 탐색**하는 방식이다.

- 현재 노드와 인접한 노드를 먼저 모두 방문한 뒤, 그 다음 레벨의 노드들을 탐색
- **큐(Queue) 자료구조**를 사용 (FIFO: First In First Out)
- **최단 경로 문제**에서 자주 사용됨 (간선의 가중치가 모두 같을 때)

---

##   2. BFS의 동작 원리

### 탐색 과정

1. 시작 노드를 큐에 넣고, 방문 표시를 한다.
2. 큐에서 노드를 하나 꺼낸다.
3. 꺼낸 노드와 인접하면서 아직 방문하지 않은 노드들을 모두 큐에 넣고 방문 표시한다.
4. 큐가 빌 때까지 2~3번 과정을 반복한다.

### 시각적 예시

다음과 같은 그래프가 있다고 가정하자.

```
      1
     / \
    2   3
   / \   \
  4   5   6
```

**BFS 탐색 순서**: `1 → 2 → 3 → 4 → 5 → 6`

레벨별로 탐색하기 때문에 같은 깊이의 노드들을 먼저 모두 방문한 뒤, 다음 깊이로 넘어간다.

---

##   3. 파이썬 기본 구현

### 3-1. `collections.deque` 사용 (권장)

파이썬의 기본 리스트를 큐로 사용하면 `pop(0)` 연산이 O(n)이므로 비효율적이다. `deque`는 양쪽 끝에서의 삽입/삭제가 O(1)이므로 반드시 이것을 사용하자.

```python
from collections import deque

def bfs(graph, start):
    visited = [False] * (len(graph) + 1)  # 방문 여부 저장
    queue = deque([start])                # 큐 초기화
    visited[start] = True                 # 시작 노드 방문 처리

    while queue:
        node = queue.popleft()            # 큐에서 노드 꺼내기
        print(node, end=' ')              # 방문 처리한 노드 출력

        # 인접 노드 중 방문하지 않은 노드를 큐에 삽입
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# 그래프 정의 (인접 리스트)
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

bfs(graph, 1)
# 출력: 1 2 3 4 5 6
```

### 3-2. 핵심 포인트

- `visited[start] = True`는 **큐에 넣을 때** 처리해야 한다. 꺼낼 때 처리하면 중복 삽입 발생 가능.
- `deque.popleft()`는 O(1), 리스트의 `pop(0)`은 O(n)이므로 반드시 `deque` 사용.

---

##   4. 시간 복잡도 & 공간 복잡도

| 구분 | 복잡도 |
|------|--------|
| 시간 복잡도 | **O(V + E)** |
| 공간 복잡도 | **O(V)** |

- V: 정점(Vertex)의 수
- E: 간선(Edge)의 수
- 모든 정점과 간선을 한 번씩 확인하므로 O(V + E)

---

##   5. BFS vs DFS 비교

| 항목 | BFS | DFS |
|------|-----|-----|
| 자료구조 | 큐(Queue) | 스택(Stack) 또는 재귀 |
| 탐색 방식 | 가까운 노드부터 | 깊은 노드부터 |
| 최단 경로 | ✅ 가능 (가중치 없는 그래프) | ❌ 보장 안 됨 |
| 메모리 사용 | 상대적으로 많음 | 상대적으로 적음 |
| 구현 난이도 | 쉬움 | 재귀 쓰면 쉬움 |

---

##   6. BFS 응용 예제

### 6-1. 최단 거리 구하기

가중치 없는 그래프에서 시작 노드부터 각 노드까지의 최단 거리를 구할 수 있다.

```python
from collections import deque

def bfs_shortest_distance(graph, start):
    distance = {node: -1 for node in graph}  # -1은 방문하지 않음을 의미
    distance[start] = 0
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return distance

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

print(bfs_shortest_distance(graph, 1))
# {1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2}
```

### 6-2. 2차원 격자에서의 BFS (미로 탐색)

백준, 프로그래머스에서 자주 나오는 유형이다.

```python
from collections import deque

def maze_bfs(maze):
    n = len(maze)      # 행의 수
    m = len(maze[0])   # 열의 수

    # 상, 하, 좌, 우 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False] * m for _ in range(n)]
    queue = deque([(0, 0, 1)])  # (x, y, 거리)
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        # 도착지에 도달하면 거리 반환
        if x == n - 1 and y == m - 1:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 체크 + 벽(0)이 아니며 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maze[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

    return -1  # 도달 불가능

# 1은 길, 0은 벽
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

print(maze_bfs(maze))  # 최단 거리 출력
```

### 6-3. 연결 요소(Connected Components) 개수 세기

```python
from collections import deque

def count_components(graph, n):
    visited = [False] * (n + 1)
    count = 0

    for start in range(1, n + 1):
        if not visited[start]:
            # 새로운 연결 요소 발견
            count += 1
            queue = deque([start])
            visited[start] = True

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

    return count

graph = {
    1: [2],
    2: [1],
    3: [4],
    4: [3],
    5: []
}

print(count_components(graph, 5))  # 3 (1-2, 3-4, 5)
```

---

##   7. BFS를 언제 사용할까?

다음과 같은 상황에서 BFS를 고려하자.

- **최단 경로** 를 구해야 할 때 (가중치가 모두 동일한 경우)
- **레벨 단위** 로 탐색해야 할 때 (예: 트리의 각 레벨별 처리)
- **가까운 노드부터** 확인해야 할 때
- 미로 찾기, 길찾기 문제
- 네트워크에서 n단계 이내의 노드 찾기

반대로 **경로의 존재 여부** 만 확인하거나 **모든 경로를 탐색** 해야 할 때는 DFS가 적합할 수 있다.

---

##   8. 자주 하는 실수

1. **방문 처리 시점 오류**: 큐에서 꺼낼 때 방문 처리하면 중복 삽입 발생. 반드시 **큐에 넣을 때** 방문 처리.
2. **리스트를 큐로 사용**: `pop(0)`은 O(n)이므로 시간 초과 발생. `deque` 사용 필수.
3. **방향 벡터 실수**: 2차원 격자 문제에서 `dx`, `dy` 순서 헷갈리지 않도록 주의.
4. **범위 체크 누락**: 격자 문제에서 `0 <= nx < n` 등의 경계 확인 필수.

---

##   9. 연습 문제 추천 (백준 기준)

| 번호 | 제목 | 난이도 |
|------|------|--------|
| 1260 | DFS와 BFS | 입문 |
| 2178 | 미로 탐색 | 초급 |
| 7576 | 토마토 | 초급 |
| 2606 | 바이러스 | 초급 |
| 1697 | 숨바꼭질 | 중급 |
| 7569 | 토마토 (3차원) | 중급 |
| 2146 | 다리 만들기 | 중급 |

---

##   10. 마무리 요약

- BFS는 **큐 기반의 너비 우선 탐색** 알고리즘이다.
- 파이썬에서는 반드시 `collections.deque` 를 사용한다.
- **가중치 없는 최단 경로** 문제에 최적이다.
- 방문 처리는 **큐에 넣는 순간**에 해야 한다.
- 2차원 격자, 그래프 탐색, 최단 거리 문제에 폭넓게 쓰인다.

**핵심 템플릿을 외워두자!**

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        # 처리 로직
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```