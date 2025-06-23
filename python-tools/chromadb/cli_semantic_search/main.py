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
5. Fetch all documents.

Enter your option (number) : 
"""


def format_result(result: dict, limit: int = 2) -> None:
    for each in range(limit):
        print(f"{each+1}). ", end="")
        if "distances" in result.keys():
            print(f"DISTANCE: {result.get('distances', '')[0][each]}", end=" || ")
            print(f"ID: {result.get('ids', '')[0][each]}", end=" || ")
            print(f"DOCUMENT: {result.get('documents', '')[0][each]}")

        else:
            print(f"ID: {result.get('ids', '')[each]}", end=" || ")
            print(f"DOCUMENT: {result.get('documents', '')[each]}")


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
            id = input(
                "Enter document ID (please look at `fetch all document option): "
            )
            new_sentence = input("Enter new sentence: ")
            status, err = store.update(id=id, new_sentence=new_sentence)
            if status:
                print(f"<<✅ {id} UPDATED ✅>>")
            else:
                print(f"❌ from update doc: {err} ❌")

            print("<<✅ END OF UPDATE DOCUMENT ✅>>")

        case 4:
            print("<<✅ DELETE DOCUMENT ✅>>")

            id = input(
                "Enter document ID (please look at `fetch all document option): "
            )
            status, err = store.delete(id=id)
            if status:
                print(f"<<✅ {id} DELETED ✅>>")
            else:
                print(f"❌ from delete doc: {err} ❌")

            print("<<✅ END OF DELETE DOCUMENT ✅>>")

        case 5:
            print("<<✅ FETCH ALL DOCUMENT ✅>>")
            result = store.fetch_all
            format_result(result, limit=len(result.get("ids")))
            print("<<✅ END OF FETCH ALL DOCUMENT ✅>>")

        case _:
            print("please enter the appropreate number of the option.")
