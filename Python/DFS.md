# DFS (Depth First Search) 알고리즘 정리

## 1. 개요
**깊이 우선 탐색(DFS)**은 그래프나 트리 구조에서 한 노드로부터 시작하여 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방식입니다.

* **특징**: 최대한 깊이 내려간 뒤, 더 이상 갈 곳이 없으면 최근의 갈림길로 돌아와 다른 방향을 탐색합니다.
* **자료구조**: **스택(Stack)**을 이용하거나, **재귀 함수(Recursion)**를 통해 구현합니다.
* **탐색 방식**: 후입선출(LIFO) 원칙을 따릅니다.



---

## 2. 동작 원리
1.  탐색 시작 노드를 방문 처리하고 스택에 삽입합니다.
2.  스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면, 그 노드를 방문 처리하고 스택에 넣습니다.
3.  방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
4.  2번과 3번의 과정을 더 이상 수행할 수 없을 때까지 반복합니다.

---

## 3. 파이썬 구현 방법

### 3.1. 재귀(Recursion) 방식
가장 보편적이고 코드가 간결한 방식입니다.

```python
def dfs_recursive(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs_recursive(graph, i, visited)

# 그래프 예시 (인접 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs_recursive(graph, 1, visited)
```

### 3.2. 스택(Stack) 이용 방식
명시적인 스택 자료구조를 사용하여 구현합니다.

```python
def dfs_stack(graph, start_node):
    visited = [False] * len(graph)
    stack = [start_node]
    
    while stack:
        v = stack.pop()
        
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            
            # 인접 노드를 스택에 삽입 (작은 번호부터 방문하려면 역순으로 삽입)
            for i in reversed(graph[v]):
                if not visited[i]:
                    stack.append(i)

dfs_stack(graph, 1)
```

---

## 4. 시간 및 공간 복잡도
* **시간 복잡도**: $O(V + E)$
    * $V$: 정점(Vertex)의 개수
    * $E$: 간선(Edge)의 개수
    * 모든 노드를 한 번씩 방문하며, 각 노드에서 인접한 모든 간선을 확인하기 때문입니다.
* **공간 복잡도**: $O(V)$
    * 방문 배열 및 재귀 호출 스택(혹은 명시적 스택)에 노드의 수만큼 공간이 필요합니다.

---

## 5. 주요 활용 사례
* 그래프의 **연결 요소(Connected Components)** 찾기
* **위상 정렬(Topological Sort)**
* **미로 찾기** (경로의 존재 여부 확인)
* **사이클(Cycle)** 존재 여부 판별

---

## 6. 주의사항
* **재귀 깊이 제한**: 파이썬은 기본 재귀 깊이 제한이 있으므로, 매우 깊은 그래프를 탐색할 때는 `sys.setrecursionlimit()`을 사용하거나 스택 방식으로 구현해야 합니다.
* **방문 처리 필수**: 방문 처리를 하지 않으면 무한 루프에 빠질 위험이 있습니다.

