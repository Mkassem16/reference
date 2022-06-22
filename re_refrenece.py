import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
pat
bat
'''


pattern = re.compile(r'M[rRsS].?\s?[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)



pattern = re.compile(r'[a-zA-Z0-9_-.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
with open('data.txt', 'r') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)



pattern = re.compile(r'ha', re.IGNORECASE)
matches = pattern.findall(text_to_search)
search = pattern.search('hey')
