import random

file = 'Study jam 1\dengan library random\data.txt'

with open(file, "w") as f:
    pass
with open(file, "w") as f:
    for i in range(20):
        random_integer = random.randint(1, 20)
        f.write(str(random_integer))
        f.write("\n")
f.close()

with open(file, 'r') as file:
    lines_list = file.readlines()

for line in lines_list:
    if int(line.strip()) % 2 == 0:
        print("angka:", line.strip(), "adalah Ganjil")
    else:
        print("angka:", line.strip(), "adalah Genap")

