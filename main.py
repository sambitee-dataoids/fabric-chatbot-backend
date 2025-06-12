import os
from fastapi import FastAPI, Request
import requests
import msal
 
app = FastAPI()
 
TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
DATA_AGENT_ID = os.getenv("DATA_AGENT_ID")
SEMANTIC_MODEL_ID = os.getenv("SEMANTIC_MODEL_ID")
SCOPE = ["https://api.fabric.microsoft.com/.default"]
FABRIC_API_URL = "https://api.fabric.microsoft.com/dataagent/query"
 
def get_token():
    app_auth = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}",
        client_credential=CLIENT_SECRET
    )
    token_result = app_auth.acquire_token_for_client(scopes=SCOPE)
    return token_result["access_token"]
 
@app.post("/ask")
async def ask_question(req: Request):
    body = await req.json()
    question = body.get("question")
    token = get_token()
 
    response = requests.post(
        FABRIC_API_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        json={
            "dataAgentId": DATA_AGENT_ID,
            "semanticModelId": SEMANTIC_MODEL_ID,
            "naturalLanguageQuery": question
        }
    )
 
    try:
        return {"answer": response.json().get("answer", "No answer found")}
    except Exception:
        return {"answer": "Error connecting to Fabric Data Agent."}
 