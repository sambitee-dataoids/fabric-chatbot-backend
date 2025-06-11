import streamlit as st
import streamlit.components.v1 as components
import requests

# Set page config
st.set_page_config(page_title="ThinkHR Copilot", layout="wide")

# Title
st.markdown("<h1 style='text-align: center;'>ThinkHR - Power BI + Chatbot</h1>", unsafe_allow_html=True)

# ---- Embed Power BI Report ---- #
embed_url = "https://app.powerbi.com/reportEmbed?reportId=dd989b6e-00b6-4a28-b25c-e309074b1bb8&autoAuth=true&ctid=38603a3d-dbcc-497e-a218-d5871ae8bbe3"

components.html(
    f"""
    <div style="display: flex; justify-content: center; padding-bottom: 20px;">
        <iframe title="Power BI Report"
                width="1200" height="700"
                src="{embed_url}"
                frameborder="0" allowFullScreen="true">
        </iframe>
    </div>
    """,
    height=720,
)

# ---- Chat Section ---- #
st.markdown("### Ask the HR Dashboard Copilot")

# Input box
question = st.text_input("Enter your question", "")

# When user submits a question
if st.button("Ask") and question.strip():
    try:
        # Call your backend API (change the URL if deployed somewhere else)
        api_url = "https://fabric-chatbot-backend.onrender.com/ask"
        response = requests.post(api_url, json={"question": question})
        response.raise_for_status()
        result = response.json()

        # Show answer
        st.success(result.get("answer", "No response returned."))
    except Exception as e:
        st.error(f"Error: {str(e)}")
