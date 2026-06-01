def get_level_questions(level):
    """Returns questions for each level"""
    
    questions = {
        1: [  # Indian States
            {
                "question": "Which is the capital of India?",
                "options": ["Mumbai", "Delhi", "Bangalore", "Kolkata"],
                "answer": "Delhi",
                "fact": "Delhi has been the capital of India since 1947."
            },
            {
                "question": "Which state is known as the 'God's Own Country'?",
                "options": ["Tamil Nadu", "Kerala", "Karnataka", "Goa"],
                "answer": "Kerala",
                "fact": "Kerala is famous for its backwaters, beaches, and natural beauty."
            },
            {
                "question": "Which is the largest state in India by area?",
                "options": ["Maharashtra", "Rajasthan", "Uttar Pradesh", "Madhya Pradesh"],
                "answer": "Rajasthan",
                "fact": "Rajasthan is a vast desert state covering about 10.2% of India's area."
            },
            {
                "question": "What is the capital of Maharashtra?",
                "options": ["Pune", "Mumbai", "Nagpur", "Aurangabad"],
                "answer": "Mumbai",
                "fact": "Mumbai is the financial capital of India and home to Bollywood."
            },
            {
                "question": "Which state is located in the northeastern part of India?",
                "options": ["Punjab", "Assam", "Rajasthan", "Gujarat"],
                "answer": "Assam",
                "fact": "Assam is famous for its tea gardens and one-horned rhinoceros."
            },
        ],
        2: [  # Freedom Fighters
            {
                "question": "Who is known as the 'Father of the Nation'?",
                "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", "Subhas Chandra Bose"],
                "answer": "Mahatma Gandhi",
                "fact": "Mahatma Gandhi led India's independence through non-violent resistance."
            },
            {
                "question": "Which freedom fighter said 'Inquilab Zindabad'?",
                "options": ["Bhagat Singh", "Chandrashekhar Azad", "Khudiram Bose", "Rajendra Prasad"],
                "answer": "Bhagat Singh",
                "fact": "Bhagat Singh was a revolutionary who fought for Indian independence as a young freedom fighter."
            },
            {
                "question": "Who is known as the 'Iron Man of India'?",
                "options": ["Ambedkar", "Patel", "Tilak", "Gokhale"],
                "answer": "Patel",
                "fact": "Sardar Vallabhbhai Patel unified India and is also called the 'Bismarck of India'."
            },
            {
                "question": "Who founded the Indian National Congress?",
                "options": ["Allan Hume", "Raj Mohan Roy", "Keshab Chandra Sen", "Rammohan Roy"],
                "answer": "Allan Hume",
                "fact": "Allan Hume, a British official, founded the Indian National Congress in 1885."
            },
            {
                "question": "Which freedom fighter led the Quit India Movement?",
                "options": ["Netaji Subhas Chandra Bose", "Mahatma Gandhi", "Jawaharlal Nehru", "Lal Bahadur Shastri"],
                "answer": "Mahatma Gandhi",
                "fact": "The Quit India Movement of 1942 was a mass civil disobedience movement."
            },
        ],
        3: [  # Indian Festivals
            {
                "question": "Which festival is known as the 'Festival of Lights'?",
                "options": ["Holi", "Diwali", "Navratri", "Eid"],
                "answer": "Diwali",
                "fact": "Diwali celebrates the victory of light over darkness and good over evil."
            },
            {
                "question": "Holi is celebrated by throwing which colored powder?",
                "options": ["Water", "Colored Powder", "Flour", "Colored Oil"],
                "answer": "Colored Powder",
                "fact": "Holi celebrates the arrival of spring and the victory of good over evil."
            },
            {
                "question": "Which festival marks the harvest season in India?",
                "options": ["Pongal", "Diwali", "Holi", "Navratri"],
                "answer": "Pongal",
                "fact": "Pongal is celebrated in January as a harvest festival, especially in South India."
            },
            {
                "question": "Navratri celebrates the victory of the goddess over which demon?",
                "options": ["Ravana", "Mahishasura", "Kumbhakarna", "Hiranyakashyap"],
                "answer": "Mahishasura",
                "fact": "Navratri celebrates the victory of Goddess Durga over the buffalo demon Mahishasura."
            },
            {
                "question": "Which festival is celebrated by lighting lanterns and flying kites?",
                "options": ["Diwali", "Makar Sankranti", "Holi", "Onam"],
                "answer": "Makar Sankranti",
                "fact": "Makar Sankranti marks the sun's transition and is celebrated with kite flying."
            },
        ],
        4: [  # Swadeshi Products
            {
                "question": "Which Indian textile is famous worldwide for its intricate designs?",
                "options": ["Cotton", "Silk", "Khadi", "Wool"],
                "answer": "Khadi",
                "fact": "Khadi is a handspun and handwoven fabric promoted by Gandhi as a symbol of swadeshi."
            },
            {
                "question": "Which Indian spice is known as 'Black Gold'?",
                "options": ["Turmeric", "Black Pepper", "Cumin", "Cardamom"],
                "answer": "Black Pepper",
                "fact": "Black pepper is native to India and was historically called 'black gold' due to its value."
            },
            {
                "question": "Which Indian handicraft is known for its colorful pottery and design?",
                "options": ["Blue Pottery", "Bamboo Craft", "Stone Carving", "Brass Work"],
                "answer": "Blue Pottery",
                "fact": "Blue Pottery of Jaipur is a beautiful traditional craft with Persian influence."
            },
            {
                "question": "Which Indian state is famous for its diamond polishing industry?",
                "options": ["Rajasthan", "Gujarat", "Maharashtra", "Tamil Nadu"],
                "answer": "Gujarat",
                "fact": "Gujarat processes about 90% of the world's diamonds."
            },
            {
                "question": "Which Indian fruit is known as the 'King of Fruits'?",
                "options": ["Apple", "Mango", "Banana", "Orange"],
                "answer": "Mango",
                "fact": "India is the world's largest producer of mangoes, producing over 20 million tons annually."
            },
        ],
        5: [  # Traditional Games
            {
                "question": "Which traditional Indian game is played with colored discs?",
                "options": ["Carrom", "Kabaddi", "Kho-Kho", "Ludo"],
                "answer": "Carrom",
                "fact": "Carrom is a traditional strike-based game played on a board with pockets."
            },
            {
                "question": "What is the traditional Indian rope game called?",
                "options": ["Hopscotch", "Kabaddi", "Kite Flying", "Skipping"],
                "answer": "Skipping",
                "fact": "Traditional skipping games have been played in India for centuries."
            },
            {
                "question": "Which team game involves chasing and tagging?",
                "options": ["Carrom", "Kho-Kho", "Ludo", "Pachisi"],
                "answer": "Kho-Kho",
                "fact": "Kho-Kho is a traditional Indian team sport that dates back centuries."
            },
            {
                "question": "Which traditional Indian board game is the ancestor of modern Ludo?",
                "options": ["Ashta Chamma", "Chaupar", "Pachisi", "Vyavahara"],
                "answer": "Pachisi",
                "fact": "Pachisi is an ancient Indian board game that inspired modern Ludo."
            },
            {
                "question": "What is the name of the traditional Indian wrestling style?",
                "options": ["Karate", "Kung Fu", "Kushti", "Muay Thai"],
                "answer": "Kushti",
                "fact": "Kushti is a traditional form of wrestling practiced in India for centuries."
            },
        ]
    }
    
    return questions.get(level, [])
