from openai import OpenAI

client = OpenAI()

print("Welcome to the GPT Text Assistant!")
print("Type 'exit' to close the application.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Thank you for using the GPT Text Assistant!")
        break

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user_input
        )

        print("\nAI:", response.output_text)
        print()

    except Exception as e:
        print("An error occurred:", e)
