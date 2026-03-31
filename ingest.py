import boto3
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings
from langchain_community.vectorstores import Chroma

# Initialize Bedrock
bedrock_client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Use the model we just successfully tested
embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v2:0", 
    client=bedrock_client
)

def create_vector_store():
    print("Loading PDFs from 'data' folder...")
    loader = PyPDFDirectoryLoader("data")
    docs = loader.load()
    
    print(f"Splitting {len(docs)} pages into smaller chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(docs)
    
    print("Creating embeddings and saving to chroma_db folder...")
    vectorstore = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory="./chroma_db"
    )
    print("✅ Done! Your AI now has memory.")

if __name__ == "__main__":
    create_vector_store()