import streamlit as st
from src.password_generators import PinGenerator,RandomPasswordGenerator,MemorablePasswordGenerator

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWY19wMEiv_r2tuxU87CT3pkEkfnh7CO9q7UoHsAP31A&s=10', width= 550)
st.title(':zap: Password Generators :zap:')

option = st.radio(
    'select a password generator',
    ('PinGenerator','RandomPasswordGenerator','MemorablePasswordGenerator')
)

if option == 'PinGenerator':
    length = st.slider('Select the length of the Pin code',4,32,8)
    
    generator = PinGenerator(length)
    
elif option == 'RandomPasswordGenerator':
    length = st.slider('Select the length of Password',8,100,32)
    include_symbol = st.toggle('Include Symbols')
    include_number = st.toggle('Include Number')
    
    generator = RandomPasswordGenerator(length, include_symbol, include_number)
    
elif option == 'MemorablePasswordGenerator':
     num_of_words = st.slider('Select the Number of Words',4,10,3)
     Seperator = st.text_input('Seperator',value= '-')
     Capitalization = st.toggle('Capitalization')
     
     generator = MemorablePasswordGenerator(num_of_words, Seperator, Capitalization )
     
password = generator.generate()
st.write(fr'Your password is: `{password}`')