def largest(filename):
    file = open(filename, "r")
    longest = ""
    for line in file:
        if len(line) > len(longest):
            longest = line
    file.close()
    print("Longest line in the file is:")
    print(longest)


fname = input("Enter the file name: ")
largest(fname)