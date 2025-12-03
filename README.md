# bubble-Lib
A Python library that can pop up custom bubble notifications
# 注意(Notice)
popup.py是bubble.py的实验版，不稳定

popup.py is an experimental version of bubble.py and is unstable

带有_lib的是可以引用的库，使用`from bubble_lib import BubbleBox`引用bubble

Libraries with _lib can be imported. Use `from bubble_lib import BubbleBox` to import bubble.
# 功能与局限(Functions and Bugs)
## bubble
### 功能(Functions)
- [x] 支持弹出气泡框(Support pop-up bubbles)
- [ ] 按顺序弹出气泡框(Pop up the bubble frames in order)
### 局限性(Bugs)
- [x] 气泡框消失气泡窗依赖的主窗口也会随之消失(When the bubble frame disappears, the main window that the bubble window depends on will also disappear.)
## popup
### 功能(Functions)
- [x] 支持弹出气泡框(Support pop-up bubbles)
- [x] 按顺序弹出气泡框(Pop up the bubble frames in order)
### 局限性(Bugs)
- [x] 使用按顺序弹出气泡框时会让气泡窗依赖的主窗口隐藏，并且气泡窗消失进程依然持续(Using sequential pop-up bubbles causes the main window that the bubbles rely on to be hidden, and the bubble window's disappearance process continues.)
