import random

def get_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't programmers like nature? It has too many bugs.",
        "Why do we tell actors to 'break a leg?' Because every play has a cast.",
        "I am Billionaire Mafia.",
        "Why did the math book look sad? Because it had too many problems.",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "Why did the bicycle fall over? Because it was two tired!",
        "How does a penguin build its house? Igloos it together.",
        "Why can't you trust stairs? They're always up to something."
    ]
    return random.choice(jokes)

def main():
    print("="*60)
    print("           Welcome to the Random Joke Generator!")
    print("="*60)
    print("Press Enter to get a joke or type 'q' and Enter to quit.\n")
    
    while True:
        user_input = input("Your choice: ").strip().lower()
        if user_input == 'q':
            print("\nThanks for using the Random Joke Generator. Goodbye!")
            break
        joke = get_random_joke()
        print("\n😄  " + joke + "\n")
        print("-"*60)

if __name__ == "__main__":
    main()

