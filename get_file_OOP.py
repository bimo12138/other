from tkinter import Tk, Frame, Button, filedialog, Label, Entry, messagebox
import os
import subprocess

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createViewer()

    def createViewer(self):
        self.button = Button(self, text="选择文件", command=self.choose_file)
        self.button.grid(row=0, column=0)
        self.entry = Entry(self, text="请输入需要解压的文件地址或者点击左侧按钮快速选择")
        self.entry.grid(row=0, column=1)
        self.submit = Button(self, text="提交", command=self.run_refuse)
        self.submit.grid(row=1, column=0)

    def run_refuse(self):
        if self.ext.lower() == "zip":
            self.unzip()
        elif self.ext.lower() == "rar":
            self.unrar()
        messagebox.showinfo("解压成功", "文件解压成功，目录为: {}".format(self.path))
        
        # TODO 怎么处理打开文件管理器。麻烦哎 QAQ os 
        # os.system("explorer.exe %s" % self.path)
        # 问题总结: python 中获取的路径为 / 作为分割符, 但是 windows 中使用 \\ 所以需要替换
        # 并且使用 subprocess 可以隐藏 cmd 的窗格
        subprocess.Popen(r"explorer.exe {}".format(self.path.replace("/", "\\")), shell=True)
        
    def choose_file(self):
        accept_type = ["rar", "zip"]
        file_path = filedialog.askopenfilename(filetypes=[("RAR 压缩文件", "rar"), ("ZIP 压缩文件", "zip")])
        name, ext = file_path.split(".")
        if ext not in accept_type:
            raise TypeError("输入的文件格式错误, 请重新输入！")
        self.file = file_path
        self.ext = ext
        self.path = name
        self.change_entry(file_path)
        
    def unzip(self):
        try:
            from zipfile import ZipFile
        except:
            raise ImportError("没有zipFile库")
        
        file = ZipFile(r"{}".format(self.file))
        
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        for file_name in file.namelist():
            filename = file_name.encode("cp437").decode("gbk")
            file.extract(file_name, path=self.path)
            os.chdir(self.path)
            os.rename(file_name, filename)
        
    def unrar(self):
        try:
            import rarfile
        except:
            raise ImportError("没有rarfile库")
        file = rarfile.RarFile(r"{}".format(self.file))
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        try:
            file.extract(self.path)
        except:
            raise OSError("请检查UNRAR.exe是否存在！")

    def change_entry(self, message):
        self.entry.select_clear()
        self.entry.insert(0, message)

root = Tk()
app = Application(master=root)
app.mainloop()
