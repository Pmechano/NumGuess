import tkinter as tk

def hide_button():
    button.destroy()  # 删除按钮

# 创建主窗口
root = tk.Tk()
root.title("按钮消失示例")
root.geometry("300x200")

# 创建一个按钮
button = tk.Button(root, text="点击我消失", command=hide_button)
button.pack(pady=50)  # 使用 pack 布局，增加上下间距

# 启动主循环
root.mainloop()
