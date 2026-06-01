import tkinter as tk
from tkinter import messagebox, simpledialog
import customtkinter as ctk
from game import GameApp
from database import init_database, get_leaderboard

class WelcomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Swadeshi Quest - Welcome")
        self.root.geometry("800x600")
        self.root.configure(bg="#FF9933")
        
        # Initialize database
        init_database()
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg="#FF9933")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = tk.Label(
            self.main_frame,
            text="Swadeshi Quest",
            font=("Arial", 48, "bold"),
            bg="#FF9933",
            fg="white"
        )
        title.pack(pady=30)
        
        subtitle = tk.Label(
            self.main_frame,
            text="Journey Towards Atmanirbhar Bharat",
            font=("Arial", 18),
            bg="#FF9933",
            fg="white"
        )
        subtitle.pack(pady=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.main_frame, bg="#FF9933")
        buttons_frame.pack(pady=40)
        
        # Start Game Button
        start_btn = tk.Button(
            buttons_frame,
            text="Start Game",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#FF9933",
            width=20,
            height=2,
            command=self.start_game
        )
        start_btn.pack(pady=10)
        
        # Leaderboard Button
        leaderboard_btn = tk.Button(
            buttons_frame,
            text="View Leaderboard",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#FF9933",
            width=20,
            height=2,
            command=self.show_leaderboard
        )
        leaderboard_btn.pack(pady=10)
        
        # Instructions Button
        instructions_btn = tk.Button(
            buttons_frame,
            text="Instructions",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#FF9933",
            width=20,
            height=2,
            command=self.show_instructions
        )
        instructions_btn.pack(pady=10)
        
        # Exit Button
        exit_btn = tk.Button(
            buttons_frame,
            text="Exit",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#FF9933",
            width=20,
            height=2,
            command=root.quit
        )
        exit_btn.pack(pady=10)
    
    def start_game(self):
        player_name = simpledialog.askstring("Player Registration", "Enter your name:")
        if player_name and player_name.strip():
            self.root.destroy()
            root = tk.Tk()
            app = GameApp(root, player_name.strip())
            root.mainloop()
    
    def show_leaderboard(self):
        scores = get_leaderboard()
        leaderboard_text = "TOP 10 HIGH SCORES\n" + "="*40 + "\n\n"
        for i, (name, score, levels) in enumerate(scores, 1):
            leaderboard_text += f"{i}. {name:<20} Score: {score:<6} Levels: {levels}\n"
        
        messagebox.showinfo("Leaderboard", leaderboard_text)
    
    def show_instructions(self):
        instructions = """
SWADESHI QUEST - INSTRUCTIONS

Welcome to Swadeshi Quest! An interactive educational game about India.

HOW TO PLAY:
1. Enter your name to register
2. Answer questions across 5 levels:
   - Level 1: Indian States
   - Level 2: Freedom Fighters
   - Level 3: Indian Festivals
   - Level 4: Swadeshi Products
   - Level 5: Traditional Games

3. Each question has a time limit
4. Correct answer = +10 points
5. Wrong answer = 0 points
6. Complete all levels to see your final score

SCORING:
- Leaderboard shows Top 10 scores
- Compete with others and climb the ranks!

Good Luck and Jai Bharat!
        """
        messagebox.showinfo("Instructions", instructions)

if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeScreen(root)
    root.mainloop()
