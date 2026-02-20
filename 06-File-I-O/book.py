def main():
    with open("alice.txt", "r") as f:
        contents = f.readlines()
   # ffdfdfd
    chapter1 = contents[52:272]

#dfsdfdsfs

    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)

main()