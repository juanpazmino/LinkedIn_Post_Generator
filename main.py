from core import SmartChatbot
from pydantic import ValidationError

print("\nWelcome to the LinkedIn Post Generator!")
print("\nPlease enter the information you want to include in your LinkedIn post.")
print(
    "You can provide details such as the topic, key points, target audience, and any specific information you want to highlight."
)
print("The more detailed your input, the better the generated post will be!\n")


bot = SmartChatbot()

prompt = input("Enter your prompt (or type '/exit' to quit): ")


while prompt:
    if prompt.lower() == "/exit":
        print("Exiting the LinkedIn Post Generator. Goodbye!")
        break
    else:
        try:
            response = bot.generate_response(prompt)
            print("\nGenerated LinkedIn Post:\n")
            print("-------------------------\n")
            print(f"Title: {response.title}")
            print("--------------------------")
            print(f"Content: {response.content}")
            print("--------------------------")
            print(f"Hashtags: {', '.join(response.hashtags)}")
            print(f"Category: {response.category}\n")

        except ValidationError as err:
            print(err)
        except Exception as e:
            print(f"An error occurred: {str(e)}\n")

    prompt = input("Enter your prompt (or type '/exit' to quit): ")
