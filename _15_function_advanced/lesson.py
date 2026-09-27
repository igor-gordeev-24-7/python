import json

book = {
    'title': '1984',
    'author': 'George Orwell',
    'isbn': '978-0451524935',
    'uuid': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
}

json_string = json.dumps(book)

print(json_string)
print(type(json_string))