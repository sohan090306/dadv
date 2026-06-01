import sqlite3

DB_NAME = "swadeshi_quest.db"

def init_db():
    """Initializes the database and creates the highscores table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS highscores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            score INTEGER NOT NULL,
            levels INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_score(player_name, score, levels):
    """Saves a player's score to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO highscores (player_name, score, levels)
        VALUES (?, ?, ?)
    ''', (player_name, score, levels))
    conn.commit()
    conn.close()

def get_top_scores(limit=10):
    """Retrieves the top N scores from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT player_name, score, levels FROM highscores
        ORDER BY score DESC, levels DESC
        LIMIT ?
    ''', (limit,))
    scores = cursor.fetchall()
    conn.close()
    return scores

# Initialize DB when the module is imported
init_db()
