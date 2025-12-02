import tkinter as tk
from tkinter import ttk

class CustomMessageBox:
    def __init__(self, root, ratio=3.25):
        self.root = root
        self.ratio = ratio  # 长宽比，默认为 3.25:1
        self.square_size = 90  # 左侧正方形区域的边长
        self.width = self.square_size + (self.square_size * self.ratio)  # 总宽度 = 正方形边长 + 右侧区域宽度
        self.height = self.square_size  # 总高度 = 正方形边长
        self.root.geometry(f"{int(self.width)}x{int(self.height)}")
        self.root.resizable(False, False)
        self.root.overrideredirect(True)  # 隐藏标题栏

        # 设置窗口在右下角显示，并往上移动 50 像素
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = screen_width - self.width
        y = screen_height - self.height - 50  # 往上移动 50 像素
        self.root.geometry(f"+{int(x)}+{int(y)}")

        # 设置主题色
        self.theme_color = "#800080"  # 默认紫色
        self.text_color = self.theme_color  # 消息内容颜色
        self.bg_color = "white"  # 右边长方形区域背景色

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
        self.frame.place(x=0, y=0, width=self.width-1, height=self.height-0.5)

        # 左边正方形区域
        self.square_frame = tk.Frame(
            self.frame,
            bg=self.theme_color,
            width=self.square_size,
            height=self.height-2
        )
        self.square_frame.pack(side="left", fill="y")

        # 右边长方形区域（内缩 1 像素，留出边框）
        self.message_frame = tk.Frame(
            self.frame,
            bg=self.bg_color,
            width=self.width - self.square_size - 4,  # 内缩 2 像素
            height=self.height-4  # 内缩 2 像素
        )
        self.message_frame.pack(side="right", fill="both", expand=True, padx=1, pady=1)

        # 消息内容（粗体，靠左，字体稍微放大）
        self.message_label = tk.Label(
            self.message_frame,
            text="这是一条消息",
            bg=self.bg_color,
            fg=self.text_color,
            font=("Arial", 12, "bold"),
            wraplength=self.width - self.square_size - 20,
            anchor="w",
            justify="left"
        )
        self.message_label.pack(pady=10, padx=5, fill="x", expand=False)

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
            command=self.close_message_box
        )
        self.close_button.place(relx=0.5, rely=0.5, anchor="center")

    def close_message_box(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomMessageBox(root, ratio=3.45)
    root.mainloop()
