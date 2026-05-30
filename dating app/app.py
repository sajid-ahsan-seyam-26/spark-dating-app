import random
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Expanded profiles data
PROFILES = [
    {
        "id": 1,
        "name": "Anika",
        "age": 22,
        "bio": "Love coffee, progressive metal music, and coding in Python.",
        "image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400"
    },
    {
        "id": 2,
        "name": "Zayan",
        "age": 24,
        "bio": "Competitive programmer by day, gamer by night. Let's grab some food.",
        "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400"
    },
    {
        "id": 3,
        "name": "Nova",
        "age": 23,
        "bio": "Anime enthusiast and UI/UX designer. Looking for someone to vibe with.",
        "image": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400"
    },
    {
        "id": 4,
        "name": "Sajid",
        "age": 22,
        "bio": "Building a voice assistant named Jarvis. Big fan of Artcell.",
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400"
    },
    {
        "id": 5,
        "name": "Esha",
        "age": 21,
        "bio": "Web developer exploring semantic HTML and CSS art. Tea lover.",
        "image": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400"
    },
    {
        "id": 6,
        "name": "Tahmid",
        "age": 25,
        "bio": "Data analyst playing around with NumPy arrays. Tech enthusiast.",
        "image": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=400"
    }
]

# Simple in-memory list to store actual matches during the session
MATCHES = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/profiles')
def get_profiles():
    return jsonify(PROFILES)

# New Feature: Handle swipe logic and check for a match
@app.route('/api/swipe', methods=['POST'])
def swipe():
    data = request.json
    profile_id = data.get('id')
    action = data.get('action') # 'like' or 'dislike'
    
    is_match = False
    matched_profile = None
    
    if action == 'like':
        # Simulating a 50% chance that they liked you back!
        is_match = random.choice([True, False])
        if is_match:
            # Find the profile details to save into matches
            for profile in PROFILES:
                if profile['id'] == profile_id:
                    matched_profile = profile
                    if profile not in MATCHES:
                        MATCHES.append(profile)
                    break
                    
    return jsonify({
        "success": True,
        "is_match": is_match,
        "matched_with": matched_profile
    })

# New Feature: API to fetch all successfully matched people
@app.route('/api/matches')
def get_matches():
    return jsonify(MATCHES)

if __name__ == '__main__':
    app.run(debug=True)