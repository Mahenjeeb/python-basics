from pathlib import Path
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_qdrant import QdrantVectorStore

load_dotenv()
pdf_path = Path(__file__).parent / "Executive_Summary.pdf"
load_pdf = PyPDFLoader(file_path=pdf_path)
docs = load_pdf.load()
rcsplitter = RecursiveCharacterTextSplitter(
    chunk_size=4000,
    chunk_overlap=400
)
chunks = rcsplitter.split_documents(docs)
ollama_embed = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)
vectore_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=ollama_embed,
    url="http://localhost:6333",
    collection_name="test-rag"
)

print("Indexing of document is done")