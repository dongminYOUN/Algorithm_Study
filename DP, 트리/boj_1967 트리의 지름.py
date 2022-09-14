V = int(input())    # 정점의 개수
L = [0] * (V+1)
R = [0] * (V+1)
E = [0] * (V+1)
P = [0] * (V+1)
# 간선은 정점보다 1개 적기때문에 V-1
for i in range(V-1):      # 부모노드, 자식 노드, 간선의 가중치
    p, c, e = map(int, input().split())
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p
    # 간선 저장을 어떻게 할까. 자식을 기준으로 가중치가 저장 된다고 생각
    E[c] = e

#트리가 잘 저장됬는지 체크 한번 해보자
def preorder(v):
    if v == 0: return
    print(v, end=' ')
    preorder(L[v])
    preorder(R[v])

preorder(1)
print()
print(E)

# 어떤 한 정점을 선택함.. 그러면 여기서