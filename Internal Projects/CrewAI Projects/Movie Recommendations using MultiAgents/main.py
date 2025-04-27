from dotenv import load_dotenv
load_dotenv()

from crew import run_crew

if __name__ == "__main__":
    try:
        user_input = input("What kind of movies do you like?\n> ")
        print("\nMovie Recommendations:\n")
        result = run_crew(user_input)
        print(result)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("Please make sure Ollama is running and the Mistral model is installed.")
    

