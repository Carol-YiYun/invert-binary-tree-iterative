# source/main.py

# 從 app 模組匯入三個核心函式：
# build_tree()  - 根據層序陣列建構二元樹
# invertTree()  - 反轉二元樹（左右子樹互換）
# level_order() - 以層序遍歷回傳結果（列表格式）
from source.app import build_tree, invertTree, level_order

# 當此檔案以主程式執行時才會執行以下區塊
# 若是被匯入（import main），則不會執行
if __name__ == "__main__":
    # 輸出說明訊息，提示使用者輸入格式
    print("Enter tree values in level order, separated by commas.")
    print("Use 'None' for null nodes (example: 4,2,7,1,3,6,9):")

    # 從標準輸入讀取使用者輸入的樹節點序列
    # strip() 去除首尾空白
    user_input = input("> ").strip()

    try:
        # 將輸入字串以逗號分隔，逐一轉換為整數或 None
        # - 若字串為 "None"（大小寫不拘），轉為 Python None
        # - 否則轉為整數
        # 範例輸入："4,2,7,1,3,6,9"
        # 範例輸出：[4, 2, 7, 1, 3, 6, 9]
        values = [
            int(x) if x.strip().lower() != "none" else None 
            for x in user_input.split(",")
        ]
        
        # 根據輸入的陣列建立二元樹結構
        root = build_tree(values)

        # 執行反轉演算法
        inverted = invertTree(root)

        # 以層序遍歷方式輸出反轉後的樹
        print("Inverted tree (level order):", level_order(inverted))

    # 捕捉任何可能的例外，例如：
    # - 使用者輸入非數字或格式錯誤
    # - 建樹過程發生型別錯誤
    except Exception as e:
        print("Error:", e)