import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+200+50")

# 下拉控件。
# cv = tkinter.StringVar()
# com = ttk.Combobox(win, textvariable=cv)
# com.pack()
# com['value'] = ('黑龙江', '吉林', '辽宁')
# com.current(0)
#
#
# def func(event):
#     print(com.get())
#     print(cv.get())
#
#
# com.bind("<<ComboboxSelected>>", func)
#
# """
# 框架控件：在桌上现实一个矩形区域，多作为一个容器控件
# """
# frm = tkinter.Frame(win)
# frm.pack()
#
# frm_1 = tkinter.Frame(frm)
# tkinter.Label(frm_1, text='左上', bg='pink').pack(side=tkinter.TOP)
# tkinter.Label(frm_1, text='左下', bg='blue').pack(side=tkinter.TOP)
# frm_1.pack(side=tkinter.LEFT)
#
# frm_r = tkinter.Frame(frm)
# tkinter.Label(frm_r, text='右上', bg='green').pack(side=tkinter.TOP)
# tkinter.Label(frm_r, text='右下', bg='red').pack(side=tkinter.TOP)
# frm_r.pack(side=tkinter.RIGHT)
#
# """
# 表格数据
# """
# tree = ttk.Treeview(win)
# tree.pack()
# # 定义列
#
# tree['columns'] = ('姓名', '年龄', '身高', '体重')
# # 设置列，列还不显示
# tree.column('姓名', width=100)
# tree.column('年龄', width=100)
# tree.column('身高', width=100)
# tree.column('体重', width=100)
#
# # 设置表头
# tree.heading('姓名', text='姓名-name')
# tree.heading('年龄', text='年龄-age')
# tree.heading('身高', text='姓名-height')
# tree.heading('体重', text='体重-weight')
#
# tree.insert('', 0, text='1', values=('小郑', '34', '177cm', '70kg'))
# tree.insert('', 1, text='2', values=('小张', '43', '188cm', '90kg'))
#
# """
# 树状数据
# """
# tree1 = ttk.Treeview(win)
# tree1.pack()
#
# treeF1 = tree1.insert('', 0, '中国', text='中国Chi', values=('F1'))
# treeF2 = tree1.insert('', 1, '美国', text='美国USA', values=('F1'))
# treeF3 = tree1.insert('', 2, '英国', text="英国UK", values=('F1'))
#
# treeF1_1 = tree1.insert(treeF1, 0, '黑龙江', text='中国黑龙江', values=('F1_1'))
# treeF1_2 = tree1.insert(treeF1, 1, '吉林', text='中国吉林', values=('F1_2'))
# treeF1_3 = tree1.insert(treeF1, 2, '辽宁', text='中国辽宁', values=('F1_3'))
#
# treeF1_1_1 = tree1.insert(treeF1_1, 0, '哈尔滨', text='黑龙江哈尔滨')
# treeF1_1_2 = tree1.insert(treeF1_1, 1, '五常', text='黑龙江省会')
#
#
# # 绝对布局
# label1 = tkinter.Label(win,text="good",bg='blue').place(x=10,y=10)
#
# label2 = tkinter.Label(win,text="nice",bg='red').place(x=50,y=50)
#
# label3 = tkinter.Label(win,text="cool",bg='green').place(x=100,y=100)


"""
相对布局
"""
# label4= tkinter.Label(win,text="good1",bg='blue').pack(side = tkinter.LEFT)
# label5 = tkinter.Label(win,text="nice1",bg='red').pack(side =tkinter.TOP)
# label6 = tkinter.Label(win,text="cool1",bg='green').pack()


label7 = tkinter.Label(win, text="good3", bg='blue').grid(row=0, column=0)
label8 = tkinter.Label(win, text="nice3", bg='red').grid(row=0, column=1)
label9 = tkinter.Label(win, text="cool3", bg='green').grid(row=0, column=2)
label20 = tkinter.Label(win, text="handsome", bg='yellow').grid(row=0, column=3)
frm = tkinter.Frame(win).grid(row=0, column=4)
frm_1 = tkinter.Frame(frm)
labe21 = tkinter.Label(frm_1, text="good4", bg='blue').grid(row=0, column=0)
labe22 = tkinter.Label(frm_1, text="nice4", bg='red').grid(row=1, column=0)
labe23 = tkinter.Label(frm_1, text="cool4", bg='green').grid(row=2, column=0)
frm_1.grid(row=0, column=4)

"""
鼠标点击事件
# <Button-1>  鼠标左键
# <Button-2>  鼠标滚轮
# <Button-1>  鼠标右键
# <Double-Button-1>  鼠标双击左键
# <Triple-Button-1>  鼠标三击左键
"""


def func(event):
    print(event.x, event.y)


button1 = tkinter.Button(win, text="leftmouse button")
button1.bind('<Button-1>', func)
button1.grid(row=0, column=5)

"""
 # <B1-Motion>  左键移动
 # <B2-Motion>  中键移动
 # <B3-Motion>  右键移动
"""
label = tkinter.Label(win, text="************")
label.grid(row=2, column=3)
label.bind('<B1-Motion>', func)

"""
<ButtonRelease-1> 释放鼠标左键
<ButtonRelease-2> 释放鼠标中键
<ButtonRelease-3> 释放鼠标右键
"""
label2 = tkinter.Label(win, text="************")
label2.grid(row=3, column=3)
label2.bind('<ButtonRelease-1>', func)

"""
进入离开事件
# <Enter>  当鼠标进入控件时触发事件
# <Leave>  当鼠标离开控件时触发事件
"""

label4 = tkinter.Label(win, text="************")
label4.grid(row=4, column=3)
label4.bind('<Enter>', func)
label4.bind('<Leave>', func)

"""所有案件事件
 <Key>  响应所有的按键（要有焦点）

"""

label3 = tkinter.Label(win, text="333************")
label3.focus_set()
label3.grid(row=5, column=3)


def func2(event):
    print('event char', event.char)
    print('event keycode', event.keycode)

label3.bind('<Key>', func2)


"""
特殊按键
# <Shift_L>  只响应左侧的shift键
 8 # <Shift_R>
 9 # <F5>
10 # <Return>  也就是回车键
11 # <BackSpace>  返回,也就是退格键
"""

label4 = tkinter.Label(win, text="444************")
label4.focus_set()
label4.grid(row=6, column=3)
label4.bind('<Shift_L>', func2)


"""指定按键"""
label4 = tkinter.Label(win, text="555************")
label4.focus_set()
label4.grid(row=7, column=3)
# win.bind('a', func2)
win.bind("<Control-Alt-a>", func) # 注意前面改成了win，只需要写出按键名即可

win.mainloop()
