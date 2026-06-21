# Simple AI Recommendation System (Project 3)

# 1. Dataset (Items with categories)
items = {
    "Interstellar": ["sci-fi", "space", "drama"],
    "The Notebook": ["romance", "drama"],
    "Avengers": ["action", "superhero"],
    "Inception": ["sci-fi", "thriller"],
    "Titanic": ["romance", "drama"],
    "Batman": ["action", "superhero"],
}

# 2. Take user preferences
user_input = input("Enter your interests (comma separated): ")


user_preferences = [x.strip().lower() for x in user_input.split(",")]

# 3. Function to calculate similarity
def get_score(user_prefs, item_tags):
    score = 0
    for tag in item_tags:
        if tag in user_prefs:
            score += 1
    return score

# 4. Recommendation logic
recommendations = []

for item, tags in items.items():
    score = get_score(user_preferences, tags)
    if score > 0:
        recommendations.append((item, score))

# 5. Sort results (best match first)
recommendations.sort(key=lambda x: x[1], reverse=True)

# 6. Output
print("\nRecommended Items for you:\n")

if recommendations:
    for item, score in recommendations:
        print(f"{item} (match score: {score})")
else:
    print("No recommendations found. Try different interests!")