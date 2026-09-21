# from langchain_community.document_loaders import TextLoader

# data = TextLoader("document loaders/notes.txt",
#                       encoding="utf-8"
#                   )

# docs = data.load()

# print(docs[0].page_content)


#print(len(docs))
# docs (document) contains 2 things -> 
# 1. matadata , 2. Page_content





##### Character Based Splitting

from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator= "",
    chunk_size = 10,
    chunk_overlap = 1
)

data = TextLoader("document loaders/testt.txt",
                      encoding="utf-8"
                  )

docs = data.load()

chunks = splitter.split_documents(docs)

print(len(chunks))

for i in chunks:
    print(i.page_content)
    print()
    print()
    print()
























