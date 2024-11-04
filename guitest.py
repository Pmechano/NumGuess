import tkinter as tk
from randomText import RandomText
from weather import Weather
from guessProgram import GuessProgram

def getStart():
    Start_label.destroy()  # 销毁开始标签
    Start.destroy()        # 销毁开始按钮

    # 创建输入框
    inputBox = tk.Entry(root, justify='center')  # 使用 justify 来居中输入文本
    inputBox.pack(side='top', pady=15)

    # 创建确认按钮并绑定功能
    confirmButton = tk.Button(root, text="确认", command=lambda: showResult(inputBox.get()))
    confirmButton.pack(side='bottom', pady=15)

    # 创建结果标签
    result = tk.Label(root, text="", anchor='center')  # 初始文本为空
    result.pack(side='top', pady=15)

def showResult(user_input):
    # 在这里处理用户输入并更新结果标签
    result.config(text=f"你输入的内容是: {user_input}")

if __name__ == "__main__":
    # 创建主窗口
    root = tk.Tk()
    root.title("N u m G u e s s")

    # 获取随机行
    randText = RandomText()
    wea = Weather()

    # 创建左下方的标签
    left_label = tk.Label(root, text=randText.getRand(), anchor='w')
    left_label.pack(side='left', padx=10, pady=10, anchor='sw')

    # 创建右下方的标签
    right_label = tk.Label(root, text=wea.getWea(), anchor='e')
    right_label.pack(side='right', padx=10, pady=10, anchor='se')

    # 创建正项目
    guess = GuessProgram()
    Start_label = tk.Label(root, text=guess.rules(), anchor="n")
    Start_label.pack(side="top", padx=10, pady=10, anchor="center")

    Start = tk.Button(root, text="确认", command=getStart)
    Start.pack(side="bottom", pady=10, anchor="center")

    # 运行主循环
    root.mainloop()
