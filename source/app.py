# source/app.py

# 使用 collections.deque 實作高效的 BFS（雙端佇列）
from collections import deque

# 定義二元樹節點結構
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # 節點值
        self.val = val
        # 左子樹
        self.left = left
        # 右子樹
        self.right = right

# 以迭代法反轉二元樹（BFS 寬度優先遍歷）
def invertTree(root: TreeNode) -> TreeNode:
    # 空樹直接回傳 None
    if not root:
        return None
    
    # 以 deque 實作佇列，用於層序遍歷
    q = deque([root])

    # 每次取出一個節點，交換左右子樹
    while q:
        node = q.popleft()
        # 交換左右子節點
        node.left, node.right = node.right, node.left

        # 將左右節點加入佇列（若存在）
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    # 回傳根節點（已完成反轉）
    return root

# 由層序陣列建構二元樹
# 例： [4,2,7,1,3,6,9] 會建立完整的對應樹
#     [4,2,7,None,3] 則會跳過 None 節點
def build_tree(values):

    if not values:
        return None
    
    # 建立節點列表，None 代表空節點
    nodes = [TreeNode(v) if v is not None else None for v in values]

    # kids 為反轉後的節點列表（用 pop 取末端）
    kids = nodes[::-1]
    # 第一個節點為根節點
    root = kids.pop()

    # 依序將子節點連接回父節點
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root

# 回傳樹的層序遍歷結果（包含 None 以保留結構）
def level_order(root):

    if not root:
        return []

    res = [] # 儲存結果
    q = deque([root]) # BFS 佇列起點

    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            # 若為空節點，也記錄 None（方便比對樹形）
            res.append(None)

    # 移除尾端多餘的 None（不影響樹結構）
    while res and res[-1] is None:
        res.pop()
        
    return res

