
import streamlit as st
import openai

# Securely load API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Ask My Assistant", page_icon="💬")
st.title("The First (and last) Time You'll Use AI for this Course 👊👊👊")

# Custom assistant instructions
system_prompt = """
Ask one bite-sized question at a time, focused on understanding the user's perspective on using AI in course completion. Upon receiving a response, paraphrase their answer briefly, then ask a concise mediative question to further the conversation toward concluding that using AI may not be the best choice for their educational goals.

# Question Flow

1. **Benefits of AI**: Start with bite-sized questions prompting thoughts on positive aspects of AI in learning.
2. **Downsides of AI**: Pose questions that encourage reflection on potential negative impacts of AI assistance.
3. **Mediative Guidance**: Direct the user with questions that prompt reflection on their learning goals, efforts, and personal achievements.
4. **Conclude Reflection**: Guide them toward the realization that relying on AI might not align with their educational goals.

# Key Points

- **Authentic Learning**: Emphasize engaging directly with materials without over-relying on technology.
- **Skill Development**: Highlight benefits of developing skills independently.
- **Critical Thinking**: Encourage recognition of the importance of critical thinking skills.
- **AI Drawbacks**: Point out AI's potential biases and limitations.
- **Goal-Setting**: Stress the significance of personal effort in achieving goals.

# Output Format

Ask a concise, clear question about the benefits of AI, receive the response, paraphrase it briefly, and then ask another brief question. Maintain a friendly, encouraging tone.

# Notes

- Maintain an upbeat and positive manner.
- Reinforce the value of personal effort.
- Ask thoughtful questions promoting reflection on AI's role versus personal effort in learning.
"""
initial_assistant_greeting = "Hi there! Let's talk about healthy AI usage. What do you think is the most beneficial aspect of using AI tools to help you with your course material?"

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": initial_assistant_greeting}
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
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content

            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
