import tkinter as tk
from tkinter import messagebox
import time
from levels import get_level_questions
from database import save_score

class GameApp:
    def __init__(self, root, player_name):
        self.root = root
        self.player_name = player_name
        self.root.title(f"Swadeshi Quest - {player_name}")
        self.root.geometry("900x700")
        
        self.current_level = 1
        self.current_question = 0
        self.score = 0
        self.timer_id = None
        self.time_left = 15
        
        self.setup_ui()
        self.load_level()
    
    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#FF9933", height=80)
        header.pack(fill=tk.X, padx=0, pady=0)
        
        player_label = tk.Label(
            header,
            text=f"Player: {self.player_name}",
            font=("Arial", 14, "bold"),
            bg="#FF9933",
            fg="white"
        )
        player_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        level_label = tk.Label(
            header,
            text=f"Level: {self.current_level}/5",
            font=("Arial", 14, "bold"),
            bg="#FF9933",
            fg="white"
        )
        level_label.pack(side=tk.LEFT, padx=20, pady=10)
        self.level_label = level_label
        
        score_label = tk.Label(
            header,
            text=f"Score: {self.score}",
            font=("Arial", 14, "bold"),
            bg="#FF9933",
            fg="white"
        )
        score_label.pack(side=tk.LEFT, padx=20, pady=10)
        self.score_label = score_label
        
        timer_label = tk.Label(
            header,
            text=f"Time: {self.time_left}s",
            font=("Arial", 14, "bold", "underline"),
            bg="#FF9933",
            fg="white"
        )
        timer_label.pack(side=tk.RIGHT, padx=20, pady=10)
        self.timer_label = timer_label
        
        # Main content area
        self.content_frame = tk.Frame(self.root, bg="white")
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    def load_level(self):
        self.questions = get_level_questions(self.current_level)
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.next_level()
    
    def display_question(self):
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        question_data = self.questions[self.current_question]
        
        # Question text
        question_frame = tk.Frame(self.content_frame, bg="white")
        question_frame.pack(fill=tk.X, pady=20)
        
        question_label = tk.Label(
            question_frame,
            text=f"Question {self.current_question + 1}/{len(self.questions)}",
            font=("Arial", 12, "italic"),
            bg="white",
            fg="#666666"
        )
        question_label.pack()
        
        question_text = tk.Label(
            question_frame,
            text=question_data["question"],
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#333333",
            wraplength=800
        )
        question_text.pack(pady=20)
        
        # Options
        options_frame = tk.Frame(self.content_frame, bg="white")
        options_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        self.selected_option = tk.StringVar()
        
        for i, option in enumerate(question_data["options"]):
            btn = tk.Radiobutton(
                options_frame,
                text=option,
                variable=self.selected_option,
                value=option,
                font=("Arial", 14),
                bg="white",
                fg="#333333",
                selectcolor="#FFD700",
                padx=10,
                pady=10
            )
            btn.pack(fill=tk.X, pady=10, padx=20)
        
        # Submit button
        submit_btn = tk.Button(
            self.content_frame,
            text="Submit Answer",
            font=("Arial", 14, "bold"),
            bg="#138808",
            fg="white",
            width=20,
            height=2,
            command=self.check_answer
        )
        submit_btn.pack(pady=20)
        
        self.current_question_data = question_data
        self.start_timer()
    
    def start_timer(self):
        self.time_left = 15
        self.update_timer()
    
    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time: {self.time_left}s")
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.time_left = 0
            self.timer_label.config(text="Time: 0s")
            messagebox.showwarning("Time's Up!", "You ran out of time!")
            self.next_question()
    
    def check_answer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        
        if not self.selected_option.get():
            messagebox.showwarning("No Answer", "Please select an answer!")
            return
        
        correct_answer = self.current_question_data["answer"]
        if self.selected_option.get() == correct_answer:
            self.score += 10
            messagebox.showinfo("Correct!", f"Great! +10 points\nCorrect Answer: {correct_answer}")
        else:
            messagebox.showinfo(
                "Incorrect",
                f"Wrong!\nCorrect Answer: {correct_answer}\n\nFact: {self.current_question_data.get('fact', 'N/A')}"
            )
        
        self.score_label.config(text=f"Score: {self.score}")
        self.next_question()
    
    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.next_level()
    
    def next_level(self):
        if self.current_level < 5:
            self.current_level += 1
            self.current_question = 0
            self.level_label.config(text=f"Level: {self.current_level}/5")
            messagebox.showinfo("Level Complete!", f"Great! Moving to Level {self.current_level}")
            self.load_level()
        else:
            self.end_game()
    
    def end_game(self):
        save_score(self.player_name, self.score, self.current_level)
        messagebox.showinfo(
            "Game Complete!",
            f"Congratulations {self.player_name}!\n\nFinal Score: {self.score}\nLevels Completed: {self.current_level}\n\nYour score has been saved!"
        )
        self.root.destroy()
