# Swadeshi Quest: Journey Towards Atmanirbhar Bharat

**Theme:** Student Innovation: Swadeshi for Atmanirbhar Bharat – Toys & Games

## Abstract
"Swadeshi Quest: Journey Towards Atmanirbhar Bharat" is an interactive, Python-based educational game designed to foster awareness and appreciation for Indian culture, heritage, and the "Made in India" initiative. In an era dominated by foreign products and digital media, this project aims to reconnect the youth with traditional Indian roots, freedom fighters, and indigenous products (Swadeshi). Built using Python's Tkinter for a rich graphical interface and SQLite for persistent score tracking, the game takes players through five distinct educational levels. It serves as a perfect blend of modern programming concepts and cultural education, making it an ideal model for engineering exhibitions and innovation hackathons.

## Problem Statement
With the rapid globalization and influx of imported toys and digital games, today's students are increasingly disconnected from India's rich historical heritage, traditional games, and the ethos of self-reliance (Atmanirbhar Bharat). There is a critical need for engaging, interactive educational platforms that promote Swadeshi ideas and educate the youth about their cultural roots in a fun and modern way.

## Objectives
- To develop an interactive educational game promoting the "Made in India" initiative.
- To educate players about Indian states, freedom fighters, festivals, and traditional games.
- To implement a modular Python application showcasing Object-Oriented Programming, GUI design, and database management.
- To provide a visually appealing, competitive environment with leaderboards and timers to encourage replayability.

## Scope
The project focuses on creating a desktop-based GUI application for Windows/Linux/Mac. It covers five distinct educational domains related to India. The current scope includes local single-player gameplay, local database storage, and integrated sound effects.

## Features
- **5-Level Progression System:** Increasing difficulty across States, Freedom Fighters, Festivals, Swadeshi Products, and Traditional Games.
- **Interactive GUI:** Built with Tkinter, featuring Indian flag-themed colors, progress bars, and transition screens.
- **Time-Based Challenges:** Countdown timers for each question to increase engagement.
- **Dynamic Scoring & Leaderboard:** Tracks player scores using an SQLite database and displays the Top 10 High Scores.
- **Audio Feedback:** Sound effects for correct answers, wrong answers, and level completions.
- **Educational Feedback:** Provides interesting facts and correct answers upon incorrect selections.

## Software Requirements
- **Programming Language:** Python 3.8 or higher
- **Libraries:** `customtkinter` (modern UI), `sqlite3` (built-in), `winsound` (built-in on Windows for audio)
- **Database:** SQLite
- **OS:** Windows (Recommended for audio features), Linux, macOS

## Hardware Requirements
- **Processor:** Intel Core i3 or equivalent (minimum)
- **RAM:** 4 GB (minimum)
- **Storage:** 50 MB free space
- **Display:** Minimum 1024x768 resolution

## System Architecture
The system follows a modular architecture divided into UI Presentation, Game Logic, and Data Access layers:
1. **main.py (Presentation):** Handles the Welcome screen, Player Registration, and navigation.
2. **game.py (Logic):** Manages the game loop, timer, score calculation, and level transitions.
3. **levels.py (Data):** Serves as the localized data model containing questions, options, and answers.
4. **database.py (Data Access):** Interfaces with the SQLite database to store and retrieve player statistics.

## Flowchart Description
1. **Start:** Application launched (`main.py`).
2. **Welcome Screen:** Display Title, Start, High Scores, Instructions, Exit.
3. **Input:** Player enters name.
4. **Game Initialization:** Connect to DB, load Level 1 questions.
5. **Question Loop:**
   - Display Question & Options.
   - Start Timer.
   - **Condition (Answer Correct?):**
     - Yes -> Play Success Sound, Add Points.
     - No -> Play Error Sound, Show Correct Answer Fact.
   - **Condition (Time Up?):**
     - Yes -> Mark as wrong.
6. **Level Check:** If questions in level complete, move to Next Level.
7. **End Game (Level 5 complete):** Save Name & Score to SQLite DB.
8. **Leaderboard:** Display Top 10 scores.
9. **Exit.**

## Database Design
**Database Name:** `swadeshi_quest.db`
**Table Name:** `highscores`

| Column Name | Data Type | Constraints             | Description                        |
|-------------|-----------|-------------------------|------------------------------------|
| `id`        | INTEGER   | PRIMARY KEY AUTOINCREMENT | Unique identifier for each entry.  |
| `player_name`| TEXT      | NOT NULL                | Name of the player.                |
| `score`     | INTEGER   | NOT NULL                | Total score achieved.              |
| `levels`    | INTEGER   | NOT NULL                | Number of levels completed (up to 5)|

## Testing Methodology
- **Unit Testing:** Individual testing of the SQLite connection and insert/fetch functions in `database.py`.
- **Integration Testing:** Ensuring the transition from `main.py` to `game.py` passes the player name correctly.
- **Functional Testing:** Verifying the timer stops when an answer is clicked, and scores are calculated accurately.
- **UI/UX Testing:** Ensuring colors map to the Indian theme (Saffron, White, Green, Navy Blue) and text is readable.

## Conclusion
"Swadeshi Quest" successfully demonstrates how programming and technology can be leveraged to promote cultural awareness and the Atmanirbhar Bharat initiative. It serves as a comprehensive educational tool that is both entertaining and informative, wrapping historical and cultural facts within a competitive gaming framework.

## Future Enhancements
- **Multiplayer Support:** Allow head-to-head trivia battles over a local network.
- **Online Leaderboards:** Migrate from local SQLite to a cloud database (e.g., Firebase) for global high scores.
- **AI-Generated Quizzes:** Integrate LLM APIs to dynamically generate new questions about India to ensure endless gameplay.
- **Voice-Based Interaction:** Implement Speech-to-Text for answering questions without a keyboard/mouse.
- **Mobile Application:** Port the game to Android/iOS using frameworks like Kivy or React Native.
