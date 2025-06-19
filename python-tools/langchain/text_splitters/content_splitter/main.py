from argparse import ArgumentParser
from content_splitter.utils import _load_pdf, _load_txt, _split_to_chunks

arg_parser = ArgumentParser(
    description="A CLI utility program to split content from `.txt` or `.pdf` and save in several chunks."
)

arg_parser.add_argument(
    "--type",
    required=True,
    type=str,
    choices=["pdf", "txt"],
)
arg_parser.add_argument(
    "--path",
    required=True,
    type=str,
)

arg_parser.add_argument(
    "--size",
    default=50,
    type=int,
)

args = arg_parser.parse_args()

match (args.type):
    case "pdf":
        pdf_content = _load_pdf(path=args.path)
        _split_to_chunks(content=pdf_content, chunks=args.size)

    case "txt":
        txt_content = _load_txt(path=args.path)
        _split_to_chunks(content=txt_content, chunks=args.size)
