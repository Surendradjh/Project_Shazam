from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

loader = DirectoryLoader('subtitles_text', glob="*.txt", show_progress=True, loader_cls=TextLoader)
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
chunks = text_splitter.split_documents(docs[:10])

os.environ["GOOGLE_API_KEY"] = "AIzaSyC9j5KaPVcanw9nvPAfKfORBqsCzBjx37I"
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
db = Chroma(collection_name="vector_database",
            embedding_function=embedding_model,
            persist_directory=".\chroma_db_")
db.add_documents(chunks[:20000])