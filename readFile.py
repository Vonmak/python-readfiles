# # this reads the whole file
# handle = open("text.txt", "r")

# data = handle.read()
# print(data)

# handle.close()


# # this reads a single  first line
# handle = open("text.txt", "r")

# data = handle.readline()
# print(data)

# handle.close()


# # this reads a single letter
# handle = open("text.txt", "r")

# data = handle.readline()[1]
# print(data)

# handle.close()


# # this reads a multiple lines
# handle = open("text.txt", "r")

# data = handle.readlines()
# print(data)

# handle.close()

# # this reads a single selected line
# handle = open("text.txt", "r")

# data = handle.readlines()[3]
# print(data)

# handle.close()


# # looping through a file
# # occurrence of a word
# # counting starts from [0] so when it says 2 it means there are 3  instances.
# handle = open("text.txt", "r")
# data = handle.read()
# counter = 0
# for word in data.split():
#     if word == "is":
#         counter += 1

# print(counter)


handle = open("text-write.txt", "w")

handle.write("Hello Victor")
handle.close()

with open("text-write.txt", "r") as handle:
    data = handle.read()
    print(data)
