import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Load Google API Key from .env
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


class LLMModel:
    def __init__(self, model_name="gemini-2.5-pro"):
        if not model_name:
            raise ValueError("Model is not defined.")
        
        self.model_name = model_name
        # Use Google Gemini instead of Groq
        self.gemini_model = ChatGoogleGenerativeAI(
            model=self.model_name,
            convert_system_message_to_human=True
        )

    def get_model(self):
        return self.gemini_model


if __name__ == "__main__":
    llm_instance = LLMModel()
    llm_model = llm_instance.get_model()
    
    response = llm_model.invoke("hi")
    print(response)
