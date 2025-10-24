# Project: Basic Quiz App (MCQs with Score)
# Day: 25 - Python Mini Projects Series
# Week 4: OOP & Little Challenges
# Author: Faiz Ur Rehman Ashrafi
# Goal:
#   - Create a Quiz system using OOP
#   - Display multiple choice questions
#   - Calculate total score at the end
# filename : 01_basic_quiz_app.py


class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, answer):
        return answer.lower() == self.correct_option.lower()


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start(self):
        print("\n===== Welcome to the Basic Quiz App =====\n")
        for idx, q in enumerate(self.questions, start=1):
            print(f"Q{idx}: {q.question}")
            for opt in q.options:
                print(f"   {opt}")
            answer = input("Enter your answer (a/b/c/d): ")
            if q.is_correct(answer):
                print("✅ Correct!\n")
                self.score += 1
            else:
                print(f"❌ Wrong! Correct answer was: {q.correct_option}\n")

        print(
            f"🎯 Quiz Completed! Your Final Score: {self.score}/{len(self.questions)}"
        )


# --- Main Program Execution ---
if __name__ == "__main__":
    quiz = Quiz()

    # Add questions
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
