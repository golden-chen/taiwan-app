import streamlit as st


#st.markdown("# main ❄️")
st.sidebar.markdown("# Taiwan story ❄️")
st.title("🎈 Taiwan story")
st.write(
    "Let's start discovering! For wonderful and nice, head over to [Taiwan](https://tw.yahoo.com)."
)
st.write(
    "Let's test again!"
)
s1_pg = st.Page("pages/story-1.py", title="story-1", icon=":material/coffee:")
s2_pg = st.Page("pages/story-2.py", title="story-2", icon=":material/deer:")
s3_pg = st.Page("pages/story-3.py", title="story-3", icon=":material/bat:")
test_pg = st.Page("pages/test.py", title="test", icon=":material/dragon:")

pg = st.navigation([s1_pg,s2_pg,s3_pg,test_pg])
st.set_page_config(page_title="home", page_icon=":material/home:")
pg.run()
