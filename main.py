# write in the file using with()function
with open('file.txt', 'w') as file:
    file.write("Hi! I am Mike and I am 1 yr old.")
    file.close()

# split file into words
with open('file.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print(word)
file.close()        