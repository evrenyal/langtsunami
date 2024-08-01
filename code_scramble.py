import random
import json

def scramble_word_order(text, language):
    """Scramble the order of words or characters in the text based on the language."""
    if language == "Chinese":
        chars = list(text)  # Treat each character as an individual element
        random.shuffle(chars)  # Shuffle the characters
        return ''.join(chars)  # Join shuffled characters back into text
    else:
        words = text.split()  # Split text into words
        random.shuffle(words)  # Shuffle the order of words
        return ' '.join(words)  # Join shuffled words back into text

def scramble_text_multiple_times(text, times, language):
    """Scramble the text multiple times and return the results."""
    results = []
    for _ in range(times):
        scrambled_text = scramble_word_order(text, language)
        results.append(scrambled_text)
    return results

# Load texts from translations.json
with open('translations.json', 'r', encoding='utf-8') as file:
    texts = json.load(file)

# Number of iterations
iterations = 3

# Dictionary to store the scrambled texts
payloads = {}

# Scramble texts and store results in payloads dictionary
for lang, text in texts.items():
    print(f"\n{lang}:")
    scrambled_versions = scramble_text_multiple_times(text, iterations, lang)
    for i, scrambled in enumerate(scrambled_versions, 1):
        print(f"Iteration {i}: {scrambled}")
        payloads[f"{lang}_iteration_{i}"] = scrambled

# Save the payloads dictionary to a JSON file
with open('results/code_scramble.json', 'w', encoding='utf-8') as f:
    json.dump(payloads, f, ensure_ascii=False, indent=4)

