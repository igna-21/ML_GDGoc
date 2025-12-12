file = 'data.txt'

with open(file, 'r') as file:
    lines_list = file.readlines()

for line in lines_list:
    if int(line.strip()) % 2 == 0:
        print("angka:", line.strip(), "adalah Ganjil")
    else:
        print("angka:", line.strip(), "adalah Genap")

