# 配置下载的界面和启动下载的地方，同时可以保存数据
import tkinter
import StockConfig
import stock as stk


def download():
    code_number = e1.get()
    if len(code_number) == 0 or len(code_number) != 6 or not (code_number.isdigit()):
        print('请输入股票代码')
        text.delete(0.0, tkinter.END)
        text.insert(tkinter.INSERT, "请输入股票代码"+'\n')
    else:
        # 还要增加很多判断，如是不是股票代码，股票数据下载的进度条,然后即使六位数字的字符是不是股票代码了
        text.insert(tkinter.INSERT, "开始下载"+'\n')
        print(code_number)
        list = get_filters()
        print('列表数据',list)
        stk.get_filter_list(list)
        text.insert(tkinter.INSERT, "下载中"+'\n')
        time_list = stk.get_time_param(code_number)
        stk.get_html(time_list)
        text.insert(tkinter.INSERT, "下载完成"+'\n')



def get_filters():
    dict = list()
    if res1.get():
        dict.append(check1.configure('text')[-1])
    if res2.get():
        dict.append(check2.configure('text')[-1])
    if res3.get():
        dict.append(check3.configure('text')[-1])
    if res4.get():
        dict.append(check4.configure('text')[-1])
    if res5.get():
        dict.append(check5.configure('text')[-1])
    if res6.get():
        dict.append(check6.configure('text')[-1])
    if res7.get():
        dict.append(check7.configure('text')[-1])
    if res8.get():
        dict.append(check8.configure('text')[-1])
    if res9.get():
        dict.append(check9.configure('text')[-1])
    if res10.get():
        dict.append(check10.configure('text')[-1])
    if res11.get():
        dict.append(check11.configure('text')[-1])
    if res12.get():
        dict.append(check12.configure('text')[-1])
    return dict


win = tkinter.Tk()
win.title("股票数据下载")
win.geometry('500x500+200+100')
lable = tkinter.Label(win, text='输入股票代码')
lable.pack(anchor='w')
e1 = tkinter.Variable()
entry = tkinter.Entry(win, textvariable=e1)
entry.pack(anchor='w')

# 复选框，选择需要下载的数据，后面可以用循环的形式生成的。
res1 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win, text="收盘价", variable=res1)
check1.pack()

res2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win, text="最高价", variable=res2)
check2.pack()

res3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win, text="最低价", variable=res3)
check3.pack()

res4 = tkinter.BooleanVar()
check4 = tkinter.Checkbutton(win, text="开盘价", variable=res4)
check4.pack()

res5 = tkinter.BooleanVar()
check5 = tkinter.Checkbutton(win, text="前收盘", variable=res5)
check5.pack()

res6 = tkinter.BooleanVar()
check6 = tkinter.Checkbutton(win, text="涨跌额", variable=res6)
check6.pack()

res7 = tkinter.BooleanVar()
check7 = tkinter.Checkbutton(win, text="涨跌幅", variable=res7)
check7.pack()

res8 = tkinter.BooleanVar()
check8 = tkinter.Checkbutton(win, text="换手率", variable=res8)
check8.pack()

res9 = tkinter.BooleanVar()
check9 = tkinter.Checkbutton(win, text="成交量", variable=res9)
check9.pack()

res10 = tkinter.BooleanVar()
check10 = tkinter.Checkbutton(win, text="成交金额", variable=res10)
check10.pack()

res11 = tkinter.BooleanVar()
check11 = tkinter.Checkbutton(win, text="总市值", variable=res11)
check11.pack()

res12 = tkinter.BooleanVar()
check12 = tkinter.Checkbutton(win, text="流通市值", variable=res12)
check12.pack()

button_down = tkinter.Button(win, text='下载', fg='green', bg='gray', command=download)
button_down.pack()

text = tkinter.Text(win, width=500, height=20)
text.pack()

win.mainloop()

