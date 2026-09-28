from pydantic import BaseModel
from typing import List, Optional

class ComicPanel(BaseModel):
    panel_number: int
    description: str
    dialogue: str
    image_prompt: Optional[str] = ""

class ComicOutline(BaseModel):
    title: str
    panels: List[ComicPanel]