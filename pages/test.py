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
#---------------------------------------------------
st.divider()
st.title('Counter Example using Callbacks with args')
if 'count1' not in st.session_state:
    st.session_state.count1 = 0
c3,c4,c5,c6=st.columns([3,2,2,2])
increment_value = c3.number_input('Enter a value', value=0, step=1)

def add_counter1(increment_value):
    st.session_state.count1 += increment_value
def sub_counter1(increment_value):
    st.session_state.count1 -= increment_value
increment = c4.button('Add', on_click=add_counter1,
    args=(increment_value, ))
increment = c5.button('Sub', on_click=sub_counter1,
    args=(increment_value, ))
c6.text('Count1 = '+str(st.session_state.count1))
#-----------------------------------------------------
st.divider()
st.title('test dialog')
st.button('dialog',on_click=tvote)
def tvote():
    @st.dialog("Cast your vote")
    def vote(item):
        st.write(f"Why is {item} your favorite?")
        reason = st.text_input("Because...")
        if st.button("Submit"):
            st.session_state.vote = {"item": item, "reason": reason}
            st.rerun()
    
    if "vote" not in st.session_state:
        st.write("Vote for your favorite")
        if st.button("A"):
            vote("A")
        if st.button("B"):
            vote("B")
    else:
        f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
#--------------------------------------------------------    
st.divider()
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")
