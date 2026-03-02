# Lirbary imports
from xmlrpc import client

from openai import AzureOpenAI
import warnings

warnings.filterwarnings("ignore")  # specify to ignore warning messages

from dotenv import load_dotenv

from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from enum import Enum
import json

from models import LinkedInPost

# Load environment variables from .env file
load_dotenv()


class api_client:
    def __init__(self):
        self.deployment = "gpt-4.1-nano"  # Nombre del modelo desplegado en Azure OpenAI
        self.client = AzureOpenAI()  # Inicia el cliente y como las variables tiene el nombre del SDK no hace falta escribir


    def api_response(self, prompt):
        try:
            # Realizar la llamada a la API con structured outputs
            completion = self.client.beta.chat.completions.parse(
                model=self.deployment,
                messages=[
                    {
                        "role": "system",
                        "content": 
                        "You are an expert in digital marketing and SEO content writing."
                        "Your task is to generate professional and engaging LinkedIn posts based on the information provided by the user. "
                        "Ensure the content is relevant, informative, and engaging for LinkedIn's audience, using a professional and persuasive tone. "
                        "Include relevant hashtags to increase post visibility. "
                        "The post should be clear, concise, and highlight the key points of the information provided by the user.",
                    },
                    {"role": "user", "content": prompt},
                ],
                response_format=LinkedInPost,
                temperature=0.9,
                max_tokens=2000,
            )
            return completion.choices[0].message.parsed
        except Exception as e:
            print(f"✗ Error generating description: {str(e)}")
            raise
