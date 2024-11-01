import streamlit as st
st.session_state['Golden']='best'
st.session_state['terry']='weak'
st.session_state['length']=31
st.session_state['SWITCH']=True
"Before of test",st.session_state
st.markdown("# Story-2 ❄️")
st.session_state.Golden='The best'
st.session_state['terry']='bad'
st.session_state.length=39
st.session_state['SWITCH']=False
"After of test",st.session_state
st.sidebar.markdown("# Story-2 ❄️")
st.image("./static/b2.jpg", caption="Sunrise by the mountains")
