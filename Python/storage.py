import json
import sort

def load():
    global notes
    with open('notes.json', 'r', encoding='utf-8') as dl:
        notes = json.load(dl)
    return notes

def save():
    sort.sorting()
    with open('notes.json', 'w', encoding='utf-8') as dl:
        dl.write(json.dumps(notes, ensure_ascii=False))

# def save_sort():
#     with open('notes.json', 'w', encoding='utf-8') as dl:
#         dl.write(json.dumps(notes, ensure_ascii=False, sort_keys=True))
