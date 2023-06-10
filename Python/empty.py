import json


notes={}

def save():
    with open('notes.json', 'w', encoding='utf-8') as ds:
        ds.write(json.dumps(notes, ensure_ascii=False))

# save()
