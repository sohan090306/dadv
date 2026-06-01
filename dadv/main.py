import customtkinter as ctk
from tkinter import messagebox
from game import GameEngine
from database import get_top_scores

# Set global CustomTkinter aesthetics
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class SwadeshiQuestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Swadeshi Quest: Journey Towards Atmanirbhar Bharat")
        self.root.geometry("950x700")
        
        self.current_frame = None
        self.show_main_menu()
        
    def clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.current_frame = None

    def show_main_menu(self):
        self.clear_frame()
        
        self.current_frame = ctk.CTkFrame(self.root, fg_color="#F4F4F9", corner_radius=0)
        self.current_frame.pack(fill=ctk.BOTH, expand=True)
        
        # Subtle Saffron/Green Banners
        saffron_header = ctk.CTkFrame(self.current_frame, fg_color="#FF6F00", height=15, corner_radius=0)
        saffron_header.pack(fill=ctk.X, side=ctk.TOP)
        
        green_footer = ctk.CTkFrame(self.current_frame, fg_color="#0A7E07", height=15, corner_radius=0)
        green_footer.pack(fill=ctk.X, side=ctk.BOTTOM)
        
        # Center container for layout
        content = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        content.pack(expand=True)
        
        # Title
        lbl_title = ctk.CTkLabel(content, text="Swadeshi Quest", font=("Helvetica", 54, "bold"), text_color="#1A237E")
        lbl_title.pack(pady=(10, 5))
        
        lbl_subtitle = ctk.CTkLabel(content, text="Journey Towards Atmanirbhar Bharat", font=("Helvetica", 24, "italic"), text_color="#FF6F00")
        lbl_subtitle.pack(pady=(0, 40))
        
        # Player Name Input
        self.entry_name = ctk.CTkEntry(content, placeholder_text="Enter your Name here...", font=("Helvetica", 16), width=350, height=50, corner_radius=15, border_color="#1A237E", border_width=2)
        self.entry_name.pack(pady=20)
        
        # Menu Buttons with smooth hover effects
        btn_start = ctk.CTkButton(content, text="▶️ Start Game", font=("Helvetica", 20, "bold"), fg_color="#0A7E07", hover_color="#005000", text_color="white", width=350, height=55, corner_radius=25, command=self.start_game)
        btn_start.pack(pady=10)
        
        btn_scores = ctk.CTkButton(content, text="🏆 High Scores", font=("Helvetica", 18, "bold"), fg_color="#FF6F00", hover_color="#CC5800", text_color="white", width=350, height=45, corner_radius=20, command=self.show_high_scores)
        btn_scores.pack(pady=10)
        
        btn_analytics = ctk.CTkButton(content, text="📊 View Analytics", font=("Helvetica", 18, "bold"), fg_color="#4CAF50", hover_color="#388E3C", text_color="white", width=350, height=45, corner_radius=20, command=self.show_analytics)
        btn_analytics.pack(pady=10)

        btn_instructions = ctk.CTkButton(content, text="📖 Instructions", font=("Helvetica", 18, "bold"), fg_color="#1A237E", hover_color="#0D145A", text_color="white", width=350, height=45, corner_radius=20, command=self.show_instructions)
        btn_instructions.pack(pady=10)
        
        btn_exit = ctk.CTkButton(content, text="🚪 Exit", font=("Helvetica", 18, "bold"), fg_color="#757575", hover_color="#555555", text_color="white", width=350, height=45, corner_radius=20, command=self.root.quit)
        btn_exit.pack(pady=10)

    def start_game(self):
        player_name = self.entry_name.get().strip()
        if not player_name:
            messagebox.showwarning("Input Error", "Please enter your name to start the game!")
            return
            
        self.clear_frame()
        self.current_frame = ctk.CTkFrame(self.root, fg_color="#F4F4F9", corner_radius=0)
        self.current_frame.pack(fill=ctk.BOTH, expand=True)
        self.game = GameEngine(self.current_frame, player_name, self.show_main_menu)

    def show_high_scores(self):
        self.clear_frame()
        self.current_frame = ctk.CTkFrame(self.root, fg_color="#F4F4F9", corner_radius=0)
        self.current_frame.pack(fill=ctk.BOTH, expand=True)
        
        lbl_title = ctk.CTkLabel(self.current_frame, text="🏆 Top 10 High Scores 🏆", font=("Helvetica", 36, "bold"), text_color="#1A237E")
        lbl_title.pack(pady=40)
        
        scores = get_top_scores()
        
        if not scores:
            lbl_no = ctk.CTkLabel(self.current_frame, text="No scores yet. Be the first to play!", font=("Helvetica", 20, "italic"), text_color="#757575")
            lbl_no.pack(pady=20)
        else:
            # Modern table card
            table_card = ctk.CTkFrame(self.current_frame, fg_color="white", corner_radius=15, border_color="#DDDDDD", border_width=2)
            table_card.pack(pady=10, padx=50)
            
            # Header Row
            headers = ["Rank", "Player", "Score", "Levels"]
            for col, text in enumerate(headers):
                lbl = ctk.CTkLabel(table_card, text=text, font=("Helvetica", 18, "bold"), text_color="#FF6F00", width=150)
                lbl.grid(row=0, column=col, pady=(15,5), padx=10)
            
            # Data Rows
            for idx, (name, score, levels) in enumerate(scores):
                ctk.CTkLabel(table_card, text=str(idx+1), font=("Helvetica", 16), text_color="#333333").grid(row=idx+1, column=0, pady=5)
                ctk.CTkLabel(table_card, text=name, font=("Helvetica", 16), text_color="#333333").grid(row=idx+1, column=1, pady=5)
                ctk.CTkLabel(table_card, text=str(score), font=("Helvetica", 18, "bold"), text_color="#0A7E07").grid(row=idx+1, column=2, pady=5)
                ctk.CTkLabel(table_card, text=str(levels), font=("Helvetica", 16), text_color="#333333").grid(row=idx+1, column=3, pady=5)
            
            # Bottom padding for table
            ctk.CTkLabel(table_card, text="").grid(row=len(scores)+1, column=0, pady=(0, 10))
        
        btn_back = ctk.CTkButton(self.current_frame, text="🔙 Back to Menu", font=("Helvetica", 18, "bold"), fg_color="#1A237E", hover_color="#0D145A", text_color="white", width=250, height=45, corner_radius=20, command=self.show_main_menu)
        btn_back.pack(pady=40)

    def show_instructions(self):
        instructions = (
            "Welcome to Swadeshi Quest!\n\n"
            "1. Enter your name and click '▶️ Start Game'.\n"
            "2. There are 5 levels testing your knowledge about India:\n"
            "   - Level 1: Indian States & Capitals\n"
            "   - Level 2: Freedom Fighters\n"
            "   - Level 3: Festivals & Culture\n"
            "   - Level 4: Swadeshi Products\n"
            "   - Level 5: Traditional Games\n"
            "3. You have 15 seconds to answer each question.\n"
            "4. Answer quickly to earn more bonus points!\n"
            "5. You have ONE '💡 50/50 Lifeline' per game to remove two wrong options.\n"
            "6. The top 10 scores are saved on the Leaderboard.\n\n"
            "Embrace Atmanirbhar Bharat. Good luck!"
        )
        messagebox.showinfo("📖 Instructions", instructions)

    def show_analytics(self):
        try:
            from dashboard import show_analytics_dashboard
            success = show_analytics_dashboard()
            if not success:
                messagebox.showinfo("Analytics", "No scores available yet. Play a game first!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not load analytics: {str(e)}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = SwadeshiQuestApp(root)
    root.mainloop()
