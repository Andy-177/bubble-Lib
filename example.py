import tkinter as tk
from bubble import BubbleBox
if __name__ == "__main__":
    root = tk.Tk()

    # 在主线程中创建多个气泡框实例
    BubbleBox(root, title="重要提示", text="这是一条重要的消息，请注意查看！", color="#0088FF", height=50)
    BubbleBox(root, title="重要提示2", text="这是第二条消息，请注意查看！", color="#FF8800", height=100)
    BubbleBox(root, title="重要提示3", text="这是第三条消息，请注意查看！", color="#88FF00", height=150)

    # 将气泡框任务放入队列
    BubbleBox.enqueue_bubble(root, title="hello", text="hello，请注意查看！", color="#8400FF", height=550)
    BubbleBox.enqueue_bubble(root, title="world", text="world，请注意查看！", color="#FF00F2", height=550)

    root.mainloop()