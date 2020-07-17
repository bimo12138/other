"""
@author: bimo
@date:   2019.11.11 22:18:15
@ide:    IDLE
@e-mail: 1371639183@qq.com
"""
import winreg
from tkinter import Tk, Frame, Label, Button, filedialog, PhotoImage, Canvas
import time
try:
    from PIL import Image, ImageTk
except:
    import os
    os.system("pip install pillow")
    
def get_desktop():
    
    temp = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
               r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
    return winreg.QueryValueEx(temp, "Desktop")[0]

class Application(Frame):

    def __init__(self, master=None):
        self.desktop_path = get_desktop()
        Frame.__init__(self, master)
        self.pack()
        self.createViewer()

    def createViewer(self):
        self.title = Label(self, text="图片基础处理工具")
        self.title.grid(row=0, column=0, columnspan=3)
        self.button = Button(self, text="选择图片", command=self.choose_image)
        self.button.grid(row=1, column=1)
        self.images = Label(self)
        self.images.grid(row=1, column=2)
        self.one_button = Button(self, text="1 寸照片", command=self.change_to_one)
        self.one_button.grid(row=2, column=0)
        self.two_button = Button(self, text="2 寸图片", command=self.change_to_two)
        self.two_button.grid(row=2, column=1)
    def choose_image(self):
        accept_type = [("JPG 图片", "jpg"), ("GIF 图片", "gif"), ("PNG 图片", "png")]
        file_path = filedialog.askopenfilename(filetypes=accept_type)
        self.path, self.ext = file_path.split(".")
        self.image_path = file_path
        img = Image.open(file_path.replace("/", "\\"))
        img = self.adapt_size(img)
        global file
        file = ImageTk.PhotoImage(img)
        self.images["image"] = file
        self.images.grid()

    def adapt_size(self, img):
        x, y = img.size
        if x > y:
            percentage = x / 400
            return img.resize((int(x / percentage), int(y / percentage)))
        else:
            percentage = y / 400
            return img.resize((int(x / percentage), int(y / percentage)))
        
    def change_to_one(self):
        img = Image.open(self.image_path)
        img = img.resize((295, 413))
        path = self.desktop_path + "\\" + str(int(time.time())) + ".jpg"
        img.save(path)

    def change_to_two(self):
        img = Image.open(self.image_path)
        img = img.resize((413, 626))
        path = self.desktop_path + "\\" + str(int(time.time())) + ".jpg"
        img.save(path)
        
root = Tk()
app = Application(master=root)
app.mainloop()
