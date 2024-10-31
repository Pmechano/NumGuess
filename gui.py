import subprocess
import tkinter as tk
from tkinter import messagebox
import os

def get_random_line_from_a():
    try:
        print(os.listdir('.'))
        # 调用randomText.py并获取输出
        result = subprocess.run(['python3', 'randomText.py'], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"发生错误：{e}"

def show_random_line():
    random_line = get_random_line_from_a()
    messagebox.showinfo("随机行", random_line)

# 创建主窗口
root = tk.Tk()
root.title("随机行显示器")

# 创建按钮并绑定事件
button = tk.Button(root, text="显示随机行", command=show_random_line)
button.pack(pady=20)

# 运行主循环
root.mainloop()
