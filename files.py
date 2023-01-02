try:
    # opening file in read mode
    f=open("file1.txt","r")
    print(f.read())
    f.close()

    # opening file in write mode 
    f1=open("file1.txt","w")
    f1.write(" \n Moon Light \n ")
    f1.close()

    # opening file in append mode
    f2=open("file1.txt","a")
    f2.write(" \n Rainbow \n ")
    f2.close()

    # opening file in r+ mode ( pointer is at beginig of the file)
    f3=open("file1.txt","r+")
    f3.write("recently added \n ")
    print(f3.read())
    f3.close()

    # opening file in w+ mode
    f4=open("file1.txt","w+")
    f4.write("\n new item \n ")
    f4.close()

    # opening file in a+ mode
    f5=open("file1.txt","a+")
    f5.write("\n a+ method \n")
    f5.close()
except:
    print("error occured in opening the file")
