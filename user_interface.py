import streamlit as st

# page configuration
st.set_page_config(
    page_title="AI Writing Assistant",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ AI Writing Assistant")
st.subheader("Generate professional content in seconds")
st.markdown('---')

# select content type and get user input
content_type=st.selectbox(' 📝 Select Content Type', ['-- Select a content type --','Blog Introduction', 'Twitter Post', 'Professional Email', 'LinkedIn Post'], index = 0)
user_input = st.text_input("💡 Topic ", placeholder="Enter your topic here...")

# generate content button
st.markdown("")
clicked =st.button('✨ Generate ')


if clicked:
    # if generated button is cliked and gets by default content type, it shows error and warning message
    if content_type == '-- Select a content type --':
        st.error("⚠️ Please select a content type first!")
    # if generated button is clicked but user input is empty, it show an erro message
    elif not user_input:
        st.error("⚠️ Please enter a topic to generate content!")
    # if generated button is clicked and content type and user input are valid, it shows the generated content
    else:
        st.markdown('---')
        st.subheader('📄 Generated Content')
        st.code(user_input, language=None)
        st.success("✅ Content generated successfully!")