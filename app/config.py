import os
import sys

from app.util.model import FileModel, JsonModel, HtmlModel

def get_app_root():
    if getattr(sys, 'frozen', False):
        app_root = os.path.dirname(sys.executable)
    else:
        app_root = os.path.dirname(os.path.abspath(__file__)) 
        app_root = os.path.dirname(app_root)
    return app_root

def get_parent_dir():
    app_root = get_app_root()
    app_parent_dir = os.path.dirname(app_root)
    return app_parent_dir

def get_bundled_dir():
    if getattr(sys, 'frozen', False):
        app_root = sys._MEIPASS
    else:
        app_root = os.path.abspath(".")
    return app_root

def get_resource_paths():
    app_root = get_app_root()

    config_folder = os.path.join(app_root, "config")
    app_assets_folder = os.path.join(config_folder, "app_assets")
    
    themes_folder = os.path.join(app_root, "themes")
    assets_folder = os.path.join(app_root, "assets")

    config_json_path = os.path.join(config_folder, "config.json")
    posts_json_path = os.path.join(app_root, "posts.json")

    JsonModel.make_json_file_if_new(posts_json_path, {})
    FileModel.make_folder_if_new(themes_folder)
    FileModel.make_folder_if_new(assets_folder)

    resource_paths = {
        "config_folder": config_folder,
        "app_assets_folder": app_assets_folder,
        "config_json": config_json_path,
        "posts_json": posts_json_path,
        "assets_folder": "assets",
        "theme_folder": themes_folder,
        "app_root": app_root
    }
    return resource_paths
