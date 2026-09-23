# from langchain_community.document_loaders import PyPDFLoader

# data = PyPDFLoader("document loaders/GRU.pdf",
#                   )

# docs = data.load()

# print(docs[7])


# docs (document) contains 2 things -> 
# 1. matadata , 2. Page_content
# so , if there are 15 docs then each docs has it's own  1. matadata , 2. Page_content
# no. of pages in pdf == the no of document form


from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

data = PyPDFLoader("document loaders/GRU.pdf",
                  )

docs = data.load()

splitter = TokenTextSplitter(
    chunk_size = 700,
    chunk_overlap = 5
)

chunks = splitter.split_documents(docs)

print(chunks[0].page_content)





