import tkinter as tk
from tkinter import font, ttk
from tkinter.messagebox import askyesno
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except ImportError:
    print("Error: windll not imported. Text may be blurred")
    pass

from app.util.controller import JsonController, Controller
from app.gui.windows.landing.base_link_update import BaseLinkUpdate

BUTTON_WIDTH = 25
BUTTON_HEIGHT = 2
BUTTON_PADDING = 15
colors = JsonController.get_config_data("colors")
C1 = colors["c1"]
C2 = colors["c2"]
C3 = colors["c3"]
C4 = colors["c4"]

class Landing(tk.Frame):
    def __init__(self, container, main_window):
        super().__init__(container)
        BUTTON_FONT = font.Font(family="Helvetica", size=20, weight="bold")
        FONT_XL = font.Font(family="Helvetica", size=30, weight="bold")
        FONT_MD = font.Font(family="Helvetica", size=16, weight="bold")
        self.config(bg=C1)
        #GROUPER
        container = tk.Frame(self, bg=C2, border=3, relief="groove")
        container.pack( expand=True, padx=40, pady=40, fill='both')
        self.body = tk.Frame(container, bg=C2)
        self.body.pack( expand=True)
        
        #BODY
        new_post_btn = tk.Button(
            self.body, 
            text="New Post", 
            command=lambda: main_window.load_content("NewPost"),
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            font= FONT_MD,
            bg="white"
        )
        new_post_btn.pack(padx=BUTTON_PADDING, pady=BUTTON_PADDING)

        configure_post_btn = tk.Button(
            self.body,
            text="Configure Website",
            command=lambda: main_window.load_content("ConfigureWebsite"),
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            font=FONT_MD,
            bg="white"
        )
        configure_post_btn.pack(padx=BUTTON_PADDING, pady=BUTTON_PADDING)

        edit_post_btn = tk.Button(
            self.body,
            text="Edit Posts",
            command=lambda: main_window.load_content("EditPosts"),
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            font=FONT_MD,
            bg='white'
        )
        edit_post_btn.pack(padx=BUTTON_PADDING, pady=BUTTON_PADDING)

        

        base_link = BaseLinkUpdate(self.body)
        base_link.pack()

        test_webpage_btn = tk.Button(
            self.body,
            text="Test With Local Host",
            command= Controller.open_index_html_local_host,
            width=25,
            height=BUTTON_HEIGHT,
            font=FONT_MD,
            bg="white"
        )
        test_webpage_btn.pack(padx=BUTTON_PADDING, pady=BUTTON_PADDING)

        pass

