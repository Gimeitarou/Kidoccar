#Copyright (c) 2025 Gimeitarou
#This software is released under the MIT License, see LICENSE.

import pyautogui
import tkinter as tk
from tkinter import messagebox

def continue_process():#ユーザーが「全画面にしました！」ボタンを押した後に実行される処理。
    root.destroy()#UIの消去
    Response = ''
    while Response != 'no':
        for i in range(10):
            pyautogui.click(1210, 452, button="right",interval=1)#1secごと
        Response = messagebox.askquestion("既読操作の継続確認", "まだ通知が残っているのなら'はい'を、全て既読にできたのなら'いいえ'を押してください。")
    
    messagebox.showinfo("挨拶", "ご協力ありがとうございました。終わりです。")

#動作の開始から最初に表示される注意喚起をするUI
messagebox.showinfo("注意喚起","通知のなかには見逃すと不利益を被るたぐいのものがあります。既読をつけてよいとあなたが判断した通知のみをこのプログラムが既読をつける対象となるようにあなたが責任を持ってください。")

# メインウィンドウの作成
root = tk.Tk()
root.title("全画面表示確認")
root.geometry("660x240") # ウィンドウサイズを設定

# 指示を表示するラベル
instruction_label = tk.Label(
    root,
    text="Gaidai Passで通知画面を開き、ページを全画面表示にしてください。"
                               +"\n全画面にできたら、下にあるボタンを押してください。\n"
                               +"\n1回の動作ごとに、10個の通知を既読にしていきます。"
                               +"\n10個既読し終えたら通知がまだ残っているかを適宜確認します。\n"
                               +"\nそれでは、全画面にでき次第、ボタンを押してくださいね。",
    font=("Helvetica", 12)
)
instruction_label.pack(pady=20)

# ユーザーが全画面表示を完了したことを確認するためのボタン
confirm_button = tk.Button(
    root,
    text="ページを全画面表示できました！",
    command=continue_process,#上で定義した「全画面にしました！」ボタンを押した後に実行される処理
    font=("Helvetica", 12),
    padx=10, # ボタンの左右のパディング
    pady=5   # ボタンの上下のパディング
)
confirm_button.pack(pady=10)

# Tkinterイベントループの開始
root.mainloop()