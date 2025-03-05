import streamlit as st
import random
import string

def generate_pass(lth, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for i in range(lth))

st.title('Password Generator 🐱‍💻')
length = st.slider('Enter Password\'s Length', min_value = 4, max_value = 100, value = 24)
use_digits = st.checkbox('Use numbers in password')
use_special = st.checkbox('Use special characters in password')

if st.button('Generate Password'):
    st.subheader('Password:')
    st.text(generate_pass(length, use_digits, use_special))

st.write('---')
st.write('Built by Uzair Bin Asif, follow / connect on [Github](https://github.com/UzairBinAsif)\
    and [LinkedIn](https://www.linkedin.com/in/uzair-bin-asif-a6782529a/) 🙂')