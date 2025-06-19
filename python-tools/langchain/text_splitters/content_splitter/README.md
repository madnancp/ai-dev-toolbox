> [!NOTE]
> A cli utility to split the content from a .txt file or pdf 
> and make chunks with the text`

- used `langchain` & `argparse`

usage
```bash
python main.py --pdf path/to/pdf --chunk_size 200

# it will fetch the content from the pdf and split to several chunks that contain 200 chars in each. and store that in txt files
```

