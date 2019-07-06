import sys
from tkinter import *
from tkinter import ttk
import tkinter as tk
from datetime import datetime

main_window = tk.Tk()
main_window.title("CentOS Clock")   #タイトルバー
main_window.geometry("400x180")     #画面サイズ　横×縦

timeLabel = tk.Label(text="時間：") #時間設定の部分
timeLabel.place(x=10, y=10)         #ラベルをmain_window上にx×y上に表示
musicVolume = tk.IntVar(master=main_window, value=50)   #音量調節用変数


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
    main_window.after(100, show_CurrentTime)    #100ms×10ms=1000msなので1秒ごとに更新。10msはmainloop()の直前のやつ

#音源のパス
musicPathLabel = tk.Label(text="音源のパス：")
musicPathLabel.place(x=10, y=40)

#音源のパスを入れるためのテキストボックス
musicPathTextBox = tk.Entry(width=40)
musicPathTextBox.insert(tk.END, "ここに入れた文字がテキストボックスに入ります")
musicPathTextBox.place(x=90, y=40)

#音源のパスを参照するためのボタン
musicPathReferenceButton = tk.Button(text="参照", width=5)
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

#音量バー
musicVolume.set("Volume："+str(musicVolume.get()))
musicVolumeLabel = tk.Label(main_window, textvariable=musicVolume)
musicVolumeLabel.place(x=190, y=70)

#音量用のラベルと音量調整
def MusicValueChanged(*args):
    global musicVolume
    global musicVolumeLabel
    musicVolume.set("Volume："+str(musicVolume.get()))
    musicVolumeLabel.place(x=190, y=70)

#音量用の変数と音量バーを紐付けるための処理
musicVolume.trace("w", MusicValueChanged)

#音量バー
volumeBar = tk.Scale(main_window, length=120, orient='h', from_=0, to=100, variable=musicVolume, showvalue=False)
volumeBar.place(x=270, y=70)

#流している曲名を入れるためのラベル
musicNameLabel = tk.Label(text="曲名：")
musicNameLabel.place(x=10, y=100)

#ストップとスタートのボタン
switchButton = tk.Button(text="start")
switchButton.pack(fill = "x", padx=30, pady = 20, side = "bottom")

main_window.after(10, show_CurrentTime())
main_window.mainloop()
