from crud import stu_insert,stu_view,stu_update,staff_insert,staff_view


print("Welcome to Prince Group Of Institutions 🏫 \n")
print("1. Student Login🎓\n2. Staff Login🪪\n3. Admin Login🔑")
login=int(input("Enter your Login Number: "))
if login==1:
    while True:
        print(f"Student Dashboard 📚\n\nThe Operations you can perform:\n")
        print("Menu:\n\n Insert = 1\n View = 2\n Update = 3\n Exit = 4\n")
        User_input=(int(input("Enter the Operation Number: ")))
        if User_input==1:
            stu_insert()
        elif User_input==2:
            stu_view()
        elif User_input==3:
            stu_update()
        elif User_input==4:
            exit()
        else:
            print("Invalid Choice")
elif login==2:
    while True:
        print(f"Staff Dashboard 🪪\n\nThe Operations you can perform:\n")
        print("Menu:\n\n Insert = 1\n View = 2\n Update = 3\n Exit = 4\n")
        User_input=(int(input("Enter the Operation Number: ")))
        if User_input==1:
            staff_insert()
        elif User_input==2:
            staff_view()
        elif User_input==3:
            stu_update()
        elif User_input==4:
            exit()
        else:
            print("Invalid Choice")

    

  # if role_choice==2:
    #     print("Verify Your Identity as Staff\n")
    #     password=int(input("Enter your Password"))
    #     if password==4242:
    #          print("Your are in Staff")
    