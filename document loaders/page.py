from langchain_community.document_loaders import WebBaseLoader

url = "https://www.apple.com/in-edu/store?afid=p240%7Cgo~cmp-11197666798~adg-197981515401~ad-808135809725_kwd-2469445450483~dev-c~ext-~prd-~mca-~nt-search&cid=aos-in-kwgo-txt-edu-edu--"

data = WebBaseLoader(url)

docs = data.load()

print(docs[0].page_content)




