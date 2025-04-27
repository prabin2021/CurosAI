from crewai import Agent
from langchain_community.chat_models import ChatOllama

  # Use 'mistral' or another supported model


user_query_agent = Agent(
    role="User Query Analyzer",
    goal="Understand the user's movie preferences",
    backstory="An expert in understanding what movie genres and styles people enjoy.",
    verbose=True,
    llm = ChatOllama(model="mistral")
)
