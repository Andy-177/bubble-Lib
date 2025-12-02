import tkinter as tk
from tkinter import ttk


class BubbleBox:
    def __init__(self, root, title="消息提示", text="这是一条消息", color="#800080"):
        self.root = root
        self.title = title  # 窗口标题
        self.text = text  # 消息内容
        self.theme_color = color  # 主题色
        self.ratio = 3.45  # 固定长宽比为 3.45:1
        self.square_size = 90  # 左侧正方形区域的边长
        self.width = self.square_size + (self.square_size * self.ratio)  # 总宽度 = 正方形边长 + 右侧区域宽度
        self.height = self.square_size  # 总高度 = 正方形边长
        self.root.geometry(f"{int(self.width)}x{int(self.height)}")
        self.root.resizable(False, False)
        self.root.overrideredirect(True)  # 隐藏标题栏
        # 设置窗口初始位置（在屏幕右侧外）
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.start_x = screen_width  # 初始位置在屏幕右侧外
        self.target_x = screen_width - self.width  # 目标位置在屏幕右下角
        self.y = screen_height - self.height - 50  # 往上移动 50 像素
        self.root.geometry(f"+{int(self.start_x)}+{int(self.y)}")
        # 设置主题色
        self.text_color = self.theme_color  # 消息内容颜色
        self.bg_color = "white"  # 右边长方形区域背景色
        # 设置窗口透明度
        self.root.attributes("-alpha", 1.0)  # 初始透明度为 1.0（完全不透明）
        # 创建 Canvas 作为背景
        self.canvas = tk.Canvas(
            self.root,
            width=self.width,
            height=self.height,
            bd=0,
            highlightthickness=0,
            bg=self.theme_color
        )
        self.canvas.pack()
        # 创建主框架（背景为主题色，放在 Canvas 上方，内缩 1 像素）
        self.frame = tk.Frame(
            self.canvas,
            bg=self.theme_color,
            bd=0
        )
        self.frame.place(x=0, y=0, width=self.width - 1, height=self.height - 0.5)
        # 左边正方形区域
        self.square_frame = tk.Frame(
            self.frame,
            bg=self.theme_color,
            width=self.square_size,
            height=self.height - 2
        )
        self.square_frame.pack(side="left", fill="y")
        # 右边长方形区域（内缩 1 像素，留出边框）
        self.message_frame = tk.Frame(
            self.frame,
            bg=self.bg_color,
            width=self.width - self.square_size - 4,  # 内缩 2 像素
            height=self.height - 4  # 内缩 2 像素
        )
        self.message_frame.pack(side="right", fill="both", expand=True, padx=1, pady=1)
        # 标题（粗体，靠左，字体稍微放大）
        self.title_label = tk.Label(
            self.message_frame,
            text=self.title,
            bg=self.bg_color,
            fg=self.text_color,
            font=("Arial", 14, "bold"),
            anchor="w",
            justify="left"
        )
        self.title_label.pack(pady=(10, 5), padx=5, fill="x", expand=False)
        # 消息内容（粗体，靠左，字体稍微放大）
        self.message_label = tk.Label(
            self.message_frame,
            text=self.text,
            bg=self.bg_color,
            fg=self.text_color,
            font=("Arial", 12, "bold"),
            wraplength=self.width - self.square_size - 20,
            anchor="w",
            justify="left"
        )
        self.message_label.pack(pady=(0, 10), padx=5, fill="x", expand=False)
        # 右上角关闭按钮
        self.close_button_size = 20
        self.close_button_frame = tk.Frame(
            self.message_frame,
            bg=self.bg_color,
            width=self.close_button_size,
            height=self.close_button_size
        )
        self.close_button_frame.place(x=self.width - self.square_size - self.close_button_size - 6, y=4)
        self.close_button_frame.pack_propagate(False)
        # 创建关闭按钮
        self.close_button = tk.Button(
            self.close_button_frame,
            text="✕",
            bg=self.theme_color,
            fg="white",
            font=("Arial", 12, "bold"),
            bd=0,
            command=self.fade_out  # 调用消失动画
        )
        self.close_button.place(relx=0.5, rely=0.5, anchor="center")
        # 启动弹出动画
        self.start_animation()

    def start_animation(self):
        """从右到左的弹出动画"""
        if self.start_x > self.target_x:
            self.start_x -= 5  # 每次移动 5 像素
            self.root.geometry(f"+{int(self.start_x)}+{int(self.y)}")
            self.root.after(1, self.start_animation)  # 每 1 毫秒更新一次位置
        else:
            self.root.geometry(f"+{int(self.target_x)}+{int(self.y)}")
            # 动画完成后，设置一个定时器，4秒后自动调用 fade_out 方法
            self.root.after(4000, self.fade_out)  # 修改为4秒（4000毫秒）

    def fade_out(self):
        """逐渐透明的消失动画"""
        current_alpha = self.root.attributes("-alpha")
        if current_alpha > 0:
            new_alpha = current_alpha - 0.05  # 每次减少 0.05 的透明度
            self.root.attributes("-alpha", new_alpha)
            self.root.after(20, self.fade_out)  # 每 20 毫秒更新一次透明度
        else:
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = BubbleBox(root, title="重要提示", text="这是一条重要的消息，请注意查看！", color="#0088FF")
    root.mainloop()
