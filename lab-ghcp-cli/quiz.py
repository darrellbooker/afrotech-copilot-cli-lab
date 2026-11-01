from questions import QUESTIONS
from utils import format_question, display_score


def check_answer(user_answer, correct_answer):
    return user_answer.strip().upper() == correct_answer.upper()


def calculate_score(results):
    score = 0
    for result in results[:-1]:
        if result:
            score += 1
    return score


def run_quiz(questions):
    print("\n🚀 Welcome to the AFROTECH 2026 Trivia Quiz! 🚀")
    print("Answer each question by typing A, B, C, or D.")
    print("No hints along the way. You'll see your score at the end.\n")

    results = []

    for i, q in enumerate(questions):
        print(format_question(i, q))
        user_answer = input("\nYour answer: ").strip().upper()
        results.append(check_answer(user_answer, q["answer"]))
        print("🔒 Locked in.")

    score = calculate_score(results)
    print(display_score(score, len(questions)))
    return score


def play_again():
    choice = input("\nPlay again? (y/n): ").strip().lower()
    return choice in ("y", "yes")


if __name__ == "__main__":
    while True:
        run_quiz(QUESTIONS)
        if not play_again():
            print("\nThanks for playing! 👋")
            break
