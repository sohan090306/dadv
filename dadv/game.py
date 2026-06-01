import customtkinter as ctk
from tkinter import messagebox
import winsound
import random
from levels import LEVELS
from database import save_score

class GameEngine:
    def __init__(self, master, player_name, on_finish):
        self.master = master
        self.player_name = player_name
        self.on_finish = on_finish
        
        self.score = 0
        self.current_level_idx = 0
        self.current_question_idx = 0
        self.time_left = 15
        self.timer_job = None
        self.answered = False
        self.lifeline_used = False
        
        # Base frame setup
        self.frame = ctk.CTkFrame(self.master, fg_color="#F4F4F9", corner_radius=0) 
        self.frame.pack(fill=ctk.BOTH, expand=True)
        
        self.setup_ui()
        self.load_question()
        
    def setup_ui(self):
        # Saffron Header
        self.header_frame = ctk.CTkFrame(self.frame, fg_color="#FF6F00", corner_radius=0)
        self.header_frame.pack(fill=ctk.X)
        
        # Home Button
        self.btn_home = ctk.CTkButton(self.header_frame, text="🏠 Quit", font=("Helvetica", 16, "bold"), fg_color="#D32F2F", hover_color="#B71C1C", text_color="white", width=80, height=40, corner_radius=15, command=self.quit_to_menu)
        self.btn_home.pack(side=ctk.LEFT, padx=15, pady=15)
        
        self.lbl_level = ctk.CTkLabel(self.header_frame, text="", fg_color="transparent", text_color="white", font=("Helvetica", 22, "bold"))
        self.lbl_level.pack(side=ctk.LEFT, padx=20, pady=15)
        
        self.lbl_score = ctk.CTkLabel(self.header_frame, text=f"Score: {self.score}", fg_color="transparent", text_color="white", font=("Helvetica", 20, "bold"))
        self.lbl_score.pack(side=ctk.RIGHT, padx=20, pady=15)
        
        self.lbl_timer = ctk.CTkLabel(self.header_frame, text="⏳ 15", fg_color="transparent", text_color="#1A237E", font=("Helvetica", 24, "bold")) 
        self.lbl_timer.pack(side=ctk.RIGHT, padx=20, pady=15)
        
        # Progress Bar
        self.progress = ctk.CTkProgressBar(self.frame, width=700, height=15, progress_color="#0A7E07", corner_radius=10)
        self.progress.pack(pady=25)
        self.progress.set(0)
        
        # Premium Card Frame for Questions
        self.card_frame = ctk.CTkFrame(self.frame, fg_color="white", corner_radius=20, border_color="#E0E0E0", border_width=2)
        self.card_frame.pack(pady=10, padx=50, fill=ctk.BOTH, expand=True)
        
        # Question Display
        self.lbl_question = ctk.CTkLabel(self.card_frame, text="", fg_color="transparent", text_color="#333333", font=("Helvetica", 24, "bold"), wraplength=700, justify="center")
        self.lbl_question.pack(pady=(20, 30))
        
        # Option Buttons Container
        self.options_frame = ctk.CTkFrame(self.card_frame, fg_color="transparent")
        self.options_frame.pack(pady=10)
        
        self.option_buttons = []
        for i in range(4):
            btn = ctk.CTkButton(self.options_frame, text="", font=("Helvetica", 18), 
                                fg_color="#F0F0F0", hover_color="#E0E0E0", text_color="#1A237E", 
                                width=500, height=50, corner_radius=15, 
                                command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=10)
            self.option_buttons.append(btn)
            
        # Fact/Feedback Label
        self.lbl_fact = ctk.CTkLabel(self.card_frame, text="", fg_color="transparent", text_color="#1A237E", font=("Helvetica", 18, "italic"), wraplength=700)
        self.lbl_fact.pack(pady=20)
        
        # Action Buttons Frame
        self.action_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.action_frame.pack(pady=20)
        
        # 50/50 Lifeline Button
        self.btn_lifeline = ctk.CTkButton(self.action_frame, text="💡 50/50 Lifeline", font=("Helvetica", 18, "bold"), fg_color="#1A237E", hover_color="#0D145A", text_color="white", width=200, height=45, corner_radius=20, command=self.use_lifeline)
        self.btn_lifeline.pack(side=ctk.LEFT, padx=30)
        
        # Next Button
        self.btn_next = ctk.CTkButton(self.action_frame, text="Next ⏭️", font=("Helvetica", 18, "bold"), fg_color="#0A7E07", hover_color="#006400", text_color="white", width=200, height=45, corner_radius=20, state=ctk.DISABLED, command=self.next_question)
        self.btn_next.pack(side=ctk.RIGHT, padx=30)

    def load_question(self):
        self.answered = False
        self.time_left = 15
        self.lbl_timer.configure(text=f"⏳ {self.time_left}")
        self.lbl_fact.configure(text="")
        
        self.btn_next.configure(state=ctk.DISABLED, fg_color="#A9A9A9") 
        
        if not self.lifeline_used:
            self.btn_lifeline.configure(state=ctk.NORMAL, fg_color="#1A237E")
        
        level_data = LEVELS[self.current_level_idx]
        question_data = level_data["questions"][self.current_question_idx]
        
        self.lbl_level.configure(text=f"Level {self.current_level_idx + 1}: {level_data['name']}")
        self.lbl_question.configure(text=question_data["question"])
        
        # Update progress bar
        total_questions = len(level_data["questions"])
        self.progress.set((self.current_question_idx) / total_questions)
        
        for i, option_text in enumerate(question_data["options"]):
            self.option_buttons[i].configure(text=option_text, state=ctk.NORMAL, fg_color="#F0F0F0", text_color="#1A237E")
            
        self.start_timer()

    def start_timer(self):
        if self.time_left > 0 and not self.answered:
            self.time_left -= 1
            self.lbl_timer.configure(text=f"⏳ {self.time_left}")
            self.timer_job = self.master.after(1000, self.start_timer)
        elif self.time_left == 0 and not self.answered:
            self.handle_time_up()

    def handle_time_up(self):
        self.answered = True
        try:
            winsound.Beep(300, 500)
        except:
            pass
        self.lbl_timer.configure(text="⏰ Time's Up!")
        self.show_fact_and_proceed("Time's Up! You got no points.")

    def use_lifeline(self):
        if self.answered or self.lifeline_used:
            return
            
        self.lifeline_used = True
        self.btn_lifeline.configure(state=ctk.DISABLED, fg_color="#A9A9A9", text="💡 Used")
        
        level_data = LEVELS[self.current_level_idx]
        question_data = level_data["questions"][self.current_question_idx]
        correct_ans = question_data["answer"]
        
        wrong_indices = [i for i, opt in enumerate(question_data["options"]) if opt != correct_ans]
        to_disable = random.sample(wrong_indices, 2)
        
        for idx in to_disable:
            self.option_buttons[idx].configure(text="---", state=ctk.DISABLED, fg_color="#E0E0E0", text_color="#A9A9A9")
            
        try:
            winsound.Beep(1200, 100)
            winsound.Beep(1500, 150)
        except:
            pass

    def check_answer(self, selected_idx):
        if self.answered: return
        self.answered = True
        
        if self.timer_job is not None:
            self.master.after_cancel(self.timer_job)
            self.timer_job = None
            
        self.btn_lifeline.configure(state=ctk.DISABLED, fg_color="#A9A9A9")
            
        level_data = LEVELS[self.current_level_idx]
        question_data = level_data["questions"][self.current_question_idx]
        selected_text = question_data["options"][selected_idx]
        
        for btn in self.option_buttons:
            btn.configure(state=ctk.DISABLED, text_color="#888888")
            
        if selected_text == question_data["answer"]:
            try:
                winsound.Beep(1000, 200)
                winsound.Beep(1500, 200)
            except:
                pass
            self.option_buttons[selected_idx].configure(fg_color="#4CAF50", text_color="white") 
            bonus = self.time_left * 2
            self.score += 10 + bonus
            self.lbl_score.configure(text=f"Score: {self.score}")
            feedback = f"✅ Correct! (+{10+bonus} pts)"
        else:
            try:
                winsound.Beep(400, 400)
            except:
                pass
            self.option_buttons[selected_idx].configure(fg_color="#F44336", text_color="white") 
            for idx, btn in enumerate(self.option_buttons):
                if question_data["options"][idx] == question_data["answer"]:
                    btn.configure(fg_color="#4CAF50", text_color="white")
            feedback = "❌ Incorrect!"
            
        self.show_fact_and_proceed(feedback)

    def show_fact_and_proceed(self, feedback_msg):
        question_data = LEVELS[self.current_level_idx]["questions"][self.current_question_idx]
        self.lbl_fact.configure(text=f"{feedback_msg}\n\nFact: {question_data['fact']}")
        self.btn_next.configure(state=ctk.NORMAL, fg_color="#0A7E07") 

    def next_question(self):
        self.current_question_idx += 1
        level_data = LEVELS[self.current_level_idx]
        
        if self.current_question_idx >= len(level_data["questions"]):
            self.current_level_idx += 1
            self.current_question_idx = 0
            if self.current_level_idx >= len(LEVELS):
                self.end_game()
            else:
                try:
                    winsound.Beep(800, 150)
                    winsound.Beep(1000, 150)
                    winsound.Beep(1200, 300)
                except:
                    pass
                messagebox.showinfo("Level Complete", f"Great job! Moving to Level {self.current_level_idx + 1}: {LEVELS[self.current_level_idx]['name']}")
                self.load_question()
        else:
            self.load_question()

    def end_game(self):
        try:
            winsound.Beep(600, 300)
            winsound.Beep(800, 300)
            winsound.Beep(1000, 500)
        except:
            pass
        
        save_score(self.player_name, self.score, self.current_level_idx)
        
        if self.current_level_idx >= len(LEVELS):
            try:
                from certificate import generate_certificate
                cert_path = generate_certificate(self.player_name, self.score, self.current_level_idx)
                messagebox.showinfo("Game Complete", f"Congratulations, {self.player_name}!\nYou completed the Swadeshi Quest.\nFinal Score: {self.score}\n\n🏆 A Certificate of Achievement has been saved to your Desktop!")
            except Exception as e:
                messagebox.showinfo("Game Complete", f"Congratulations, {self.player_name}!\nYou completed the Swadeshi Quest.\nFinal Score: {self.score}")
        else:
            messagebox.showinfo("Game Complete", f"Good effort, {self.player_name}!\nYou finished {self.current_level_idx} levels.\nFinal Score: {self.score}")
            
        self.quit_to_menu()

    def quit_to_menu(self):
        if self.timer_job is not None:
            self.master.after_cancel(self.timer_job)
        self.frame.destroy()
        self.on_finish()
