import json

with open("../data/domains.json", 'r') as file_handle:
    content = file_handle.read()

domains_dict = json.loads(content)
new_domains_dict = {}
for domain, author_list in domains_dict.items():
    new_domains_dict[domain] = json.dumps(author_list)

with open("../data/new_domains.json", 'w') as file_handle:
    file_handle.write(json.dumps(new_domains_dict))
