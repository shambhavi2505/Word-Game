import random
import streamlit as st

# Word bank
word_bank = [
    'golgappa', 'momos', 'papdi_chaat', 'vada_pav', 'pav_bhaji',
    'chilli_chicken', 'noodles', 'biryani', 'litti', 'chicken_tikka',
    'burger', 'pasta', 'pizza', 'dosa', 'cheesecake', 'chole_kulche',
    'butter_chicken', 'brownie', 'rasmalai', 'bread_pakoda', 'popcorn'
]

# Hints
word_hints = {
    'golgappa': 'Crunchy & tangy street snack',
    'momos': 'Steamed or fried favorite',
    'papdi_chaat': 'Sweet, spicy, crispy combo',
    'vada_pav': 'Potato in a bun',
    'pav_bhaji': "Shubbu's favourite",
    'chilli_chicken': 'Spicy Indo-Chinese dish',
    'noodles': 'Long and slippery',
    'biryani': 'Fragrant rice meal',
    'litti': 'Stuffed wheat balls baked to perfection',
    'chicken_tikka': 'Grilled marinated pieces',
    'burger': 'Patty sandwiched in a bun',
    'pasta': 'Italian noodle dish',
    'pizza': 'Cheesy flatbread',
    'dosa': 'Crispy South Indian roll',
    'cheesecake': 'Creamy sweet slice',
    'chole_kulche': 'Spicy chickpeas with soft bread',
    'butter_chicken': 'Creamy tomato chicken',
    'brownie': 'Chocolatey square',
    'rasmalai': 'Soft sweet soaked in milk',
    'bread_pakoda': 'Deep-fried spiced bread snack',
    'popcorn': 'Puffy, crunchy cinema snack'
}

# Initialize session state
if 'word' not in st.session_state:
    st.session_state.word = random.choice(word_bank)
    st.session_state.word_lower = st.session_state.word.lower()
    st.session_state.hint = word_hints[st.session_state.word]
    st.session_state.guessWord = [' ' if c == '_' else '_' for c in st.session_state.word]
    st.session_state.attempts = 5
    st.session_state.guessed_letters = []

# Title and info
st.title("Word Guessing Game")
st.write(f"Hint: {st.session_state.hint}")
st.write(f"Attempts left: {st.session_state.attempts}")
st.write('Current word: ' + ' '.join(st.session_state.guessWord))

# Function to handle guess submission
def process_guess():
    guess = st.session_state.input_guess.lower()
    st.session_state.input_guess = ""  # Clear input safely
    if len(guess) != 1:
        st.warning("Please enter only a single letter.")
    elif guess in st.session_state.guessed_letters:
        st.warning(f"You already guessed '{guess}'. Try another letter.")
    else:
        st.session_state.guessed_letters.append(guess)
        if guess in st.session_state.word_lower:
            for i, char in enumerate(st.session_state.word_lower):
                if char == guess:
                    st.session_state.guessWord[i] = st.session_state.word[i]
            st.success("Great guess!")
        else:
            st.session_state.attempts -= 1
            st.error(f"Wrong guess! Attempts left: {st.session_state.attempts}")

# Input box with callback
st.text_input("Guess a letter:", key="input_guess", max_chars=1, on_change=process_guess)

# Check win/loss
if '_' not in st.session_state.guessWord:
    st.success(f"Congrats! You guessed the word correctly: {st.session_state.word.replace('_',' ')}")
elif st.session_state.attempts == 0:
    st.error(f"You've run out of attempts! The word was: {st.session_state.word.replace('_',' ')}")


