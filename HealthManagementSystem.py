print("~~~ Welcome to Riya's Health Management System ~~~\n")
def name_choice():
    c1=int(input("Choose:\n 1 for Harry:\n 2 for Rohan:\n 3 for Hammad:\n Enter your choice:"))
    if c1==1:
        c2=int(input("Choose:\n Log : 0\n Retrieve : 1\n Enter your choice:"))
        c3=int(input("Choose the file:\n Exercise : Press 0\n Food : Press 1\n"))
        if c2==0 and c3==0:
            m1=input("Enter what you want to write in the exercise file:")
            with open ("harryex.txt","a") as f:
                f.write("\n")
                f.write(m1)
                print("Successfully added !")
        if c2==0 and c3==1:
            m2=input("What you want to write in food file:")
            with open ("harryfood.txt", "a") as f:
                f.write("\n")
                f.write(m2)
                print("Successfully added !")
        if c2==1 and c3==0:
            with open ("harryex.txt", "rt") as f:
                print(f.read())
        if c2==1 and c3==1:
            with open ("harryfood.txt", "rt") as f:
                print(f.read())

    elif c1==2:
        c2=int(input("Choose:\n Log : 0\n Retrieve : 1\n Enter your choice:"))
        c3=int(input("Choose the file:\n Exercise : Press 0\n Food : Press 1\n"))
        if c2==0 and c3==0:
            m1=input("Enter what you want to write in the exercise file:")
            with open ("rohanex.txt","a") as f:
                f.write("\n")
                f.write(m1)
                print("Successfully added !")
        if c2==0 and c3==1:
            m2=input("What you want to write in food file:")
            with open ("rohanfood.txt", "a") as f:
                f.write("\n")
                f.write(m2)
                print("Successfully added !")
        if c2==1 and c3==0:
            with open ("rohanex.txt", "rt") as f:
                print(f.read())
        if c2==1 and c3==1:
            with open ("rohanfood.txt", "rt") as f:
                print(f.read())

    elif c1==3:
        c2=int(input("Choose:\n Log : 0\n Retrieve : 1\n Enter your choice:"))
        c3=int(input("Choose the file:\n Exercise : Press 0\n Food : Press 1\n"))
        if c2==0 and c3==0:
            m1=input("Enter what you want to write in the exercise file:")
            with open ("hammadex.txt","a") as f:
                f.write("\n")
                f.write(m1)
                print("Successfully added !")
        if c2==0 and c3==1:
            m2=input("What you want to write in food file:")
            with open ("hammadfood.txt", "a") as f:
                f.write("\n")
                f.write(m2)
                print("Successfully added !")
        if c2==1 and c3==0:
            with open ("hammadex.txt", "rt") as f:
                print(f.read())
        if c2==1 and c3==1:
            with open ("hammadfood.txt", "rt") as f:
                print(f.read())
     

name_choice()