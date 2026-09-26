import ollama, os
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

base_url = os.getenv("OLLAMA_BASE_URL")
client =  ollama.Client(base_url)
ollama_embed = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)
vectore_store = QdrantVectorStore.from_existing_collection(
    embedding=ollama_embed,
    url="http://localhost:6333",
    collection_name="test-rag"
)

print(f"\n🤖 How Can i assist you today ?\n")
user_ip = input(">> ")

srch_res = vectore_store.similarity_search(query=user_ip)
context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" 
                       for result in srch_res])

SYSTEM_PROMPT = f"""
You are a helpful assistant. you need to return all the queries from the user 
by the conetxt i am going to provide as an source of truth as a pdf result.

Give the loaction of file exact page number
for refence once you finish processing the resoponse

Context: {context}
"""

resp = client.chat(
    model="gemma:2b",
    messages=[
        {"role": "system","content": SYSTEM_PROMPT},
        {"role": "user","content": user_ip},
    ],
    stream=False
)

print(f"\n{resp.message.content}\n")