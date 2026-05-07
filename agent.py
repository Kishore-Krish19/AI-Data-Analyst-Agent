from llm import ask_llm
import tools

def analyze_dataset(path):
    report = []

    report.append(tools.load_dataset(path))
    report.append(tools.dataset_summary())
    report.append(tools.missing_values())
    report.append(tools.correlation_heatmap())
    report.append(tools.train_model())

    explanation = ask_llm(
        "Explain the insights of this dataset:\n" + tools.dataset_summary()
    )

    report.append("\nAI Insights:\n" + explanation)

    with open("report.txt", "w") as f:
        for r in report:
            f.write(r + "\n\n")

    return "Analysis complete. Report saved."

def chatbot():
    print("AI Data Analyst Agent\n")
    
    # Initialize the memory!
    chat_history = [
        {"role": "system", "content": "You are a helpful AI Data Analyst Assistant."}
    ]

    while True:
        user = input("You: ")

        if user.lower() == "exit":
            break

        if user.endswith(".csv"):
            print(analyze_dataset(user))
            # Inject the CSV event into the bot's memory so it knows what you did
            chat_history.append({"role": "user", "content": f"I just uploaded and analyzed a dataset: {user}"})
            chat_history.append({"role": "assistant", "content": "Analysis complete. Report saved."})
        else:
            # Add user input to memory
            chat_history.append({"role": "user", "content": user})
            
            # Pass the WHOLE memory to the LLM
            answer = ask_llm(chat_history)
            
            # Clean up those weird empty lines
            clean_answer = answer.strip() 
            print("Agent:", clean_answer)
            
            # Save the bot's reply to memory
            chat_history.append({"role": "assistant", "content": clean_answer})