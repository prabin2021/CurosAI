from crewai import Task
from agents.user_query_agent import user_query_agent
from agents.movie_search_agent import movie_search_agent
from agents.recommendation_agent import recommendation_agent

def get_tasks(user_query):
    task1 = Task(
        description=f"Analyze this user query and extract preferences: '{user_query}'",
        agent=user_query_agent
    )

    task2 = Task(
        description="Search for movies that match the extracted preferences.",
        agent=movie_search_agent,
        context=[task1]
    )

    task3 = Task(
        description="Recommend the top 3 movies with short reasons.",
        agent=recommendation_agent,
        context=[task2]
    )

    return [task1, task2, task3]
