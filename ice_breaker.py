from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai

if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain!")
    print(os.environ['COOL_API_KEY'])
