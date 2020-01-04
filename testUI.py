import tkinter

win = tkinter.Tk()
win.title("Python-14")
win.geometry("500x500+200+100")


def func():
    message = ""
    if res1.get():
        message += "张三\n"
    if res2.get():
        message += "李四\n"
    if res3.get():
        message += "王五\n"

    # 清除text中所有内容
    text.delete(0.0, tkinter.END)

    # 把message写入text中
    text.insert(tkinter.INSERT, message)


# 判断复选框是否被选定 返回一个bool值
res1 = tkinter.BooleanVar()
# 创建一个复选框
check1 = tkinter.Checkbutton(win, text="张三", variable=res1)
check1.pack()

res2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win, text="李四", variable=res2)
check2.pack()

res3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win, text="王五", variable=res3)
check3.pack()

# 创建一个文本框
text = tkinter.Text(win, width=50, height=20)
text.pack()
# 创建一个按钮
button = tkinter.Button(win, text="submit", width=10, height=5, command=func)
button.pack()
win.mainloop()