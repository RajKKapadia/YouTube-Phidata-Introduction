import os

from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2
from phi.llm.openai import OpenAIChat
from phi.embedder.openai import OpenAIEmbedder
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

embedder = OpenAIEmbedder(api_key=os.getenv("OPENAI_API_KEY"))

assistant = Assistant(
    llm=OpenAIChat(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY")),
    storage=PgAssistantStorage(table_name="recipe_assistant", db_url=db_url),
    knowledge_base=PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=PgVector2(collection="recipe_documents", db_url=db_url,
                            embedder=embedder),
    ),
    # Show tool calls in the response
    show_tool_calls=True,
    # Enable the assistant to search the knowledge base
    search_knowledge=True,
    # Enable the assistant to read the chat history
    read_chat_history=True,
)
# # Comment out after first run
# assistant.knowledge_base.load(recreate=False)  # type: ignore

# response = assistant.run("How do I make pad thai?", stream=False)

# print(response)
