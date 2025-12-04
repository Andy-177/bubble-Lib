import tkinter as tk
import queue


class BubbleBox:
    task_queue = queue.Queue()  # 线程安全的任务队列
    current_instance = None  # 当前正在显示的气泡框实例

    def __init__(self, root, title="消息提示", text="这是一条消息", color="#800080", height=50, title_font="Arial", title_size=14, title_style="bold", text_font="Arial", text_size=12, text_style="normal"):
        self.root_window = root  # 保存主窗口的引用
        self.root = tk.Toplevel(root)  # 使用 Toplevel 创建独立窗口
        self.title = title
        self.text = text
        self.theme_color = color
        self.height_offset = height  # 新增参数，控制垂直偏移量
        self.ratio = 3.45
        self.square_size = 90
        self.width = self.square_size + (self.square_size * self.ratio)
        self.height = self.square_size

        self.title_font = title_font
        self.title_size = title_size
        self.title_style = title_style
        self.text_font = text_font
        self.text_size = text_size
        self.text_style = text_style

        # 设置窗口属性
        self.root.geometry(f"{int(self.width)}x{int(self.height)}")
        self.root.resizable(False, False)
        self.root.overrideredirect(True)
        self.root.attributes("-alpha", 1.0)
        self.root.attributes("-topmost", True)

        # 设置窗口初始位置（在屏幕右侧外）
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.start_x = screen_width
        self.target_x = screen_width - self.width
        self.y = screen_height - self.height - self.height_offset  # 使用 height 参数计算垂直位置
        self.root.geometry(f"+{int(self.start_x)}+{int(self.y)}")

        # 创建 GUI 元素
        self.canvas = tk.Canvas(
            self.root,
            width=self.width,
            height=self.height,
            bd=0,
            highlightthickness=0,
            bg=self.theme_color
        )
        self.canvas.pack()

        self.frame = tk.Frame(self.canvas, bg=self.theme_color, bd=0)
        self.frame.place(x=0, y=0, width=self.width - 1, height=self.height - 0.5)

        self.square_frame = tk.Frame(
            self.frame,
            bg=self.theme_color,
            width=self.square_size,
            height=self.height - 2
        )
        self.square_frame.pack(side="left", fill="y")

        self.message_frame = tk.Frame(
            self.frame,
            bg="white",
            width=self.width - self.square_size - 4,
            height=self.height - 4
        )
        self.message_frame.pack(side="right", fill="both", expand=True, padx=1, pady=1)

        self.title_label = tk.Label(
            self.message_frame,
            text=self.title,
            bg="white",
            fg=self.theme_color,
            font=(self.title_font, self.title_size, self.title_style),
            anchor="w",
            justify="left"
        )
        self.title_label.pack(pady=(10, 5), padx=5, fill="x", expand=False)

        self.message_label = tk.Label(
            self.message_frame,
            text=self.text,
            bg="white",
            fg=self.theme_color,
            font=(self.text_font, self.text_size, self.text_style),
            wraplength=self.width - self.square_size - 20,
            anchor="w",
            justify="left"
        )
        self.message_label.pack(pady=(0, 10), padx=5, fill="x", expand=False)

        self.close_button_frame = tk.Frame(
            self.message_frame,
            bg="white",
            width=20,
            height=20
        )
        self.close_button_frame.place(x=self.width - self.square_size - 26, y=4)
        self.close_button_frame.pack_propagate(False)

        self.close_button = tk.Button(
            self.close_button_frame,
            text="✕",
            bg=self.theme_color,
            fg="white",
            font=("Arial", 12, "bold"),
            bd=0,
            command=self.fade_out
        )
        self.close_button.place(relx=0.5, rely=0.5, anchor="center")

        # 启动弹出动画
        self.start_animation()

    def start_animation(self):
        """从右到左的弹出动画"""
        if self.root and self.root.winfo_exists():
            if self.start_x > self.target_x:
                self.start_x -= 5
                self.root.geometry(f"+{int(self.start_x)}+{int(self.y)}")
                self.root.after(1, self.start_animation)
            else:
                self.root.geometry(f"+{int(self.target_x)}+{int(self.y)}")
                self.root.after(4000, self.fade_out)  # 4秒后自动消失

    def fade_out(self):
        """逐渐透明的消失动画"""
        if self.root and self.root.winfo_exists():
            current_alpha = self.root.attributes("-alpha")
            if current_alpha > 0:
                new_alpha = current_alpha - 0.05
                self.root.attributes("-alpha", new_alpha)
                self.root.after(20, self.fade_out)
            else:
                self._safe_destroy()

    def _safe_destroy(self):
        """安全销毁窗口及其子组件"""
        if self.root and self.root.winfo_exists():
            try:
                # 安全销毁子组件
                for widget in self.root.winfo_children():
                    widget.destroy()
                self.root.destroy()
            except tk.TclError as e:
                print(f"Error during safe destroy: {e}")
            finally:
                if self.root_window:  # 如果主窗口存在
                    self.root_window.lift()  # 将主窗口置于最上方
                self._start_next_instance()

    @classmethod
    def _start_next_instance(cls):
        """销毁当前实例后，启动下一个实例（如果存在）"""
        if cls.current_instance and cls.current_instance.root and cls.current_instance.root.winfo_exists():
            cls.current_instance.root.after(100, cls._start_next_instance)  # 稍微延迟启动下一个实例
        elif not cls.task_queue.empty():
            root, title, text, color, height, title_font, title_size, title_style, text_font, text_size, text_style = cls.task_queue.get()  # 获取下一个任务的参数
            cls.current_instance = BubbleBox(root, title, text, color, height, title_font, title_size, title_style, text_font, text_size, text_style)  # 实例化并显示下一个气泡框
        else:
            cls.current_instance = None  # 没有更多实例时，清除当前实例

    @classmethod
    def enqueue_bubble(cls, root, title, text, color, height=50, title_font="Arial", title_size=14, title_style="bold", text_font="Arial", text_size=12, text_style="normal"):
        """将创建气泡框的任务参数放入队列中"""
        cls.task_queue.put((root, title, text, color, height, title_font, title_size, title_style, text_font, text_size, text_style))  # 存储气泡框的参数
        if cls.current_instance is None:  # 如果当前没有正在显示的实例，立即启动第一个任务
            cls._start_next_instance()
