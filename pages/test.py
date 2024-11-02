import streamlit as st
import pandas as pd
st.markdown("# test ❄️")
st.sidebar.markdown("# test ❄️")
st.title('Counter Example using Callbacks')
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1

st.button('Increment', on_click=increment_counter)

st.write('Count = ', st.session_state.count)
st.markdown("#  ❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄")
st.title('Counter Example using Callbacks with args')
if 'count1' not in st.session_state:
    st.session_state.count1 = 0

increment_value = st.number_input('Enter a value', value=0, step=1)

def increment_counter1(increment_value):
    st.session_state.count1 += increment_value

increment = st.button('Add', on_click=increment_counter1,
    args=(increment_value, ))

st.write('Count = ', st.session_state.count1)
