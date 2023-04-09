# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog
import pikepdf
import os


class Pdf_Unlock:
    def __init__(self):
        self.gui = tk.Tk()  # 实例化tkinter
        self.gui.title("PDF编辑密码解除 by@TouchingTune")  # 定义主窗口名
        self.gui.geometry("580x80+650+400")  # 定义窗口大小及出现位置
        self.result_list = []
        self.pdf_origin_url = tk.StringVar()  # 创建一个tkinter的字符串变量用于保存和显示PDF文件或所在文件夹路径
        self.processing_type = tk.IntVar()  # 定义一个tkinter的整型变量用于区别处理类型（单个文件或批量处理）
        self.processing_type.set(1)  # 设置默认处理类型为单个文件处理模式
        self.label_pdf_origin_url = tk.Label(self.gui, text="请选择一个PDF文件:")  # PDF文件位置输入框前的提示
        self.entry_pdf_origin_url = tk.Entry(self.gui, width=50)  # 创建一个输入框用于输入PDF文件路径
        self.button_pdf_file_browse = tk.Button(self.gui, text="浏览", command=self.get_pdf_origin_url,
                                                width=8)  # 创建一个“浏览”按钮，点击后自动弹出选择PDF文件的图形界面并在确定后返回选择的路径
        self.button_confirm = tk.Button(self.gui, text="确定", command=self.confirm,
                                        width=8)  # 创建一个“确定”按钮，点击后自动验证输入是否合法并根据输入内容运行处理脚本
        self.button_cancel = tk.Button(self.gui, text="取消", command=self.cancel,
                                       width=8)  # 创建一个“取消”按钮，点击后主动退出程序

    def display(self):
        self.label_pdf_origin_url.grid(row=1, column=0, padx=5, pady=5, columnspan=2,
                                       sticky=tk.W)  # 在第1行，第0列显示"PDF文件路径:"提示
        self.entry_pdf_origin_url.grid(row=1, column=2, padx=0, pady=5, columnspan=6,
                                       sticky=tk.W)  # 在第1行，第2列显示PDF文件路径输入框
        self.button_pdf_file_browse.grid(row=1, column=8, padx=15, pady=5, columnspan=1,
                                         sticky=tk.E)  # 在第1行，第8列显示浏览按钮
        self.button_confirm.grid(row=3, column=7, padx=15, pady=5, columnspan=1, sticky=tk.E)  # 在第3行，第7列显示“确定”按钮
        self.button_cancel.grid(row=3, column=8, padx=15, pady=5, columnspan=1, sticky=tk.E)  # 在第3行，第8列显示“取消”按钮
        self.gui.mainloop()  # 根据以上配置对所有元素进行显示

    def get_pdf_origin_url(self):
        self.pdf_origin_url = filedialog.askopenfilename(defaultextension='.pdf')  # 获取PDF文件路径
        if self.pdf_origin_url:  # 如果输入的路径存在
            self.entry_pdf_origin_url.delete(0, tk.END)  # 清空输入框中设置的默认显示内容
            self.entry_pdf_origin_url.insert(0,
                                             self.pdf_origin_url)  # 弹出选择文件的图形窗口并将获取到的值返回给entry_pdf_origin_url显示到输入框

    def confirm(self):
        if os.path.exists(str(self.pdf_origin_url)):  # 如果该文件存在
            pdf = pikepdf.open(str(self.pdf_origin_url))  # 使用pikepdf打开并解密PDF文件
            os.chdir(os.path.dirname(str(self.pdf_origin_url)))  # 切换OS工作目录到PDF文件所在目录
            file_name, file_ext = os.path.splitext(str(os.path.basename(str(self.pdf_origin_url))))  # 读取文件名
            pdf.save(file_name + '[已解密]' + file_ext)  # 设置保存的文件名为原文件名+[已解密]并保存
            warm_Window = tk.Toplevel(self.gui)  # 创建一个顶层窗口
            warm_Window.title("提示")  # 修改程序窗口的名字
            warm_Window.geometry("300x50+800+450")  # 定义窗口大小及出现位置
            warm = tk.Label(warm_Window, text="解密成功！", padx=40, pady=10)  # 设置弹窗文本与布局
            warm.pack()  # 显示弹窗
        else:
            warm_Window = tk.Toplevel(self.gui)  # 创建一个顶层窗口
            warm_Window.title("警告")  # 修改程序窗口的名字
            warm_Window.geometry("300x50+800+450")  # 定义窗口大小及出现位置
            warm = tk.Label(warm_Window, text="请输入正确的PDF文件路径！", padx=40, pady=10)  # 设置弹窗文本与布局
            warm.pack()  # 显示弹窗

    @staticmethod
    def cancel():  # 如果按下取消按键
        os._exit(0)  # 主动退出程序


if __name__ == "__main__":
    unlock_gui = Pdf_Unlock()
    unlock_gui.display()