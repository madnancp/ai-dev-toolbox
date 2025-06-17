# PromptTemplate example.
########################################
from langchain.prompts import PromptTemplate

prompt_temp = PromptTemplate.from_template(template="Translate To France, {content}")

llm_ip = prompt_temp.format(content="Thank You")
print(llm_ip)  # "Translate To France, Thank You"

###################################################


# ChatPromptTemplate example.
####################################################

from langchain.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages(
    messages=[
        (
            "system",
            "You are a helpful AI assistant, who give reply to user prompt in short answer.",
        ),
        (
            "user",
            "{prompt}",
        ),
    ]
)

chat_llm = chat_prompt.format(prompt="what is the hidden secret of Biriyani?")
print(
    chat_llm
)  # System: You are a helpful AI assistant, who give reply to user prompt in short answer.
# Human: what is the hidden secret of Biriyani?
####################################################
