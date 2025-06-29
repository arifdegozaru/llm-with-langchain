import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor

load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOpenAI(api_key=os.environ["OPEN_AI_KEY"], model="gtp-3.5-turbo")
    template = """give the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
    Your answer should contain only URL"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func="?",
            description="useful for when you need get the Linkedin Page Url"
        )
    ]

    return "https://www.linkedin.com/in/arif-hidayatulah-4817a5a8"
