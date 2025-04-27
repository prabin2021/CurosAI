from dotenv import load_dotenv
load_dotenv()

from crew import run_crew

if __name__ == "__main__":
    user_input = input("What kind of movies do you like?\n> ")
    result = run_crew(user_input)
    print("\nMovie Recommendations:\n")
    print(result)
