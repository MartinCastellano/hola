address = "255.100.50.0"

address = list(address)

for i in range(len(address)):
    if address[i]=='.':
        address[i]='[.]'

address = "".join(address)


print(address)