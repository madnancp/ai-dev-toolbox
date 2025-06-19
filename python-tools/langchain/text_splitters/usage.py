# example of `RecursiveCharacterTextSplitter`
# most common in RAG applications.
# it split with meaning aware way
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_loader = TextLoader(file_path="./content.txt")
text_doc = text_loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=15, chunk_overlap=5, separators=[" ", ""]
)

splited = text_splitter.split_documents(text_doc)
for idx, each in enumerate(splited, start=1):
    print(f"Document {idx} : {each.page_content} len : {len(each.page_content)}")
