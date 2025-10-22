# test/test_invert_tree.py
# ---------------------------------------------------------------
# 單元測試：驗證 invertTree() 是否能正確反轉二元樹結構
# 使用 pytest 進行參數化測試（多組輸入一次測多案例）
# ---------------------------------------------------------------

import sys, os
# 將上層目錄加入 Python 模組搜尋路徑
# 使得 pytest 在 test/ 目錄下仍能匯入 source/main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 從主程式匯入三個核心函式
# - build_tree(): 建構二元樹
# - invertTree(): 執行反轉演算法
# - level_order(): 將結果以層序遍歷轉成 list 方便比對
from source.main import build_tree, invertTree, level_order

# 匯入 pytest 以使用 @pytest.mark.parametrize 等裝飾器
import pytest

# 使用 pytest 參數化測試裝飾器：
# 對同一個測試函式提供多組 (input, expected) 測資
@pytest.mark.parametrize(
    "inp, expected",
    [
        # example 1:
        # 原樹結構 [5,3,8,1,7,2,6]
        #   反轉後 => [5,8,3,6,2,7,1]
        ([5, 3, 8, 1, 7, 2, 6], [5, 8, 3, 6, 2, 7, 1]),

        # example 2:
        # 只有兩層，左右節點互換即可
        ([6, 8, 9], [6, 9, 8]),

        # example 3:
        # 範例含 None，測試不完整樹結構是否仍能正確反轉
        (
            [5, 3, 8, 1, 7, 2, 6, 100, 3, -1],
            [5, 8, 3, 6, 2, 7, 1, None, None, None, None, None, -1, 3, 100],
        ),

        # example 4:
        # 空樹（無節點）
        ([], []),

        # example 5:
        # 僅單節點，反轉結果相同
        ([-2], [-2]),

        # example 6:
        # 含負數且兩層結構
        ([-1, -2, -3], [-1, -3, -2]),
    ],
)


def test_invert_tree_iterative(inp, expected):
    """
    測試目標：
    驗證 invertTree() 反轉邏輯的正確性。
    將層序輸入陣列建構成樹後，反轉並輸出層序結果，
    比對是否與預期結果相符。
    """

    # Step 1：由輸入陣列建構二元樹
    root = build_tree(inp)

    # Step 2：執行反轉演算法
    out_root = invertTree(root)

    # Step 3：以層序輸出結果，與預期值比對
    assert level_order(out_root) == expected

