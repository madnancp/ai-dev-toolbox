# load .txt file
# TextLoader can load `.txt` & `.md`
from langchain_community.document_loaders import TextLoader

text_loader = TextLoader(file_path="./content.txt")
text_data = text_loader.load()
print(f"Text File `page_content` : {text_data[0].page_content}")
print(f"Text File `metadata` : {text_data[0].metadata}")

#####################################################

# load .json file
# depends: `jq`
from langchain_community.document_loaders import JSONLoader

json_loader = JSONLoader(file_path="./data.json", jq_schema=".", text_content=False)
json_data = json_loader.load()
print(f"Json File `page_content` : {json_data[0].page_content}")
print(f"Json File `metadata` : {json_data[0].metadata}")


#####################################################
