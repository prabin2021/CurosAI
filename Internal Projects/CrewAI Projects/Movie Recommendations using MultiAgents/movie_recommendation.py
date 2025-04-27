from crewai import Agent, Task, Crew
from langchain.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the search tool
search_tool = DuckDuckGoSearchRun()

# Create our movie recommendation agents
movie_researcher = Agent(
    role='Movie Researcher',
    goal='Research and analyze movies based on user preferences',
    backstory="""You are a highly knowledgeable movie researcher with expertise in 
    analyzing films across various genres, periods, and styles. You understand both 
    technical and artistic aspects of cinema.""",
    tools=[search_tool],
    verbose=True
)

recommendation_analyst = Agent(
    role='Recommendation Analyst',
    goal='Analyze user preferences and create personalized movie recommendations',
    backstory="""You are an expert in analyzing viewing patterns and user preferences 
    to make highly personalized movie recommendations. You excel at understanding 
    what makes movies appealing to different audiences.""",
    tools=[search_tool],
    verbose=True
)

def get_movie_recommendations(user_preferences):
    # Define tasks for our agents
    research_task = Task(
        description=f"""Research movies that match the following user preferences: {user_preferences}
        Focus on highly-rated and critically acclaimed films that align with these preferences.
        Provide a detailed analysis of why these movies would be good matches.""",
        agent=movie_researcher
    )

    recommendation_task = Task(
        description="""Based on the research results, create a curated list of 5 movie recommendations.
        For each movie, provide:
        1. Title and year
        2. Brief synopsis
        3. Why it matches the user's preferences
        4. What makes it special/unique""",
        agent=recommendation_analyst
    )

    # Create a crew with our agents
    crew = Crew(
        agents=[movie_researcher, recommendation_analyst],
        tasks=[research_task, recommendation_task],
        verbose=True
    )

    # Get recommendations
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    # Example usage
    user_preferences = """
    - Enjoys psychological thrillers
    - Likes complex plot twists
    - Prefers modern cinematography (2010+)
    - Appreciates strong character development
    """
    
    recommendations = get_movie_recommendations(user_preferences)
    print("\nMovie Recommendations:")
    print(recommendations) 