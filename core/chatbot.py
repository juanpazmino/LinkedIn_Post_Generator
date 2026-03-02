from core.api_client import api_client
from models.linkedin_post import LinkedInPost
from pydantic import ValidationError


class SmartChatbot:
    def __init__(self):
        self.api_client = api_client()

    def generate_response(self, prompt):
        try:
            description = self.api_client.api_response(prompt)

            if description is None:
                raise ValueError("La API no retornó una respuesta válida")

            print(f"✓ LinkedinPost generate sucessfully: {description.title}")
            return description

        except Exception as e:
            print(f"✗ Error generating description: {str(e)}")
            raise
