import tkinter as tk
from tkinter import messagebox

def start_process():
    # ユーザーに指示を出す
    instruction_label.config(text="Google Chromeを全画面表示にしてください。\n完了したら、下のボタンを押してください。")
    start_button.pack_forget() # 開始ボタンを非表示にする
    confirm_button.pack(pady=20) # 確認ボタンを表示する

def continue_process():
    # ユーザーが「完了しました」ボタンを押した後の処理
    instruction_label.config(text="全画面表示の確認ができました！\n次の処理に進みます。")
    confirm_button.pack_forget() # 確認ボタンを非表示にする

    messagebox.showinfo("処理完了", "次の処理を開始します。")
    # --- ここにユーザーが全画面表示にした後に実行したい処理を記述 ---
    print("全画面表示の確認後、処理が実行されました。")
    # --------------------------------------------------------------------

# メインウィンドウの作成
root = tk.Tk()
root.title("全画面表示確認プログラム")
root.geometry("400x200") # ウィンドウサイズを設定

# 指示を表示するラベル
instruction_label = tk.Label(root, text="「開始」ボタンを押して、指示に従ってください。", font=("Helvetica", 12))
instruction_label.pack(pady=30)

# 処理を開始するためのボタン（最初はこれだけ表示）
start_button = tk.Button(root, text="開始", command=start_process, font=("Helvetica", 12))
start_button.pack(pady=10)

# ユーザーが全画面表示を完了したことを確認するためのボタン（最初は非表示）
confirm_button = tk.Button(root, text="Chromeを全画面にしました！", command=continue_process, font=("Helvetica", 12))
# confirm_button.pack() は start_process() 内で呼び出す

root.mainloop()
