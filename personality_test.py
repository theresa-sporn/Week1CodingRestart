def personality_test():
    print("Welcome to the Personality Test!")
    print("Answer each question with 'yes' or 'no'.")

    questions = [
        "Do you enjoy meeting new people?",
        "Are you comfortable in social situations?",
        "Do you prefer reading books over going to parties?",
        "Are you often the life of the party?",
        "Do you like taking risks?",
    ]

    scores = {"introvert": 0, "extrovert": 0}

    for i, question in enumerate(questions, start=1):
        answer = input(f"Question {i}: {question} (yes/no): ").lower()
        if answer == "yes":
            scores["extrovert"] += 1
        elif answer == "no":
            scores["introvert"] += 1
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")

    print("\nResults:")
    if scores["extrovert"] > scores["introvert"]:
        print("You have extroverted tendencies.")
    elif scores["extrovert"] < scores["introvert"]:
        print("You have introverted tendencies.")
    else:
        print("You have a balanced personality.")

if __name__ == "__main__":
    personality_test()
