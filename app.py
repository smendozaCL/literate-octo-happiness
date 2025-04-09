
import streamlit as st
import openai

# Securely load API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Ask My Assistant", page_icon="💬")
st.title("💬 Ask My Assistant")

# Custom assistant instructions
system_prompt = """
You are an expert support assistant trained to help users understand and use our educational tools. Always be clear, concise, and friendly. Your job is to explain product features, answer frequently asked questions, and provide guidance in an accessible tone.
"""

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

# Show history
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Type your question here...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=st.session_state.messages
            )
            reply = response["choices"][0]["message"]["content"]
            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
