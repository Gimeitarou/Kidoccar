#Copyright (c) 2025 Gimeitarou
#This software is released under the MIT License, see LICENSE.

import pyautogui
import tkinter as tk
from tkinter import messagebox

def start_process():#ふたつめのUI,表示2,注意喚起を理解した！ボタンを押した後のUI
    instruction_label.config(text="Gaidai Passで通知画面を開き、ページを全画面表示にしてください。"
                               +"\n全画面にできたら、下にあるボタンを押してください。\n"
                               +"\n1回の動作ごとに、5個の通知を既読にしていきます。"
                               +"\n5個既読し終えたら通知がまだ残っているかを適宜確認します。\n"
                               +"\nそれでは、全画面にでき次第、ボタンを押してくださいね。")
    start_button.pack_forget() #注意喚起を理解した！ボタンを非表示にする
    confirm_button.pack(pady=20) #全画面にしました！ボタンを表示する

def continue_process():#ユーザーが「全画面にしました！」ボタンを押した後に実行されるメイン処理
    root.destroy()#UIの消去
    #以下、メイン処理
    Res = ''
    while Res != 'no':
        for i in range(5):
            pyautogui.click(1210, 452, button="right",interval=0.5)#0.5secごと
        Res = messagebox.askquestion("既読操作の継続確認", "まだ通知が残っているのなら'はい'を、全て既読にできたのなら'いいえ'を押してください。")
    
    messagebox.showinfo("挨拶", "動作は以上です。\nご協力ありがとうございました。")#最終UI

#メインUIの作成(一番はじめの動作)
root = tk.Tk()
root.title("Kidokkar")
root.geometry("660x240") #UIサイズ

#初めに表示されるUI,表示1
instruction_label = tk.Label(
    root,
    text="<<プログラムを使うにあたっての注意事項です。>>\n"
        +"\n通知のなかには見逃すと不利益を被るたぐいのものがあります。"
        +"\n既読をつけてよいとあなたが判断した通知のみ"
        +"\nプログラムが既読をつける対象となるようにあなたが責任を持ってください。\n"
        +"\nご理解の程よろしくお願いします。",
    font=("Helvetica", 12)
)
instruction_label.pack(pady=20)

#表示1のボタン
start_button = tk.Button(root, text="理解しました", command=start_process, font=("Helvetica", 12))
start_button.pack(pady=15)

#ユーザーが全画面表示を完了したことを確認するためのボタン（最初は非表示）(表示2のボタン)
confirm_button = tk.Button(root, text="ページを全画面表示できました！", command=continue_process, font=("Helvetica", 12))
#表示2のボタンを表示してくれる行は冒頭の定義start_process()内に

root.mainloop()