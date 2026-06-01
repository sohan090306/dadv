# Swadeshi Quest - Setup & Run Guide

## Project Overview
**Swadeshi Quest: Journey Towards Atmanirbhar Bharat** is an interactive Python-based educational game designed to foster awareness and appreciation for Indian culture, heritage, and the "Made in India" initiative.

## Features
- **5-Level Progression System**: Indian States → Freedom Fighters → Festivals → Swadeshi Products → Traditional Games
- **Interactive GUI**: Built with Tkinter, featuring Indian flag-themed colors
- **Time-Based Challenges**: 15-second countdown timer for each question
- **Dynamic Scoring & Leaderboard**: Tracks top 10 high scores using SQLite
- **Educational Feedback**: Interesting facts with each question

## System Requirements
- **Python**: 3.8 or higher
- **OS**: Windows, Linux, or macOS
- **RAM**: Minimum 2GB
- **Storage**: 50MB free space

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/sohan090306/dadv.git
cd dadv
```

### 2. Install Python (if not already installed)
- Download from: https://www.python.org/downloads/
- Ensure Python 3.8+ is installed

### 3. Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Game

### Start the Game
```bash
python main.py
```

## Project Structure
```
dadv/
├── main.py              # Welcome screen and game launcher
├── game.py              # Game logic and question display
├── levels.py            # Question data for all 5 levels
├── database.py          # Database operations for leaderboard
├── requirements.txt     # Python dependencies
├── index.html           # GitHub Pages welcome page
├── dadv/
│   └── README.md        # Project documentation
└── README_SETUP.md      # This file
```

## How to Play

1. **Welcome Screen**: Launch the application and select "Start Game"
2. **Register**: Enter your player name
3. **Game Flow**:
   - Answer 5 questions per level
   - Each question has 15 seconds
   - Correct answer = +10 points
   - 5 Levels total
4. **Scoring**: 
   - Maximum score: 250 points (5 levels × 5 questions × 10 points)
   - View leaderboard after each game
5. **Complete the Game**: Play all 5 levels and see your final score

## Levels Overview

### Level 1: Indian States
- Questions about Indian states and their capitals
- Learn geography and state information

### Level 2: Freedom Fighters
- Questions about Indian independence leaders
- Understand India's struggle for freedom

### Level 3: Indian Festivals
- Questions about traditional celebrations
- Appreciate India's cultural diversity

### Level 4: Swadeshi Products
- Questions about Indian-made products and crafts
- Support the "Make in India" initiative

### Level 5: Traditional Games
- Questions about Indian heritage games and sports
- Learn about ancient gaming traditions

## Features Explained

### Leaderboard
- View top 10 high scores
- Scores are saved to SQLite database
- Persistent across sessions

### Timer System
- 15 seconds per question
- Visual countdown display
- Auto-submit on timeout (marked as wrong)

### Scoring System
- Correct answer: +10 points
- Wrong answer: 0 points
- Total possible: 250 points

## Troubleshooting

### Error: ModuleNotFoundError: No module named 'tkinter'
**Solution**: tkinter is usually included with Python. On Linux:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

### Error: No module named 'customtkinter'
**Solution**: Install dependencies again:
```bash
pip install -r requirements.txt
```

### Database file not created
**Solution**: The database is auto-created on first run. Ensure you have write permissions in the project directory.

## Features Coming Soon

- Multiplayer support (local network)
- Online leaderboards (cloud database)
- AI-generated dynamic questions
- Voice-based interaction
- Mobile application (Kivy/React Native)

## Contributing

To contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available for educational purposes.

## Contact & Support

For issues, suggestions, or feedback:
- GitHub: https://github.com/sohan090306/dadv
- Report issues in the GitHub Issues section

## Credits

Created as part of the "Student Innovation: Swadeshi for Atmanirbhar Bharat" initiative to promote awareness of Indian culture and heritage through interactive gaming.

---

**Jai Bharat! Happy Playing! 🇮🇳**
