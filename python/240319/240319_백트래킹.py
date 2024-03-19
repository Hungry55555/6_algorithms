# 중복된 순열
# 1~3 까지 숫자 배열
# 111, 112, 113, 121, 122, 123 ... 332, 333

# 재귀 함수 => 특정 시점으로 돌아오는 게 핵심!
# 재귀 함수 팁
# 파라미터: 바로 작성 x
# 구조를 먼저 잡으면 자연스럽게 필요한 변수들이 보인다!


arr = [i for i in range(1,4)]
path=[0]*3

# 순열
# 123 , 132, 213, 231, 312, 321
# 조건: 숫자는 한 번 만 사용해라!

# 결과 조건 도출 문제에서 조건

# for i in arr:
#     for j in arr:
#         for k in arr:
#             print(i*100+j*10+k,end=' ')

def dfs(level):
    # 기저 조건
    # 이 문제에서는 3개를 뽑았을 때 까지 반복
    if level ==3:
        print(*path)
        return
    
    # 들어가기 전
    # 다음 재귀 호출
    # - 다음에 갈 수 있는 곳들은 어디인가?
    # - 이 문제에서는 1, 2, 3 세 가지 경우의 수가 존재
    # path[level]=arr[0]
    # dfs(level +1)
    # path[level]=arr[1]
    # dfs(level+1)
    # path[level]=arr[2]
    # dfs(level+1)
    

    # 갈 수 있는 후보군
    for i in range(len(arr)):
        # 여기는 못가! (가지치기)
        # 백트래킹 코드 팁
        # 갈수없는 경우를 활용
        # 아래 코드처럼 갈 수 없을 때 continue

        if arr[i] in path:
            continue


        path[level] = arr[i]
        dfs(level+1)
        # 갔다와서 할 로직
        # 기존 방문을 초기화
        path[level]=0
dfs(0)

x=[]
arr = [1, 2, 1, 3, 2, 4, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
# 정석 개발 버전
class TreeNode:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self,child):
        # 왼쪽에 삽입 시도
        if not self.left:
            self.left=child

            return
        # 오른쪽에 삽입 시도
        if not self.right:
            self.right = child
            return

        # 삽입 실패
        return
    
    def inorder(self):
        if self != None:
            # 왼쪽이 있으면 계속 탐색
            if self.left:
                self.left.inorder()
            print(self.value, end=' ')
            
            # 오른쪽이 있으면 계속 탐색
            if self.right:
                self.right.inorder()

# 이진 트리 만들기
# 1. 노드들을 생성
nodes = [TreeNode(i) for i in range(0,14)] 

# 2. 간선 연결
for i in range(0, len(arr),2):
    parent_node = arr[i]
    child_node = arr[i+1]
    nodes[parent_node].insert(nodes[child_node])

nodes[1].inorder()