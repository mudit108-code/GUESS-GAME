import random

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def binary_search(min_value, max_value):
    target_number = generate_random_number(min_value, max_value)
    print(f"I'm thinking of a number between {min_value} and {max_value}. Can you guess it?")

    while True:
        guess = (min_value + max_value) // 2
        print("Is it", guess, "? (yes/no)")
        user_input = input().lower()

        if user_input == "yes":
            print("Great! I guessed your number. It's", guess)
            break
        elif user_input == "no":
            print("Is it higher or lower than", guess, "? (higher/lower)")
            hint = input().lower()

            if hint == "higher":
                min_value = guess + 1
            elif hint == "lower":
                max_value = guess - 1
            else:
                print("Please enter 'higher' or 'lower'.")
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    min_value = 1
    max_value = 100
    binary_search(min_value, max_value)
