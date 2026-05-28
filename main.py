import os
from random import randrange as r 
from time import time as t

def run_multiplication_practice():
    """
    Automates an interactive mathematical evaluation loop.
    Implements dynamic data logging and handles systemic input validation.
    """
    print('Hello! Welcome to Multiplication Practice')
    
    # 1. Defensive Input Validation Subsystem
    try:
        no_questions = int(input('How many questions do you want?: '))
        max_num = int(input('Highest number used in practice?: '))
        if no_questions <= 0 or max_num <= 0:
            raise ValueError("Parameters must be positive integers.")
    except ValueError as e:
        print(f"❌ Input validation error: {e}. Defaulting to 5 questions, max value 10.")
        no_questions = 5
        max_num = 10

    score = 0
    answer_list = []
    
    # 2. Synchronized Session Timeline Anchor
    start_time = t() 
    
    for q in range(no_questions):
        num1, num2 = r(1, max_num + 1), r(1, max_num + 1)
        ans = num1 * num2
        
        # Protective user answer conversion gate
        try:
            u_ans = int(input(f'Question {q+1}/{no_questions}: {num1} X {num2} = '))
        except ValueError:
            print("⚠️ Invalid numeric entry detected. Defaulting assignment to 0.")
            u_ans = 0
            
        answer_list.append(f'{num1} X {num2} = {ans} | Your Answer: {u_ans}')
        
        if u_ans == ans:
            score += 1
            
    # CRITICAL STRUCTURAL FIX: Capture completion time AFTER the processing loop terminates
    end_time = t()
    total_elapsed = round(end_time - start_time, 1)
    
    # Avoid zero-division logic calculation errors
    avg_speed = round(total_elapsed / no_questions, 1) if no_questions > 0 else 0
    accuracy_percentage = round((score / no_questions) * 100) if no_questions > 0 else 0

    # 3. Final Analytical Output Presentation
    print('\n' + '='*40)
    print('Thank you for playing!')
    print(f'Final Score: {score} out of {no_questions} ({accuracy_percentage}%)')
    print(f'Total Velocity: {total_elapsed} seconds ({avg_speed} s/question)')
    print('='*40 + '\n--- Question Review Sheet ---')
    
    for item in answer_list:
        print(item)
        
    # 4. Automated Persistent Leaderboard Logging (The Portfolio Layer)
    log_filename = "practice_leaderboard.txt"
    try:
        with open(log_filename, 'a', encoding='utf-8') as file:
            file.write(f"Session: Accuracy={accuracy_percentage}%, Time={total_elapsed}s, Limit={max_num}\n")
        print(f"\n💾 System performance metrics archived to disk: '{log_filename}'")
    except IOError:
        print("\n❌ File system warning: Unable to persist leaderboard log metrics.")

if __name__ == "__main__":
    run_multiplication_practice()