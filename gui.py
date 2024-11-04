import subprocess
import tkinter as tk
from randomText import RandomText
from weather import Weather
from guessProgram import GuessProgram

def endGame():
    inputBox.bind('<Return>', lambda dummy: exit(0))
    confirmButton.config(command=lambda : exit(0))

def checkGuess():
    msg = str()
    try:
        num = int(inputBox.get())
        inputBox.delete(0, tk.END)
        output = guess.tryGuess(num)
        if output[0] == 0:
            endGame()
        msg = output[1]
    except ValueError:
        msg = "Error"
    result.config(text=msg)

def getStart():
    Start_label.destroy()
    Start.destroy()

    global inputBox
    inputBox = tk.Entry(root, justify='center')
    inputBox.bind('<Return>', lambda dummy: checkGuess())
    inputBox.pack(side='top',pady = 15,anchor='center')

    global confirmButton
    confirmButton = tk.Button(root,text="确认",command=checkGuess)
    confirmButton.pack(side='bottom',pady = 15,anchor='center')

    global result
    result = tk.Label(root, text="请输入数字", anchor='center')
    result.pack(side='top',pady = 15,anchor='center')

if __name__ == "__main__":
    # 创建主窗口
    root = tk.Tk()
    root.title("N u m G u e s s")

    # 获取随机行
    randText = RandomText()
    wea = Weather()

    # 创建左下方的标签
    left_label = tk.Label(root, text=randText.getRand(), anchor='w')  # anchor='w' 表示文本左对齐
    left_label.pack(side='left', padx=10, pady=10, anchor='sw')  # sw 表示左下角

    # 创建右下方的标签
    right_label = tk.Label(root, text=wea.getWea(), anchor='e')  # anchor='e' 表示文本右对齐
    right_label.pack(side='right', padx=10, pady=10, anchor='se')  # se 表示右下角

    # 创建正项目
    guess = GuessProgram()
    Start_label = tk.Label(root,text=guess.rules(),anchor="n")
    Start_label.pack(side="top",padx=10,pady=10,anchor="center")

    Start = tk.Button(root,text="确认",command=getStart)
    Start.pack(side="bottom",pady=10,anchor="center")

    #运行主循环
    root.mainloop()
