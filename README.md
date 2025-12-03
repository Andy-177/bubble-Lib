# bubble-Lib
A Python library that can pop up custom bubble notifications
# 使用教程（User Guide）
## 示例（Example）
### 无队列，同时弹出（No queue, pop up simultaneously）
```
BubbleBox(window, title="标题（title）", text="消息内容（Message content）", color="#0088FF", height=50)
```
### 有队列，按顺序弹出（There is a queue, popping out in order）
```
BubbleBox.enqueue_bubble(window, title="标题（title）", text="消息内容（Message content）", color="#0088FF", height=50)
```
## 提示（Tips）
1.加入队列使用在BubbleBox后面添加.enqueue_bubble，以将气泡窗添加到队列
- To join the queue, use .enqueue_bubble after BubbleBox to add a bubble window to the queue.

2.第一个属性值是窗口实例的名称，比如创建了实例`root = tk.TK`，那么第一个属性要和实例名称重合，比如在这个例子里就是`BubbleBox.enqueue_bubble(root, title="标题（title）", text="消息内容（Message content）", `color="#0088FF", height=50)`
- The first attribute value is the name of the window instance. For example, if you create an instance with `root = tk.TK`, then the first attribute should match the instance name. In this example, it would be `BubbleBox.enqueue_bubble(root, title="Title (title)", text="Message content", color="#0088FF", height=50)`
