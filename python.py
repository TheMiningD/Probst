with open('hosts.md', 'r', encoding='utf_16') as file  
    content = file.read()

with open('hosts.md', 'w', encoding='utf_8') as file
    file.write(content)
