import pyautogui
import tkinter
from tkinter import messagebox

Ready = messagebox.showinfo("UI", "Gaidai Passの通知画面を開いたWebページを全画面してください。"
                               +"\n全画面にできたら、下にある'ok'を押してください。"
                               +"\n1回の動作ごとに、10個の通知を既読にしていきます。"
                               +"\n10個を既読し終えたらまだ通知が残っているかを確認するので、また教えてください。"
                               +"\nでは、準備ができ次第、'ok'を押してください。")

if Ready == 'ok':
    Res = ''
    while Res != 'no':
        for i in range(5):
            pyautogui.click(1208, 440, button="left",interval=0.7)#1secごと
        Res = messagebox.askquestion("既読操作の継続確認", "まだ通知が残っているのなら'はい'を、全て既読にできたのなら'いいえ'を押してください。")

messagebox.showinfo("UI", "ご協力ありがとうございました。終わりです。")