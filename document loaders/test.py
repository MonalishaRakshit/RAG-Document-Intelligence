from langchain_community.document_loaders import TextLoader

data = TextLoader("document loaders/notes.txt",
                      encoding="utf-8"
                  )

docs = data.load()

print(docs[0].page_content)
#print(len(docs))

# docs (document) contains 2 things -> 
# 1. matadata , 2. Page_content
