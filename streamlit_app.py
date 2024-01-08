import streamlit as st
import openai

# Set up the page
st.title('GPT-4 Chatbot with OpenAI')

# Sidebar for API key input
with st.sidebar:
    openai_api_key = st.text_input("Enter your OpenAI API key", type="password")

# Check if the API key is entered
if not openai_api_key:
    st.warning("Please enter your OpenAI API key in the sidebar to continue.")
    st.stop()

# Setting OpenAI API key
openai.api_key = openai_api_key

# Chat UI
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

user_input = st.text_input("You: ", key="user_input")

if st.button("Send"):
    st.session_state['messages'].append("You: " + user_input)
    try:
        # Call to OpenAI's API
        response = openai.Completion.create(
          model="gpt-4.0-turbo",  # Specify GPT-4 here
          prompt=user_input,
          max_tokens=150
        )
        reply = response.choices[0].text.strip()
        st.session_state['messages'].append("Bot: " + reply)
    except Exception as e:
        st.error(f"Error in calling OpenAI API: {str(e)}")

# Display chat history
for message in st.session_state['messages']:
    st.text(message)
