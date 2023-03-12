import tkinter as tk
import datasource as ds
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import base64
from io import BytesIO
from bg_jpg import *


class Window(tk.Tk):
    def __init__(self, town):
        super().__init__()
        # 建立背景
        bgImage = Image.open(BytesIO(base64.b64decode(img)))
        self.tkImage = ImageTk.PhotoImage(bgImage)
        mainCanvas = tk.Canvas(self)
        mainCanvas.create_image(-100, -50, anchor=tk.NW, image=self.tkImage)
        mainCanvas.pack(fill=tk.BOTH, expand=True)

        # 建立標題
        title_label = tk.Label(mainCanvas, text="臺中市YouBike2.0租借站位置查詢", fg="#191970", font=(
            "標楷體", 24)).pack(padx=30, pady=30)

        # 建立按鈕
        buttoms_frame = tk.Frame(mainCanvas, cursor="hand2")
        buttoms_frame.pack(padx=50, pady=(0, 30))

        grid_row_nums = 5
        for index, name in enumerate(town):
            btn = tk.Button(buttoms_frame, text=f"{name}", bg="#b0c4de", fg="#0000cd", font=(
                "標楷體", 16), width=8, height=2, padx=20, pady=5)
            btn.grid(row=index // grid_row_nums, column=index % grid_row_nums)
            btn.bind("<Button-1>", self.button_click)

    # 顯示資料
    def button_click(self, event):
        btn_text = event.widget["text"]
        print(f"地區:{btn_text}")

        try:
            town_forcase = ds.get_forcase_data(btn_text)
            if hasattr(self, "displayFrame"):  # 框框標題
                self.displayFrame.destroy()
            self.displayFrame = DisplayFrame(
                self, data=town_forcase, text=btn_text, borderwidth=2, relief=tk.GROOVE)
            self.displayFrame.pack(fill=tk.BOTH, padx=50, pady=(10, 30))

        except Exception as e:
            messagebox.showerror(
                title='Error!!', message='查無此資料')
            if hasattr(self, "displayFrame"):
                self.displayFrame.destroy()
                return

    # 建立資料表格


class DisplayFrame(ttk.LabelFrame):
    def __init__(self, parent, data=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.city_data = data
        total_rows = len(self.city_data)
        centterFrame = CustomFrame(self, data=self.city_data)
        centterFrame.pack(side=tk.LEFT, padx=15)

    # 建立資料內容


class CustomFrame(tk.Frame):
    def __init__(self, parent, data=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.list_data = data
        style = ttk.Style()
        style.configure("Treeview", background="#ffe4e1",
                        foreground="#4682b4", fieldbackground="#afeeee",rowheight=25)
        style.map("Treeview", background=[("selected", "#ffa500")])
        # style.theme_use("classic")
        self.tree = ttk.Treeview(
            self, columns=["#1", "#2", "#3", "#4"], show="headings", height=15)
        self.tree.pack(side=tk.LEFT)
        srcollbar = tk.Scrollbar(self)
        srcollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.config(yscrollcommand=srcollbar.set)
        srcollbar.config(command=self.tree.yview)

        self.tree.heading("#1", text="區域")
        self.tree.heading("#2", text="站點名稱")
        self.tree.heading("#3", text="詳細位置")
        self.tree.heading("#4", text="車位總數")
        self.tree.column("#1", width=60, anchor="center")
        self.tree.column("#2", width=250, anchor="w")
        self.tree.column("#3", width=250, anchor="w")
        self.tree.column("#4", width=80, anchor="center")

        for item in self.list_data:
            self.tree.insert("", tk.END, values=item)


def main():
    window = Window(ds.town_names)
    window.title("臺中市YouBike2.0租借站位置查詢")
    window.resizable(0, 0)
    window.mainloop()


if __name__ == "__main__":
    main()
