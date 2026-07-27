import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class CapyPiDesktop:
    def __init__(self, root):
        self.root = root
        self.root.title("CapyPi OS (水豚派系統)")
        self.root.attributes('-fullscreen', True) # 樹莓派全螢幕執行

        # 指定圖片區路徑 (對應你的 Capybaraphoto)
        self.photo_dir = "../Capybaraphoto"

        # 1. 載入桌面背景 (capybara.png)
        self.load_background()

        # 2. 建立置底工作列與開始按鈕
        self.create_taskbar()

    def load_background(self):
        bg_path = os.path.join(self.photo_dir, "capybara.png")
        if os.path.exists(bg_path):
            image = Image.open(bg_path)
            image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
            self.bg_image = ImageTk.PhotoImage(image)
            
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        else:
            self.root.configure(bg="#D7CCC8") # 備用療癒淺棕色

    def create_taskbar(self):
        # 置底工作列
        self.taskbar = tk.Frame(self.root, bg="#3E2723", height=45)
        self.taskbar.pack(side="bottom", fill="x")
        self.taskbar.pack_propagate(False)

        # 圓角水豚開始按鈕 (icon.png)
        btn_path = os.path.join(self.photo_dir, "icon.png")
        if os.path.exists(btn_path):
            img_icon = Image.open(btn_path).resize((32, 32))
            self.start_icon = ImageTk.PhotoImage(img_icon)
            self.start_btn = tk.Button(self.taskbar, image=self.start_icon, bg="#5D4037", bd=0, command=self.open_start_menu)
        else:
            self.start_btn = tk.Button(self.taskbar, text="🦫 水豚", fg="white", bg="#5D4037", font=("Microsoft JhengHei", 10, "bold"), command=self.open_start_menu)
        
        self.start_btn.pack(side="left", padx=10, pady=6)

    def open_start_menu(self):
        print("【系統】開啟水豚派開始選單...")

    def trigger_warning(self):
        """當系統觸發安全警告時呼叫『水豚在釣魚』(1.png)"""
        warn_path = os.path.join(self.photo_dir, "1.png")
        messagebox.showwarning("水豚在釣魚", "注意：此動作可能會修改受保護的系統檔案！")

    def trigger_crash(self):
        """當系統嚴重錯誤時呼叫『水豚滑倒了』(sleep.png)"""
        crash_path = os.path.join(self.photo_dir, "sleep.png")
        messagebox.showerror("水豚滑倒了", "系統遇到未預期的錯誤，請重新啟動！")

if __name__ == "__main__":
    root = tk.Tk()
    app = CapyPiDesktop(root)
    root.mainloop()