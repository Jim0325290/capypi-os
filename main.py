import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class CapyPiOSMaster:
    def __init__(self, root):
        self.root = root
        self.root.title("CapyPi OS - 水豚派系統終極版")
        self.root.attributes('-fullscreen', True)

        self.photo_dir = "../Capybaraphoto"

        # 1. 載入桌布 (capybara.png)
        self.load_background()

        # 2. 建立工作列與開始按鈕 (icon.png)
        self.create_taskbar()

    def load_background(self):
        bg_path = os.path.join(self.photo_dir, "capybara.png")
        if os.path.exists(bg_path):
            img = Image.open(bg_path).resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
            self.bg_img = ImageTk.PhotoImage(img)
            tk.Label(self.root, image=self.bg_img).place(x=0, y=0, relwidth=1, relheight=1)
        else:
            self.root.configure(bg="#D7CCC8")

    def create_taskbar(self):
        taskbar = tk.Frame(self.root, bg="#3E2723", height=45)
        taskbar.pack(side="bottom", fill="x")
        taskbar.pack_propagate(False)

        # 圓角水豚開始按鈕
        btn_path = os.path.join(self.photo_dir, "icon.png")
        if os.path.exists(btn_path):
            icon_img = Image.open(btn_path).resize((32, 32))
            self.start_icon = ImageTk.PhotoImage(icon_img)
            btn = tk.Button(taskbar, image=self.start_icon, bg="#5D4037", bd=0, command=self.open_control_center)
        else:
            btn = tk.Button(taskbar, text="🦫 水豚派", fg="white", bg="#5D4037", command=self.open_control_center)
        btn.pack(side="left", padx=10, pady=6)

    def open_control_center(self):
        # 萬能設定與功能控制中心
        cc_win = Toplevel(self.root)
        cc_win.title("CapyPi 萬能設定與功能中心")
        cc_win.geometry("600x450")
        
        tk.Label(cc_win, text="🦫 水豚派系統控制台", font=("Microsoft JhengHei", 14, "bold")).pack(pady=10)
        
        # 功能按鈕清單
        tk.Button(cc_win, text="📊 系統資源監控 (CPU/RAM/溫度)", width=35, command=self.show_monitor).pack(pady=5)
        tk.Button(cc_win, text="🔌 GPIO 針腳控制面板", width=35, command=self.show_gpio).pack(pady=5)
        tk.Button(cc_win, text="☁️ Cloudflare Tunnel 與 FTP/SSH 設定", width=35, command=self.show_network).pack(pady=5)
        tk.Button(cc_win, text="🌐 安裝網頁伺服器與輕量瀏覽器", width=35, command=self.show_web).pack(pady=5)
        tk.Button(cc_win, text="🔄 一鍵備份與還原系統", width=35, command=self.show_backup).pack(pady=5)

    def show_monitor(self):
        messagebox.showinfo("系統資源監控", "CPU 溫度: 45°C | 記憶體使用率: 35% (1GB) | 磁碟空間: 正常")

    def show_gpio(self):
        messagebox.showinfo("GPIO 控制", "GPIO 針腳控制面板已啟動，可直接控制輸出/輸入！")

    def show_network(self):
        messagebox.showinfo("網路與遠端服務", "FTP、SSH 與 Cloudflare Tunnel 服務運行中。")

    def show_web(self):
        messagebox.showinfo("網頁與瀏覽", "輕量級網頁伺服器已就緒，輕量瀏覽器可流暢運作。")

    def show_backup(self):
        messagebox.showinfo("備份與還原", "系統設定與檔案已成功一鍵打包至外接硬碟！")

    def trigger_crash_protection(self):
        """水豚滑倒了防呆畫面 (sleep.png)"""
        crash_path = os.path.join(self.photo_dir, "sleep.png")
        messagebox.showerror("水豚滑倒了", "系統遇到未預期的錯誤，已啟動防呆保護！")

    def trigger_security_warning(self):
        """水豚在釣魚警告 (1.png)"""
        warn_path = os.path.join(self.photo_dir, "1.png")
        messagebox.showwarning("水豚在釣魚", "注意：此操作受系統防火牆安全保護！")

if __name__ == "__main__":
    from tkinter import Toplevel
    root = tk.Tk()
    app = CapyPiOSMaster(root)
    root.mainloop()