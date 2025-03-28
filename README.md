# Project_Shazam
**Project Shazam - Audio File Uploader and Transcription with Contextual Q&A**

Project Shazam is a web-based application built using Streamlit that allows users to upload audio files, transcribe them using AssemblyAI, and perform contextual question-answering based on a pre-loaded text database. The app leverages Google Generative AI for embeddings and language model responses, with Chroma as the vector database for similarity search.

**Features**
- Upload any audio file and store it temporarily in the session state.
- Transcribe audio files using the AssemblyAI API.
- Perform similarity search on a pre-loaded text database (e.g., subtitle files) using Google Generative AI embeddings.
- Generate detailed answers to questions derived from the transcription, based on the retrieved context.
- Simple and intuitive UI powered by Streamlit.

**Prerequisites**<br>
Python 3.8+<br>
A Google API key for Google Generative AI (set as an environment variable: GOOGLE_API_KEY).<br>
An AssemblyAI API key for audio transcription (set as an environment variable: voice_api).<br>
A directory of text files (e.g., subtitles_text) to populate the vector database (optional, if not pre-built).<br>

**Installation**<br>
1. Clone the Repository<br>
   git clone https://github.com/yourusername/project-shazam.git<br>
   cd project-shazam
2. Set Up a Virtual Environment (Optional but Recommended)<br>
   python -m venv venv<br>
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies<br>
   pip install -r requirements.txt<br>
4. Set Environment Variables<br>
   export GOOGLE_API_KEY="your-google-api-key"<br>
   export voice_api="your-assemblyai-api-key"
5. Prepare the Vector Database<br>
   Place your text files (e.g., .txt subtitle files) in a folder named subtitles_text.<br>
   Uncomment and run the chunking code in database.py to populate the Chroma vector database (this only needs to be done once):<br>

   loader = DirectoryLoader('subtitles_text', glob="*.txt", show_progress=True, loader_cls=TextLoader)<br>
   docs = loader.load()<br>
   text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)<br>
   chunks = text_splitter.split_documents(docs[:10])<br>
   db.add_documents(chunks[:20000])<br>
   
   The database will be saved in the chroma_db_ directory<br>

**File Structure**<br>
app.py: Main Streamlit application for audio upload, transcription, and Q&A.<br>
database.py: Handles loading text files, creating embeddings, and managing the Chroma vector database.<br>
model.py: Defines the prompt template and initializes the Google Generative AI model.<br>

**Notes**<br>
- The app assumes a pre-built Chroma database in .\chroma_db_. If the database is empty or missing, populate it using the steps in "Prepare the Vector Database."
- The current implementation uses gemini-2.0-flash as the language model, which requires a valid Google API key.
- Audio file processing happens in-memory via st.session_state; large files may impact performance.
- Error handling is basic—e.g., "file is not uploaded" is shown for any exception.

**Future Improvements**<br>
- Add support for multiple audio formats explicitly.
- Enhance error handling with specific messages for different failure cases.
- Allow users to upload their own text corpus dynamically.
- Optimize chunking and database storage for larger datasets.

**License**<br>
This project is licensed under the MIT License. See the  file for details.
