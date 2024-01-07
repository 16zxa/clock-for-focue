import time
import tkinter as tk
from tkinter import messagebox

class FocusTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("专注时钟")

        # 输入框和标签
        self.label = tk.Label(self.master, text="设置专注时间（分钟）:")
        self.label.pack(pady=10)
        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=10)

        # 开始和停止按钮
        self.start_button = tk.Button(self.master, text="开始", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="停止", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        # 倒计时标签
        self.timer_label = tk.Label(self.master, text="00:00", font=("Helvetica", 24))
        self.timer_label.pack()

        # 计时状态变量
        self.running = False

    def start_timer(self):
        try:
            minutes = int(self.entry.get())
            seconds = minutes * 60
            self.countdown(seconds)
        except ValueError:
            messagebox.showerror("错误", "请输入有效的分钟数")

    def countdown(self, seconds):
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        while seconds and self.running:
            mins, secs = divmod(seconds, 60)
            self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
            self.master.update()
            time.sleep(1)
            seconds -= 1

        self.timer_label.config(text="时间到！")
        messagebox.showinfo("提示", "专注时间已结束！")

        # 计时结束后的状态恢复
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def stop_timer(self):
        self.running = False

# 创建主窗口
root = tk.Tk()
app = FocusTimer(root)

# 运行主循环
root.mainloop()
