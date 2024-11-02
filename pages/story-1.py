import streamlit as st
c1,c2,c3=st.columns([3,1,2])
c1.number_input('weight', value=40, step=1,key='w')
c3.slider('Length',1,200, value=150,key='l')
st.session_state
st.markdown("# Story-1 ❄️")
st.sidebar.markdown("# Stoory-1 ❄️")
st.image("./static/b1.png", caption="Super star")
