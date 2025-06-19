> [!NOTE]
> A cli utility to split the content from a .txt file or pdf 
> and make chunks with the text`

- used `langchain` & `argparse`

usage
```bash
python -m content_splitter.main --type pdf --path path/to/pdf --size 100

# it will fetch the content from the pdf and split to several chunks that contain 100 chars in each. and store that in txt files
```

