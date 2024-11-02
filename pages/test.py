import streamlit as st
import pandas as pd
st.markdown("# test ❄️")
st.sidebar.markdown("# test ❄️")
st.title('Counter Example using Callbacks')
if 'count' not in st.session_state:
    st.session_state.count = 0
col=st.columns(2)
def increment_counter():
    st.session_state.count += 1

col[0].button('Increment', on_click=increment_counter)
#c2.title('Count = ', st.session_state.count)
col[1].text('Count = '+ str(st.session_state.count))
st.markdown("###  ❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄")
st.title('Counter Example using Callbacks with args')
if 'count1' not in st.session_state:
    st.session_state.count1 = 0
c3,c4,c5=st.colummns([3,3,3])
increment_value = c3.number_input('Enter a value', value=0, step=1)

def increment_counter1(increment_value):
    st.session_state.count1 += increment_value

increment = c4.button('Add', on_click=increment_counter1,
    args=(increment_value, ))

c5.write('Count = ', st.session_state.count1)
