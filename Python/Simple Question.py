questions = {
    "What is the capital of France? ": "Paris",
    "What is 5 + 7? ": "12",
    "What is the color of the sky? ": "Blue"
}

score = 0
for question, correct_answer in questions.items():
    answer = input(question)
    if answer.strip().lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
print(f"Your final score is {score}/{len(questions)}")
