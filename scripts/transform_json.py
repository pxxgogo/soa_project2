import json

with open("../data/authors.json", 'r') as file_handle:
    content = file_handle.read()

authors_dict = json.loads(content)
new_authors_dict = {}
for author, author_info in authors_dict.items():
    new_authors_dict[author] = json.dumps(author_info)

with open("../data/new_authors.json", 'w') as file_handle:
    file_handle.write(json.dumps(new_authors_dict))
