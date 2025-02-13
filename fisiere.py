with open('file1.txt', 'a') as file:
    file.write('Test')
    file.close()

with open('file1.txt', 'r') as file:
    for line in list(file):
        print(line)


with open('file1.txt', 'r') as file:
    for line in file.readlines():
        print(line)
