# import streamlit as st
# import streamlit.components.v1 as components
# import requests

# # Set page config
# st.set_page_config(page_title="ThinkHR Copilot", layout="wide")

# # Title
# st.markdown("<h1 style='text-align: center;'>ThinkHR - Power BI + Chatbot</h1>", unsafe_allow_html=True)

# # ---- Embed Power BI Report ---- #
# embed_url = "https://app.powerbi.com/view?r=eyJrIjoiYmZjNjY0YmQtZGQ1OS00YjA4LWE2ODktMTZiYjY3YmE0ZWFhIiwidCI6IjM4NjAzYTNkLWRiY2MtNDk3ZS1hMjE4LWQ1ODcxYWU4YmJlMyJ9"
# components.html(
#     f"""
#     <div style="display: flex; justify-content: center; padding-bottom: 20px;">
#         <iframe title="Power BI Report"
#                 width="1200" height="700"
#                 src="{embed_url}"
#                 frameborder="0" allowFullScreen="true">
#         </iframe>
#     </div>
#     """,
#     height=720,
# )

# # ---- Chat Section ---- #
# st.markdown("### Ask the HR Dashboard Copilot")

# # Input box
# question = st.text_input("Enter your question", "")

# # When user submits a question
# if st.button("Ask") and question.strip():
#     try:
#         # Call your backend API (change the URL if deployed somewhere else)
#         api_url = "https://fabric-chatbot-backend.onrender.com/ask"
#         # print("hello")
#         response = requests.post(api_url, json={"question": question})
#         # print("hello1")
#         response.raise_for_status()
#         print(response)
#         result = response.json()
#         print(result)

#         # Show answer
#         st.success(result.get("answer", "No response returned."))
#     except Exception as e:
#         st.error(f"Error: {str(e)}")


# app.py
import streamlit as st
import requests

st.set_page_config(page_title="HR Copilot", layout="wide")
st.title("ThinkHR - Chat with Fabric + Power BI")

# Chat section
question = st.text_input("Ask a question to the HR Dashboard")

if st.button("Ask") and question.strip():
    try:
        res = requests.post(
            "http://localhost:10000/ask",  # change this to your deployed backend if needed
            json={"question": question}
        )
        res.raise_for_status()
        answer = res.json().get("answer", "No answer returned.")
        st.success(answer)
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Embed report
st.markdown("---")
st.markdown("### 📊 HR Dashboard Report")
st.components.v1.html(
    """
    <iframe title="HR Dashboard"
            width="1200"
            height="750"
            src="https://app.powerbi.com/reportEmbed?reportId=dd989b6e-00b6-4a28-b25c-e309074b1bb8&autoAuth=true&ctid=38603a3d-dbcc-497e-a218-d5871ae8bbe3"
            frameborder="0"
            allowFullScreen="true">
    </iframe>
    """,
    height=800
)