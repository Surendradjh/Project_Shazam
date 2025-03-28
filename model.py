from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os

PROMPT_TEMPLATE = """
Answer the question based only on the following context:
{context}
Answer the question based on the above context: {question}.
Provide a detailed answer.
Don’t justify your answers.
Don’t give information not mentioned in the CONTEXT INFORMATION.
Do not say "according to the context" or "mentioned in the context" or similar.
"""

prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
google_api= os.environ.get("google_api")
google_api_key=google_api 
model=ChatGoogleGenerativeAI(api_key=google_api_key, model="gemini-2.0-flash")
