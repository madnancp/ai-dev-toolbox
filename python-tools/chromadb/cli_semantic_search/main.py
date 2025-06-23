import os
from cli_semantic_search.utils import VectorStore

print("Initializing vector store ⏳...")
store = VectorStore()
print("vector store initialized successfully ✅.")


options = """
1. Add new document.
2. Search through documents.
3. Update a document.
4. Delete a document.

Enter your option (number) : 
"""


def format_result(result: dict) -> None:
    for each in range(2):
        print(
            f"DISTANCE: {result.get('distances', '')[0][each]} || ID: {result.get('ids', '')[0][each]}"
        )
        print(f"DOCUMENT: {result.get('documents', '')[0][each]}")


while True:

    try:
        user_option = int(input(options))
    except ValueError:
        print("<<❌ please enter the appropreate number of the option ❌>>")
        continue

    os.system("clear")

    match user_option:
        case 1:
            print("<< ADD NEW DOCUMENT >>")
            text = input("Enter sentence: ")
            status, err = store.create(sentence=text)
            if status:
                print("<<✅ DOCUMENT ADDED TO STORE ✅>>")
            else:
                print(f"❌ from document creation : {err} ❌")
            continue

        case 2:
            print("<< SEARCH THROUGH DOCUMENT >>")
            text = input("Enter sentence: ")
            result = store.search(sentence=text)
            print("<<✅ RESULT OF SEARCH ✅>>")
            format_result(result)
            print("<<✅ END OF RESULT OF SEARCH ✅>>")
            continue

        case 3:
            print("<<✅ UPDATE DOCUMENT ✅>>")

        case 4:
            print("<<✅ DELETE DOCUMENT ✅>>")

        case _:
            print("please enter the appropreate number of the option.")
