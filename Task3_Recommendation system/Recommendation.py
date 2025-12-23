movies = {
    "action": ["Mad Max", "John Wick", "Gladiator"],
    "comedy": ["The Mask", "Mr Bean", "Home Alone"],
    "romance": ["Titanic", "Notebook", "La La Land"],
    "horror": ["Conjuring", "Annabelle", "Insidious"]
}

print("Movie Recommendation System")
print("Available genres: Action, Comedy, Romance, Horror")

user_choice = input("Enter your favorite genre: ").lower()

if user_choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[user_choice]:
        print("-", movie)
else:
    print("Sorry, genre not found!")
