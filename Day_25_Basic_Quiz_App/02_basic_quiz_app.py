# Project: Basic Quiz App (MCQs with Score)
# Day: 25 - Python Mini Projects Series
# Week 4: OOP & Little Challenges
# Author: Faiz Ur Rehman Ashrafi
# Goal:
#   - Create a Quiz system using OOP
#   - Display multiple choice questions
#   - Calculate total score at the end
# filename : 02_basic_quiz_app.py

from typing import List


class Question:
    def __init__(self, question: str, options: List[str], correct_option: str) -> None:
        self.question: str = question
        self.options: List[str] = options
        self.correct_option: str = correct_option

    def is_correct(self, answer: str) -> bool:
        """Check if the provided answer matches the correct option."""
        return answer.lower() == self.correct_option.lower()


class Quiz:
    def __init__(self) -> None:
        self.questions: List[Question] = []  # More specific type
        self.score: int = 0

    def add_question(self, question: Question) -> None:
        """Add a Question object to the quiz."""
        self.questions.append(question)

    def start(self) -> None:
        """Start the quiz and interact with the user."""
        print("\n===== Welcome to the Basic Quiz App =====\n")

        for idx, q in enumerate(self.questions, start=1):
            print(f"Q{idx}: {q.question}")
            for opt in q.options:
                print(f"   {opt}")
            answer: str = input("Enter your answer (a/b/c/d): ")

            if q.is_correct(answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! Correct answer was: {q.correct_option}\n")

        print(f"Quiz Completed! Your Final Score: {self.score}/{len(self.questions)}")


# --- Main Program Execution ---
if __name__ == "__main__":
    quiz = Quiz()

    quiz.add_question(
        Question(
            "What is the capital of Pakistan?",
            ["a) Karachi", "b) Lahore", "c) Islamabad", "d) Peshawar"],
            "c",
        )
    )

    quiz.add_question(
        Question(
            "Which language is known as the backbone of web development?",
            ["a) Python", "b) JavaScript", "c) C++", "d) Java"],
            "b",
        )
    )

    quiz.add_question(
        Question(
            "Who developed the theory of relativity?",
            [
                "a) Isaac Newton",
                "b) Galileo Galilei",
                "c) Albert Einstein",
                "d) Nikola Tesla",
            ],
            "c",
        )
    )

    quiz.start()
