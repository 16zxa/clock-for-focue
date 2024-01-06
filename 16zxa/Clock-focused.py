import time
import tkinter as tk
from tkinter import messagebox

def start_timer():
    try:
        minutes = int(entry.get())
        seconds = minutes * 60
        countdown(seconds)
    except ValueError:
        messagebox.showerror("错误", "请输入有效的分钟数")

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        root.update()
        time.sleep(1)
        seconds -= 1
    timer_label.config(text="时间到！")
    messagebox.showinfo("提示", "专注时间已结束！")

# 创建主窗口
root = tk.Tk()
root.title("专注时钟")

# 创建标签和输入框
label = tk.Label(root, text="请设置专注时间（分钟）:")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

# 创建开始按钮
start_button = tk.Button(root, text="开始吧", command=start_timer)
start_button.pack(pady=20)

# 创建倒计时标签
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 24))
timer_label.pack()

# 运行主循环
root.mainloop()
