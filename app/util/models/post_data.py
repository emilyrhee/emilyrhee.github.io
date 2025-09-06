from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class LinkData:
    link: str
    text: str

@dataclass
class PostData:
    datetime:str 
    title:str 
    caption:str 
    media_links:str 
    base_link:str 
    username:str
    profile_pic:str 
    email:str 
    links:list 

