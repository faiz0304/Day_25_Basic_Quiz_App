# Basic Quiz App (MCQs with Score)

**Day:** 25  
**Week:** 4 - OOP & Little Challenges  
**Author:** Faiz Ur Rehman Ashrafi  

---

## Project Goal
To create a simple **Quiz Application** using **Object-Oriented Programming (OOP)** in Python that:
- Displays multiple-choice questions (MCQs)
- Takes user input for answers
- Calculates and shows the total score at the end

---

## Features
- Uses **classes and objects** for structure  
- Supports multiple questions  
- Checks answers and gives feedback (Correct / Wrong)  
- Displays **final score** at the end  

---

## Classes Used

### `Question` Class
Handles:
- The question text  
- The multiple-choice options  
- The correct answer  
- A method `is_correct()` to check the answer validity  

### 🟣 `Quiz` Class
Handles:
- Storing all questions  
- User interaction and quiz flow  
- Score calculation and display  

---

## 📁 Files Overview

| Filename | Description |
|-----------|--------------|
| `01_basic_quiz_app.py` | Base version of the quiz app using OOP without type hints |
| `02_basic_quiz_app.py` | Enhanced version with full type hints and docstrings |

---

## ▶️ How to Run
1. Open the terminal or command prompt.  
2. Navigate to your project directory.  
3. Run either file:
   ```bash
   python 01_basic_quiz_app.py
### OR
   python 02_basic_quiz_app.py

4. Enter your answers (a/b/c/d) for each question and see your final score.

## Sample Output

  ===== Welcome to the Basic Quiz App =====

  Q1: What is the capital of Pakistan?
    a) Karachi
    b) Lahore
    c) Islamabad
    d) Peshawar
  Enter your answer (a/b/c/d): c
  Correct!

  Q2: Which language is known as the backbone of web development?
    a) Python
    b) JavaScript
    c) C++
    d) Java
  Enter your answer (a/b/c/d): b
  Correct!

  Q3: Who developed the theory of relativity?
    a) Isaac Newton
    b) Galileo Galilei
    c) Albert Einstein
    d) Nikola Tesla
  Enter your answer (a/b/c/d): c
  Correct!

  Quiz Completed! Your Final Score: 3/3

