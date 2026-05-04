import os
import re

sets = ['CEP', 'CoS', 'D&D', 'ER', 'TLD']
for s in sets:
    path = f'sets/{s}-files/{s}.json'
    with open(path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    content = re.sub(r'""(?=[a-zA-Z"])', '","', content)
    with open(path, 'w', encoding='utf-8-sig') as f:
        f.write(content)
print("Fixed all JSON files")