import streamlit as st
from data_handler import CSVDataHandler
from agent import AIAgent
from voice import speak, listen

st.set_page_config(page_title="Voice AI Data Agent", layout="centered")

st.title("🎙️ Voice AI Data Agent (GROQ + CSV)")
st.markdown("Ask questions about your CSV data using voice or text.")

# Load data
data_handler = CSVDataHandler("RTO.csv")
agent = AIAgent(data_handler)

# Show data preview
with st.expander("📄 CSV Data Preview"):
    st.dataframe(data_handler.data)

# Task input (text or voice)
input_mode = st.radio("Select Input Mode", ["Text", "Voice"])

query = ""
if input_mode == "Text":
    query = st.text_input("Ask a question about the data")

elif input_mode == "Voice":
    if st.button("🎤 Start Listening"):
        query = listen()
        st.success(f"You said: {query}")

# Process query
if query:
    with st.spinner("Processing with GROQ..."):
        response = agent.handle_task(query)
        st.text_area("🧠 Response from AI", value=response, height=300)
        if st.button("🔊 Read Response"):
            speak(response[:400])
