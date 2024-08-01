import spacy
import nltk
from nltk.tokenize import word_tokenize
import string
import json

# Download necessary data for NLTK
nltk.download('punkt')

# Load Chinese language model
nlp_zh = spacy.load("zh_core_web_sm")

# Leetspeak dictionary
leet_dict = {
    'a': '4', 'e': '3', 'g': '6', 'i': '1', 'o': '0',
    's': '5', 't': '7', 'b': '8', 'l': '1'
}

# Load texts from translations.json
with open('translations.json', 'r', encoding='utf-8') as file:
    texts = json.load(file)

# Tokenize function using spacy for Chinese and nltk for other languages
def tokenize_text(text, language):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    if language == "Chinese":
        doc = nlp_zh(text)
        tokens = [token.text for token in doc]
    else:
        tokens = word_tokenize(text)
    return tokens

# Tokenize all texts
tokenized_texts = {lang: tokenize_text(text, lang) for lang, text in texts.items()}

# Function to replace a word with its leetspeak representation
def word_to_leet(word):
    return ''.join([leet_dict[char] if char in leet_dict else char for char in word.lower()])

# Function to create code-switched sentences
def create_code_switched_sentences():
    all_code_switched_sentences = {}
    
    # Iterate through each language as the base language
    for base_lang, base_tokens in tokenized_texts.items():
        for target_lang, target_tokens in tokenized_texts.items():
            if base_lang != target_lang:
                for i, target_token in enumerate(target_tokens):
                    leet_target_token = word_to_leet(target_token)
                    for j, base_token in enumerate(base_tokens):
                        new_tokens = base_tokens.copy()
                        new_tokens[j] = leet_target_token
                        code_switched_sentence = ' '.join(new_tokens)
                        key = f"{base_lang}-to-{target_lang}-word-{i+1}-base-{j+1}"
                        all_code_switched_sentences[key] = code_switched_sentence
    
    return all_code_switched_sentences

# Generate code-switched sentences
code_switched_sentences = create_code_switched_sentences()

# Print JSON outputs
json_output = json.dumps(code_switched_sentences, ensure_ascii=False, indent=4)
print(json_output)

with open('results/code_switch_leetcode.json', 'w', encoding='utf-8') as f:
    f.write(json_output)