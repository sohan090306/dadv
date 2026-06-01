import sqlite3
import os

DATABASE_NAME = "swadeshi_quest.db"

def init_database():
    """Initialize the SQLite database"""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS highscores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL,
                levels INTEGER NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")

def save_score(player_name, score, levels):
    """Save player score to database"""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO highscores (player_name, score, levels)
            VALUES (?, ?, ?)
        ''', (player_name, score, levels))
        
        conn.commit()
        conn.close()
        print(f"Score saved for {player_name}: {score} points, {levels} levels")
    except Exception as e:
        print(f"Error saving score: {e}")

def get_leaderboard(limit=10):
    """Get top scores from database"""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT player_name, score, levels FROM highscores
            ORDER BY score DESC
            LIMIT ?
        ''', (limit,))
        
        scores = cursor.fetchall()
        conn.close()
        
        return scores if scores else []
    except Exception as e:
        print(f"Error fetching leaderboard: {e}")
        return []

def get_all_scores():
    """Get all scores from database"""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT player_name, score, levels, timestamp FROM highscores
            ORDER BY score DESC
        ''')
        
        scores = cursor.fetchall()
        conn.close()
        
        return scores if scores else []
    except Exception as e:
        print(f"Error fetching all scores: {e}")
        return []

def delete_all_scores():
    """Delete all scores (for testing purposes)"""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM highscores')
        conn.commit()
        conn.close()
        print("All scores deleted!")
    except Exception as e:
        print(f"Error deleting scores: {e}")
