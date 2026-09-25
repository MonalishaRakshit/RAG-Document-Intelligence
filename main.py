##### Mistral Model 
# from dotenv import load_dotenv

# from langchain_mistralai import ChatMistralAI

# load_dotenv() 

# model = ChatMistralAI(model ="mistral-small-2603")


# result = model.invoke("Hello")

# print(result.content)




##### Groq Model 
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# model = ChatGroq(
#     model="openai/gpt-oss-20b"
# )

# result = model.invoke("Hello, explain RAG in one sentence.")

# print(result.content)






########## here we feed our LLM Model external data source (extract data from Text document)
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_community.document_loaders import TextLoader
# from langchain_core.prompts import ChatPromptTemplate

# load_dotenv()

# data = TextLoader("document loaders/notes.txt",  
#                       encoding="utf-8"
#                   )  #load data
# docs = data.load()  # convert data into document object

# template = ChatPromptTemplate.from_messages(
#     [("system","you are a AI that summarizes the text"),
#      ("human", "{data}")
#      ]
# )

# model = ChatGroq(
#     model="openai/gpt-oss-20b"
# )

# prompt = template.format_messages(data = docs[0].page_content)

# result = model.invoke(prompt)

# print(result.content)







########## here we feed our LLM Model external data source (extract data from PDF document)
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_core.prompts import ChatPromptTemplate

# load_dotenv()

# data = PyPDFLoader("document loaders/GRU.pdf")  #load data
# docs = data.load()  # convert data into document object

# template = ChatPromptTemplate.from_messages(
#     [("system","you are a AI that summarizes the text"),
#      ("human", "{data}")
#      ]
# )

# model = ChatGroq(
#     model="openai/gpt-oss-20b"
# )

# prompt = template.format_messages(data = docs[0].page_content)

# result = model.invoke(prompt)

# print(result.content)




 #### splitting very large document by creating chunks
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

data = PyPDFLoader("document loaders/GRU.pdf")  #load data
docs = data.load()  # convert data into document object

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 700,
    chunk_overlap = 200
)

chunks = splitter.split_documents(docs)

template = ChatPromptTemplate.from_messages(
    [("system","you are a AI that summarizes the text"),
     ("human", "{data}")
     ]
)

model = ChatGroq(
    model="openai/gpt-oss-20b"
)

prompt = template.format_messages(data = docs[0].page_content)

result = model.invoke(prompt)

print(result.content)




