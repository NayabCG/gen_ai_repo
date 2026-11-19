import uuid
import streamlit as st

from dotenv import load_dotenv

from langgraph.checkpoint.memory import InMemorySaver

from agents import create_supervisor
from database import initialize_database


load_dotenv()


# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Enterprise AI Assistant",
    page_icon="🤖",
    layout="wide"
)


# =====================================
# INITIALIZE DATABASE
# =====================================

initialize_database()


# =====================================
# CREATE SUPERVISOR WITH MEMORY
# =====================================

@st.cache_resource
def get_agent():

    memory = InMemorySaver()

    return create_supervisor(memory)


agent = get_agent()


# =====================================
# SESSION STATE
# =====================================

if "thread_id" not in st.session_state:

    st.session_state.thread_id = str(uuid.uuid4())


if "chat_history" not in st.session_state:

    st.session_state.chat_history = []


# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("Enterprise AI Assistant")

st.sidebar.subheader("Available Agents")

st.sidebar.markdown("""
- 👥 HR Agent
- 💰 Finance Agent
- 💻 IT Support Agent
- 🌦️ General Information Agent
""")

st.sidebar.divider()

st.sidebar.caption(
    "Powered by Python and LangChain"
)


if st.sidebar.button("New Conversation"):

    st.session_state.thread_id = str(uuid.uuid4())

    st.session_state.chat_history = []

    st.rerun()


# =====================================
# MAIN CHAT INTERFACE
# =====================================

st.title("🤖 Enterprise AI Assistant")

st.write(
    "Ask questions about company policies, "
    "employee information, IT support and more."
)


# Display previous conversations

for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# =====================================
# USER INPUT
# =====================================

user_input = st.chat_input(
    "Ask your question..."
)


if user_input:

    # Display user question

    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):

        st.markdown(user_input)


    # Invoke Supervisor Agent

    config = {
        "configurable": {
            "thread_id": st.session_state.thread_id
        }
    }

    try:

        with st.chat_message("assistant"):

            with st.spinner(
                "AI Agents are working..."
            ):

                response = agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": user_input
                            }
                        ]
                    },
                    config=config
                )

                answer = response["messages"][-1].content

                st.markdown(answer)


        # Save response in UI history

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:

        st.error(f"Something went wrong: {e}")