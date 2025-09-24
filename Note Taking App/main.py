import os

notes_dir = 'notes'

def display_menu():
    print("\nNote Taking App")
    print("1. Create a new note")
    print("2. View existing notes")
    print("3. Delete a note")
    print("4. Exit")

def view_notes():
    print("Existing Notes: \n")
    if not os.path.exists(notes_dir):
        print("No Notes Available")
        return
    for filename in os.listdir(notes_dir):
        with open(os.path.join(notes_dir,filename),"r") as file:
            content = file.read()
            print(f"{filename[:-4]} : {content}")
    
def add_note():
    note_title = input("Enter note title: ")
    note_content = input("Enter the note content: ")

    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)
    
    note_path = os.path.join(notes_dir,f"{note_title}.txt")
    with open(note_path,"a") as file:
        file.write(f"{note_content}\n")
    print(f"Note '{note_title}' added Succesfully")

def delete_note():
    note_title = input("Enter note title: ")
    note_path = os.path.join(notes_dir,f"{note_title}.txt")

    if os.path.exists(note_path):
        os.remove(note_path)
        print(f"Note '{note_title}' deleted successfully.")
    else:
        print(f"Note '{note_title}' not found.")

def main():
    while True:
        display_menu()
        choice = int(input("Enter your Choice (1-4): "))

        if choice == 1:
            add_note()
        elif choice == 2:
            view_notes()
        elif choice == 3:
            delete_note()
        elif choice == 4:
            print("Exiting the App")
            break
        else:
            print("Please Enter number between (1-4)")

if __name__ == '__main__':
    main()