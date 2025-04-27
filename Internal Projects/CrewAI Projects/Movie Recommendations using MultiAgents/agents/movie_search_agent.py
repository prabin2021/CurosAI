from crewai import Agent
from langchain.chat_models import ChatOpenAI

movie_search_agent = Agent(
    role="Movie Search Specialist",
    goal="Search for relevant movies based on preferences",
    backstory="Has access to large movie databases and can find fitting movies for any taste.",
    verbose=True,
    llm=ChatOpenAI(temperature=0.7, model="gpt-4")
)
