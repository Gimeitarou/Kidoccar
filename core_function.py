import pyautogui
import tkinter
from tkinter import messagebox

FirstRes = messagebox.showinfo("UI", "Gaidai Passの通知画面を開いたWebページを全画面してください。"
                               +"\n全画面にできたら、下にある'ok'を押してください。"
                               +"\n1回の動作ごとに、10個の通知を既読にしていきます。"
                               +"\n10個を既読し終えたらまだ通知が残っているかを確認するので、また教えてください。"
                               +"\nでは、準備ができ次第、'ok'を押してください。")

if FirstRes == 'ok':
    SecondRes = ''
    while SecondRes != 'no':
        for i in range(10):
            pyautogui.click(1210, 452, button="right",interval=1)#1secごと
        SecondRes = messagebox.askquestion("既読操作の継続確認", "まだ通知が残っているのなら'はい'を、全て既読にできたのなら'いいえ'を押してください。")

messagebox.showinfo("UI", "ご協力ありがとうございました。終わりです。")
