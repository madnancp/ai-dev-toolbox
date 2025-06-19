def _load_pdf(path: str) -> str:
    from langchain_community.document_loaders import PyPDFLoader

    loader = PyPDFLoader(file_path=path)
    pdf_content = loader.load()
    return pdf_content[0].page_content


def _load_txt(path: str) -> str:
    from langchain_community.document_loaders import TextLoader

    loader = TextLoader(file_path=path)
    pdf_content = loader.load()
    return pdf_content[0].page_content


def _split_to_chunks(content: str, chunks: int = 50) -> None:
    import os
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunks, separators=["\n\n", "\n", ".", "", ""], chunk_overlap=0
    )
    doc_chunks = splitter.split_text(content)

    os.makedirs("./outputs", exist_ok=True)
    for idx, chunk in enumerate(doc_chunks, start=1):
        with open(f"./outputs/{idx}_chunk.txt", "w") as file:
            file.write(chunk)
        print(f"./outputs/{idx}_chunk.txt WRITED SUCCESSFULLY")
