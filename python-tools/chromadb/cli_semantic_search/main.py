import os


options = """
1. Add new document.
2. Search through documents.
3. Update a document.
4. Delete a document.

Enter your option (number) : 
"""

while True:

    try:
        user_option = int(input(options))
    except ValueError:
        print("please enter the appropreate number of the option.")
        continue

    os.system("clear")

    match user_option:
        case 1:
            print("<< ADD NEW DOCUMENT >>")

        case 2:
            print("<< SEARCH THROUGH DOCUMENT >>")

        case 3:
            print("<< UPDATE DOCUMENT >>")

        case 4:
            print("<< DELETE DOCUMENT >>")

        case _:
            print("please enter the appropreate number of the option.")
