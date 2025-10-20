# test_invert_tree.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from source.source import build_tree, invertTree, level_order
import pytest

@pytest.mark.parametrize(
    "inp, expected",
    [
        # example1
        ([5, 3, 8, 1, 7, 2, 6], [5, 8, 3, 6, 2, 7, 1]),
        # example2
        ([6, 8, 9], [6, 9, 8]),
        # example3（注意中間的 None 代表結構）
        (
            [5, 3, 8, 1, 7, 2, 6, 100, 3, -1],
            [5, 8, 3, 6, 2, 7, 1, None, None, None, None, None, -1, 3, 100],
        ),
        # example4: 空樹
        ([], []),
        # 其他：包含負數與單節點
        ([-2], [-2]),
        ([-1, -2, -3], [-1, -3, -2]),
    ],
)

def test_invert_tree_iterative(inp, expected):
    root = build_tree(inp)
    out_root = invertTree(root)
    assert level_order(out_root) == expected

