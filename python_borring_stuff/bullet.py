#! python3
#

''' lista de animales
    lista de vida marina
    lista de biologos y autores
    lista de cultivos '''

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)

