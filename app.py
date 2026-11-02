import streamlit as st
from chatbot_logic import get_train_bot_response

st.set_page_config(page_title="Indian Railways AI Assistant", page_icon="🚆", layout="centered")

st.title("🚆 RailMitra: AI Train Booking Assistant")
st.markdown("Ask me about train schedules, routes, ticket classes, or help with your journey planning!")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input text box
if user_query := st.chat_input("E.g., Find trains from Chennai to Madurai tomorrow"):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... (Querying local Ollama model)"):
            # Format history for context
            history_text = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages[-5:]])
            response = get_train_bot_response(user_query, history_text)
            st.markdown(response)
            
    # Append assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})