import sys
import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
from datetime import datetime
from tkinter import filedialog as tkfd

musicList = []                      #フォルダ内の曲を入れるためのリスト
main_window = tk.Tk()
main_window.title("CentOS Clock")   #タイトルバー
main_window.geometry("400x180")     #画面サイズ　横×縦

timeLabel = tk.Label(text="時間：") #時間設定の部分
timeLabel.place(x=10, y=10)         #ラベルをmain_window上にx×y上に表示


#時のコンボボックス
hourComboBox = ttk.Combobox(main_window, state="readonly", values=list(range(0,24)), width=2)
hourComboBox.current(0)
hourComboBox.place(x=50, y=10)

#時のラベル表示
hourLabel = tk.Label(text="時")
hourLabel.place(x=90, y=10)

#分のコンボボックス
minutesComboBox = ttk.Combobox(main_window, state="readonly", values=list(range(0,60)), width=2)
minutesComboBox.current(0)
minutesComboBox.place(x=120, y=10)

#分のラベル表示
minutesLabel = tk.Label(text="分")
minutesLabel.place(x=160, y=10)

#現在時刻の表示
def show_CurrentTime():
    nowTime = datetime.now()
    currentTime = tk.StringVar()
    currentTime.set("現在時刻："+nowTime.strftime('%Y/%m/%d %H:%M:%S'))
    currentTimeLabel = tk.Label(main_window, textvariable=currentTime)
    currentTimeLabel.place(x=200, y=10)
    main_window.after(1000, show_CurrentTime)    #1000msなので1秒ごとに更新

#音源のパス
musicPathLabel = tk.Label(text="音源のパス：")
musicPathLabel.place(x=10, y=40)

#音源のパスを入れるためのテキストボックス
musicPathTextBox = tk.Entry(width=40)
musicPathTextBox.insert(tk.END, "ここに入れた文字がテキストボックスに入ります")
musicPathTextBox.place(x=90, y=40)

def musicPathOpenDialog():
    global musicList                #グローバル変数変数musicList
    dirPath = tkfd.askdirectory()

    #ダイアログでファイルを選択して開いた時にテキストボックスの中身を空にする
    if dirPath:
        musicPathTextBox.delete(0, tk.END)

    fileList = os.listdir(dirPath)  #ディレクトリ内のファイルの取得
    musicList = fileList    #コピーしても関数を抜けたあとにコピーを保持できない問題発生中
    musicPathTextBox.insert(tk.END, dirPath)
    musicPathTextBox.place(x=90, y=40)

#音源のパスを参照するためのボタン
musicPathReferenceButton = tk.Button(text="参照", width=5, command=musicPathOpenDialog)
musicPathReferenceButton.place(x=345, y=35)


#ループとシャッフル設定のチェックボックスとチェックボックス説明用のラベル
#ループ
loopCheckBox = tk.Checkbutton()
loopLabel = tk.Label(text="：ループ")
loopCheckBox.place(x=10, y=70)
loopLabel.place(x=30, y=70)

#シャッフル
shuffleCheckBox = tk.Checkbutton()
shuffleLabel = tk.Label(text="：シャッフル")
shuffleCheckBox.place(x=100, y=70)
shuffleLabel.place(x=120, y=70)

#流している曲名を入れるためのラベル
musicNameLabel = tk.Label(text="曲名：")
musicNameLabel.place(x=10, y=100)

#ストップとスタートのボタン
switchButton = tk.Button(text="start")
switchButton.pack(fill = "x", padx=30, pady = 20, side = "bottom")

main_window.after(1, show_CurrentTime())
main_window.mainloop()
