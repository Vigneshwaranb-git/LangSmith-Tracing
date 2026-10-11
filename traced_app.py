import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model_name="gpt-4o-mini", api_key=api_key)
prompts = ["Write a short story about  GenAI.", "What are the benefits of GenAI?", "How does GenAI work?"]
for p in prompts:
    print(model.invoke(p).content)
# prompt = ChatPromptTemplate.from_messages(
#     [
#         "Explain {topic} in simple terms.",
#         "Provide an example of {topic}.",
#         "Summarize the key points about {topic}.",
#     ]
# )
# output_parser = StrOutputParser()
# chain = prompt | model | output_parser
# print(chain.invoke({"topic": "LangSmith"}))