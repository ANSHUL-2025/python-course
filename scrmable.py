import random

def scramble_word(word):
    """Scrambles the letters of a given word."""
    # Convert the word to a list of characters
    word_as_list = list(word)
    # Shuffle the list in place
    random.shuffle(word_as_list)
    # Join the shuffled characters back into a string
    return "".join(word_as_list)

# Example usage
original_word = "swathimam"
scrambled_version = scramble_word(original_word)
print(f"Original: {original_word}")
print(f"Scrambled: {scrambled_version}")