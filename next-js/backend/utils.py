from typing import List
from time import sleep


def return_with_delay():
    text: List[str] = [
        "Hello",
        "my",
        "self",
        "Adnan",
        ".",
        "I",
        "Am",
        "Currently",
        "a",
        "BCA",
        "Final",
        "year",
        "student",
        ".",
        "I",
        "love",
        "to",
        "create",
        "application",
    ]

    for each in text:
        sleep(0.5)
        yield f"data: {each} \n\n"
