from crewai import Agent
from langchain_community.chat_models import ChatOllama

movie_search_agent = Agent(
    role="Movie Search Specialist",
    goal="Search for relevant movies based on preferences",
    backstory="Has access to large movie databases and can find fitting movies for any taste.",
    verbose=True,
    llm=ChatOllama(model="ollama/mistral")
)
