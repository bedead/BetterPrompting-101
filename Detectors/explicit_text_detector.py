import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


def initialize_gemini(api_key: str):
    genai.configure(api_key=api_key)


def detect_explicit_content(text: str, model_name: str = "gemini-1.5-flash"):
    llm = genai.GenerativeModel(model_name)
    response = llm.generate_content(
        f"Classify the following text as explicit (sexual, harmful, harassing) or not:\n\n{text}"
    )
    return response.candidates[0].content.parts[0].text.strip()


def chatbot():
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    initialize_gemini(GOOGLE_API_KEY)

    print("Welcome to the Explicit Content Detector Chatbot!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        result = detect_explicit_content(user_input)
        print("xBot:", result)


if __name__ == "__main__":
    chatbot()
