from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from enum import Enum
import json


class LinkedInPost(BaseModel):
    title: str = Field(..., description="Título del post de LinkedIn")
    content: str = Field(..., description="Contenido del post de LinkedIn")
    hashtags: List[str] = Field(
        ..., description="Lista de hashtags relevantes para el post de LinkedIn"
    )
    category: str = Field(..., description="Categoría del post de LinkedIn")
