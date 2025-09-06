import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
from app.gui.widgets.frames import WidgetFrame
from app.gui.widgets.labels import WidgetLabel
from app.gui.widgets.text import Entry
from app.util.controller import JsonController, Controller
from app.util.model import JsonModel
from app.util.models.post import Post

class BaseLinkUpdate(WidgetFrame):
    def __init__(self, container):
        super().__init__(container)
        self.config_data = None
        self.base_link = None
        self.base_link_var = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        #BODY
        self.lbl = WidgetLabel(self, text="Base Link:   ")
        self.lbl.grid(column=0, row=0)

        self.text_field = Entry(
            self, 
            width= 40,
            state="disabled")
        self.text_field.grid(column=1,row=0)

        self.edit_btn = tk.Button(self, text="Edit", command=self.edit, bg="white")
        self.edit_btn.grid(column=2, row=0, padx=5)  
        self.update_btn = tk.Button(self, text="Update",  command=self.update, bg="white")
        self.cancel_btn = tk.Button(self, text="Cancel",  command=self.cancel, bg="white")
        self.load_config_base_link()

    def edit(self):
        self.edit_btn.grid_forget()
        self.update_btn.grid(column=2, row=0,padx=5)
        self.cancel_btn.grid(column=3, row=0, padx=5)
        self.text_field.config(state="normal")

    def update(self):
        new_base_link = self.text_field.get()
        if askyesno(title="Change Base Link", message=f"Are you sure you want to replace {self.base_link} with {new_base_link}"):
            update_base_link(new_base_link)
        self.update_btn.grid_forget()
        self.cancel_btn.grid_forget()
        self.edit_btn.grid(column=2, row=0, padx=5)
        self.text_field.config(state="disabled")
        self.load_config_base_link()

    def cancel(self):
        self.update_btn.grid_forget()
        self.cancel_btn.grid_forget()
        self.edit_btn.grid(column=2, row=0)
        self.text_field.config(state="disabled")
        self.load_config_base_link()

    def load_config_base_link(self):
        self.config_data = JsonController.get_config_data()

        self.base_link = self.config_data["base_link"]
        self.text_field.config(state="normal")
        self.text_field.delete(0, tk.END)
        self.text_field.insert(0, self.base_link)
        self.text_field.config(state="disabled")
        pass

def update_base_link(new_base_link:str):
    old_base_link = JsonController.get_config_data("base_link")
    if new_base_link == old_base_link:
        return
    update_post_data(new_base_link, old_base_link)
    JsonController.set_config_data(key="base_link", data = new_base_link)
    
def update_post_data(new_base_link:str, old_base_link:str):
    posts_data:dict = JsonController.get_posts_data()
    if not posts_data or not isinstance(posts_data, dict):
        return
    for post_id, post in posts_data.items():
        if not isinstance(post, dict):
            continue
        post["base_link"] = new_base_link
        post["profile_pic"] = update_data_base_link(post["profile_pic"], new_base_link, old_base_link)

        for media in post["media_links"]:
            if not isinstance(media, list):
                continue
            update_data_base_link(media, new_base_link, old_base_link)
    JsonModel.write_json_file(Controller.get_resource_paths("posts_json"), posts_data)

def update_data_base_link(media_web_path:str, new_base_link:str, old_base_link:str):
    new_media_web_path = remove_prefix(media_web_path, old_base_link)
    if new_media_web_path.startswith("/") and new_base_link.endswith("/"):
        new_media_web_path = new_media_web_path[1:]
    if not new_media_web_path.startswith("/") and not new_base_link.endswith("/"):
        new_base_link += "/"
    new_media_link = new_base_link + new_media_web_path
    return new_media_link

def remove_prefix(string:str, prefix:str):
        if string.startswith(prefix):
            return string[len(prefix):] 
        return string

    

