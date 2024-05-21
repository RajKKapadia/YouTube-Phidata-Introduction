import os

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

assistant = Assistant(
    llm=OpenAIChat(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY")),
    description="You help people with their health and fitness goals.",
    instructions=["Recipes should be under 5 ingredients"],
    debug_mode=True,
)

# -*- Print the response in markdown format
assistant.print_response("Share a breakfast recipe.", markdown=True)
