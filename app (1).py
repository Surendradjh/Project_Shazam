import streamlit as st
import assemblyai as aai
from database import db
from model import prompt_template,model

st.title("Project Shazam - Audio File Uploader")

uploaded_file = st.file_uploader("Upload any audio file", type=None)

if uploaded_file is not None:
    audio_file = uploaded_file.read()
    st.session_state.audio_file = audio_file
    # st.success("Audio file uploaded and stored in the background as 'audio_file'!")
    st.write(f"Stored audio file size: {len(st.session_state.audio_file)} bytes")

if "audio_file" not in st.session_state:
    st.info("Please upload an audio file to store it in the background.")
else:
    # st.info("Audio file is stored in the background. You can proceed with further processing.")
    aai.settings.api_key = "ab1cac1fd1aa42ccaaf517ae98030f8d"
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)
    st.write(transcript.text)
    query = transcript.text
    docs_chroma = db.similarity_search_with_score(query, k=3)
    context_text = "\n\n".join([doc.page_content for doc,_score in docs_chroma])
    prompt = prompt_template.format(context=context_text, question=query)
    response_text = model.invoke(prompt)

    st.write(response_text.content)
