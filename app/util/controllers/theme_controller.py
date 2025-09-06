import os

from app.util.controller import Controller, JsonController
THEME_FOLDER_PATH = Controller.get_resource_paths("theme_folder")


class ThemePaths:
    @staticmethod
    def get_basenames() -> list:
            basenames = os.listdir(THEME_FOLDER_PATH)
            if len(basenames) == 0:
                 print(f"Warning: No themes detected in file system. Check Theme Folder Path {THEME_FOLDER_PATH}")
            return basenames

    @staticmethod
    def get_all_paths() -> list:
        basenames = ThemePaths.get_basenames()
        paths:list = []
        for basename in basenames:
            path = os.path.join(THEME_FOLDER_PATH, basename)  
            paths.append(path)
        return paths

    @staticmethod
    def get_path(basename:str):
        path:str = os.path.join(THEME_FOLDER_PATH, basename)
        return path
    
    @staticmethod
    def get_local_path(basename:str):
         return os.path.join('themes', basename)

    @staticmethod
    def get_theme_folder_path()->str:
         return THEME_FOLDER_PATH
    
    @staticmethod
    def get_last_used_basename() -> str:
        last_used_basename = JsonController.get_config_data("theme")
        if last_used_basename == None or last_used_basename == "":
            last_used_basename = ThemePaths.get_basenames()[0]
        return last_used_basename
    
    @staticmethod
    def get_last_used_path()->str:
        return ThemePaths.get_path(ThemePaths.get_basenames)
