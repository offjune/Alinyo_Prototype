import google.generativeai as genai
import os
from dotenv import load_dotenv
from .prompts import SYSTEM_INSTRUCTION, START_QUESTIONS

load_dotenv()

try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except Exception as e:
    print(f"Erro ao inicializar o cliente Google AI. Verifique sua chave de API.")
    print(f"Detalhe do erro: {e}")
    exit()


class Chatbot:
    def __init__(self):
        system_instruction = SYSTEM_INSTRUCTION

        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=system_instruction
        )

        self.chat = self.model.start_chat(history=[])
        initial_greeting = START_QUESTIONS

        print(f"\n {initial_greeting}")

    def get_response(self, user_message):
        try:
            response = self.chat.send_message(user_message)
            return response.text
        except Exception as e:
            print(f"Ocorreu um erro na API do Gemini: {e}")
            return "Desculpe, estou com problemas para me conectar no momento. Tente novamente mais tarde."
