def dortmund_fan_quiz():
    print("Welcome to the Borussia Dortmund Fan Quiz!")
    print("Answer the following questions to find out if you're a real Dortmund fan.")

    questions = [
        "Who is Borussia Dortmund's all-time top goal scorer?",
        "In which year did Borussia Dortmund win their first UEFA Champions League title?",
        "What is the stadium name where Borussia Dortmund plays their home matches?",
        "Who is the current captain of Borussia Dortmund?",
        "What are Borussia Dortmund's team colors?"
    ]

    correct_answers = [
        "Michael Zorc",
        "1997",
        "Signal Iduna Park",
        "Emre Can",
        "Yellow and Black"
    ]

    score = 0

    for i, question in enumerate(questions, start=1):
        answer = input(f"Question {i}: {question}\nYour Answer: ").strip().lower()
        
        # Check if the answer contains both "yellow" and "black"
        if "yellow" in answer and "black" in answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, that's not correct. The correct answer is: {correct_answers[i - 1]}\n")

    print(f"Quiz completed! You got {score} out of {len(questions)} questions correct.")

    if score >= 3:
        print("Congratulations! You're a true Borussia Dortmund fan.")
    else:
        print("You might want to brush up on your Borussia Dortmund knowledge to become a true fan.")

if __name__ == "__main__":
    dortmund_fan_quiz()
