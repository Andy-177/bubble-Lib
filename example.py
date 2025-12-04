from bubble import BubbleBox
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    def show_custom_bubble():
        BubbleBox.enqueue_bubble(
            root,
            title="自定义气泡框",
            text="这是一个自定义的气泡框，使用了不同的字体和颜色。",
            color="#FF5733",  # 橙色背景
            height=400,
            title_font="SimHei",  # 使用黑体字体
            title_size=16,
            title_style="italic",  # 标题斜体
            text_font="Courier New",  # 使用等宽字体
            text_size=14,
            text_style="normal",
        )

    # 将所有气泡框任务放入队列，而不是直接创建实例
    BubbleBox(root, title="重要提示", text="这是一条重要的消息，请注意查看！", color="#0088FF", height=50)
    BubbleBox(root, title="重要提示2", text="这是第二条消息，请注意查看！", color="#FF8800", height=100)
    BubbleBox(root, title="重要提示3", text="这是第三条消息，请注意查看！", color="#88FF00", height=150)
    show_custom_bubble()

    # 继续将气泡框任务放入队列
    BubbleBox.enqueue_bubble(root, title="hello", text="hello，请注意查看！", color="#8400FF", height=550)
    BubbleBox.enqueue_bubble(root, title="world", text="world，请注意查看！", color="#FF00F2", height=550)

    root.mainloop()

