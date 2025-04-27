from crewai import Task
from agents.user_query_agent import user_query_agent
from agents.movie_search_agent import movie_search_agent
from agents.recommendation_agent import recommendation_agent

def get_tasks(user_query):
    task1 = Task(
    description=f"Analyze the user's query and extract key preferences, such as movie genres, themes, actors, or any specific traits. For example, from '{user_query}', identify whether the user is asking for a genre (e.g., thriller, comedy), a mood (e.g., lighthearted, intense), or specific actors/actresses they like.",
    input_type = dict,
    agent=user_query_agent,
    expected_output="A list of extracted preferences such as genres, themes, or actors."
    )


    task2 = Task(
    description="Based on the extracted preferences from the user query, search through a movie database or list to find movies that match the preferences identified in the previous task. For example, if the user prefers thrillers, search for thriller movies that align with their query.",
    input_type = dict,
    agent=movie_search_agent,
    context=[task1],
    expected_output="A list of movie titles that match the user's preferences."
)


    task3 = Task(
    description="Based on the search results from Task 2, recommend the top 3 movies that best match the user's preferences. Each recommendation should include a brief explanation (1-2 sentences) on why it's a good fit for the user's query, referencing specific preferences from Task 1 and the search results from Task 2.",
    input_type = dict,
    agent=recommendation_agent,
    context=[task2],
    expected_output="A list of 3 movie recommendations with short reasons."
)


    return [task1, task2, task3]
