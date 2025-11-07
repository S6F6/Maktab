import sys
from datetime import datetime
import json
from pathlib import Path
from pprint import pprint

def read_json():
    file_path = Path("./notes.json")
    data = []
    if file_path.exists():
        with open(file_path, "r") as file:
            try:
                old_entry = json.load(file)
                data.extend(old_entry)
            except json.JSONDecodeError as e:
                print(e)
    
    return data

def write_to_json(data):
    with open("./notes.json", "w") as f:
        json.dump(data, f, indent=4)

def add_note():
    title = input("Enter title: ")
    try:
        date_str = input("Enter a date (YYYY-MM-DD): ")
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    except Exception as e:
        print("You entered wrong date format.")
        return
    print("Paste your text (Ctrl+D(in linux)) or Ctrl+Z(in windows) to finish):")
    content = sys.stdin.read()
    new_entry = {
        "title": title,
        "date": date_obj.strftime("%Y-%m-%d"),  
        "content": content
    }

    data = read_json()
    data.append(new_entry)
    write_to_json(data)
    print("data saved to notes.json")

def show_all_notes():
    data = read_json()
    pprint(data)

def search_note():
    title = input('Enter title or part of it: ')
    data = read_json()
    counter = 0
    for item in data:
        if title in item['title']:
            pprint(item)
            counter += 1
    if counter == 0:
        print("No data found!")

def delete_note():
    title = input('Enter exact title to remove: ')
    data = read_json()

    new_data = []
    is_removed = False
    for item in data:
        if title != item['title']:
            new_data.append(item)
        elif title == item['title']:
            print(f"{title} removed!")
            is_removed = True
    
    write_to_json(new_data)
    if not is_removed:
        print(f"{title} is not found!")

def ask_command():
    command = input("Enter 'a' to add note\n" \
                "Enter 's' to search notes\n" \
                "Enter 'sh' to show all notes\n" \
                "Enter 'd' to delete specific notes\n" \
                "Enter anything else to quit:")
    
    return command

def note_book():
    command = ask_command()
    while command in ['a', 's', 'd', 'sh']:
        if command == 'a':
            add_note()
        elif command == 'sh':
            show_all_notes()
        elif command == 's':
            search_note()
        elif command == 'd':
            delete_note()
        command = ask_command()
note_book()