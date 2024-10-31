import subprocess
import tkinter as tk

def get_random_line_from_a():
    try:
        result = subprocess.run(
            ['python3', 'randomText.py'], 
            capture_output=True, 
            text=True,
            encoding="utf-8"
        )
        return result.stdout.strip()
    except Exception as e:
        return f"发生错误：{e}"

# 创建主窗口
root = tk.Tk()
root.title("随机行显示器")

# 获取随机行
random_line = get_random_line_from_a()

# 创建一个Label来显示随机行
label = tk.Label(root, text=random_line, font=('SimHei', 14))
label.pack(pady=20)

# 运行主循环
root.mainloop()
