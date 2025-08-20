from typing import Optional
from pydantic import BaseModel

class PersonagemToyStory(BaseModel):
    
    id: Optional[int] = None
    nome: str
    dono: str
    tamanho: str
    foto: str