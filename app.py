import streamlit as st
import boto3
import json
from langchain_aws import BedrockEmbeddings
from langchain_community.vectorstores import Chroma

# --- Modern UI Configuration ---
st.set_page_config(page_title="Nova RAG Pro", page_icon="🚀", layout="wide")

# Custom CSS for the "Modern AI" look
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stTextInput input {
        background-color: #1e2227 !important;
        color: white !important;
        border: 1px solid #3e4451 !important;
        border-radius: 10px !important;
    }
    .stButton>button {
        background-color: #FF9900;
        color: white;
        border-radius: 10px;
        border: none;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    .answer-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #FF9900;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("AWS Bedrock RAG Assistant")
st.markdown("---")

# Setup (Keeping your exact logic)
bedrock_client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0", client=bedrock_client)

# Load the memory from your existing chroma_db folder
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

# --- Modern Input Layout ---
# Using columns to put the input and button side-by-side
col1, col2 = st.columns([4, 1])

with col1:
    query = st.text_input("What would you like to know?", placeholder="Ask about your documents...", label_visibility="collapsed")

with col2:
    # This is the 'Ask' button you requested
    ask_clicked = st.button("Ask Nova")

# Trigger logic on button click
if ask_clicked and query:
    with st.spinner("🔍 Searching Knowledge Base..."):
        # 1. Search for context (Your original logic)
        docs = vectorstore.similarity_search(query, k=3)
        context = "\n".join([d.page_content for d in docs])
        
        # 2. Build the Prompt for Nova Pro
        prompt = f"""Use the following context to answer the question. 
        Context: {context}
        Question: {query}
        Answer:"""
        
        # 3. Call Nova Pro
        payload = {
            "messages": [{"role": "user", "content": [{"text": prompt}]}]
        }
        
        response = bedrock_client.invoke_model(
            modelId="amazon.nova-pro-v1:0",
            body=json.dumps(payload)
        )
        
        result = json.loads(response['body'].read())
        answer = result['output']['message']['content'][0]['text']
        
        # Display the answer in a modern card
        st.markdown(f"""
            <div class="answer-card">
                <h3 style='color: #FF9900; margin-top: 0;'>🤖 Nova Pro Answer</h3>
                <p style='line-height: 1.6;'>{answer}</p>
            </div>
        """, unsafe_allow_html=True)

elif ask_clicked and not query:
    st.warning("Please enter a question first!")