from sqlalchemy.orm import sessionmaker
from models import Base,engine,People
from datetime import date, datetime
from sqlalchemy import Date,func

Session=sessionmaker(bind=engine)
session=Session()
#--------------- Student Access ---------------
def stu_insert():
    print("\nEnter Your Data 📜")
    
    name1=(input("\nEnter the Student name: ")).capitalize()
    gender1=input("Gender (M/F): ").capitalize()
    dob1=input("Date of Birth: (YYYY-MM-DD): ")
    department1=input("Department Name: ").capitalize()
    email1=input("Email: ")
    phone1=input("Phone Number: ")
    address1=input("Address: ").capitalize()
    dateofjoin_in=input("Date of Join: (YYYY-MM-DD): ")
    dateofjoin1 = datetime.strptime(dateofjoin_in, "%Y-%m-%d").date()
    users=session.query(People).filter(People.email==email1).first()
    if not users:
        users=People(name=name1,gender=gender1,dob=dob1,department=department1,email=email1,phone=phone1,address=address1,dateofjoin=dateofjoin1)
        session.add(users)
        session.commit()
        print(f"\n{name1} Data Inserted Sucessfully✅\n\n")
        print(f"{name1} | {gender1} | {dob1} | {department1} | {email1} | {phone1} | {address1} | {dateofjoin1}\n\n")
        
    else:
        print(f"\n ⚠️  {name1} Data already Exists in Database\nIf you want to Update the Data Choose the Update Menu\n\n")
    
def stu_view():
    print("\nNow You are in Display Dashboard 💻\n")
    specific_user=(input("Enter your Name: "))
    users=session.query(People).filter(People.name.ilike(specific_user)).first()
    i=users
    if users:
            print(f"\n Name: {i.name}\n Gender: {i.gender}\n Date Of Birth: {i.dob}\n Department: {i.department}\n Email: {i.email}\n Phone: {i.phone}\n Address: {i.address}\n Date of Join: {i.dateofjoin}\n\n")
    else:
        print(f"\n ⚠️  {specific_user.capitalize()} Data Not Exists\n\n")

def stu_update():
    print("\nNow You are in Update Dashboard ⬆️\n")
    update_user=input("Enter the Student Name: ")
    users=session.query(People).filter(People.name.ilike(update_user)).first()
    if users:
        print("What are the Fields you want to update")
        field_choice=int(input("Select your fields: \n 📧 Email = 1 \n 📞 Phone number = 2\n 🏠 Address =3\n Whether you want to update all fields = 4\nEnter Your Choice: "))
        if field_choice==1:
            users.email=input("New Email: ")
            print("\nEmail Updated Successfully 📧")
        elif field_choice==2:
             users.phone=input("New Phone Number: ")
             print("\nPhone Number Updated Successfully 📞")
        elif field_choice==3:
             users.address=input("New Address: ")
             print("\nAddress Updated Successfully 🏠")
        elif field_choice==4:
             users.email=input("New Email: ")
             users.phone=input("New Phone Number: ")
             users.address=input("New Address: ")
             print("\nAll Data Updated Successfully ✅")
        else:
             print(" ⚠️ Invalid Choice")
        session.commit()

    else:
        print(f"⚠️ {update_user.capitalize()} Doesn't Exist In the Database")

#--------------- Staff Access ---------------

def staff_insert():
    print("Whether you want to Insert \n1. Students Data (or)\n 2. Your Data")
    insert_data=int(input("Enter your Choice: "))
    if insert_data==1:
        print("\nEnter Your Data 📜")
        name1=(input("\nEnter the Student name: ")).capitalize()
        gender1=input("Gender (M/F): ").capitalize()
        dob1=input("Date of Birth: (YYYY-MM-DD): ")
        department1=input("Department Name: ").capitalize()
        email1=input("Email: ")
        phone1=input("Phone Number: ")
        address1=input("Address: ").capitalize()
        dateofjoin_in=input("Date of Join: (YYYY-MM-DD): ")
        dateofjoin1 = datetime.strptime(dateofjoin_in, "%Y-%m-%d").date()
        users=session.query(People).filter(People.email==email1).first()
        if not users:
            users=People(name=name1,gender=gender1,dob=dob1,department=department1,email=email1,phone=phone1,address=address1,dateofjoin=dateofjoin1,created_by="staff")
            session.add(users)
            session.commit()
            print(f"\n{name1} Data Inserted Sucessfully✅\n\n")
            print(f"{name1} | {gender1} | {dob1} | {department1} | {email1} | {phone1} | {address1} | {dateofjoin1}\n\n")
            
        else:
            print(f"\n ⚠️  {name1} Data already Exists in Database\nIf you want to Update the Data Choose the Update Menu\n\n")

    elif insert_data==2:
        print("\nEnter Your Data 📜")
        name1=(input("\nEnter your Name: ")).capitalize()
        gender1=input("Gender (M/F): ").capitalize()
        dob1=input("Date of Birth: (YYYY-MM-DD): ")
        department1=input("Department Name: ").capitalize()
        email1=input("Email: ")
        phone1=input("Phone Number: ")
        address1=input("Address: ").capitalize()
        dateofjoin_in=input("Date of Join: (YYYY-MM-DD): ")
        dateofjoin1 = datetime.strptime(dateofjoin_in, "%Y-%m-%d").date()
        users=session.query(People).filter(People.email==email1).first()
        if not users:
            users=People(name=name1,gender=gender1,dob=dob1,department=department1,email=email1,phone=phone1,address=address1,role="staff",dateofjoin=dateofjoin1,created_by="staff")
            session.add(users)
            session.commit()
            print(f"\n{name1} Data Inserted Sucessfully✅\n\n")
            print(f"{name1} | {gender1} | {dob1} | {department1} | {email1} | {phone1} | {address1} | {dateofjoin1}\n\n")
        else:
            print(f"\n ⚠️  {name1} Data already Exists in Database\nIf you want to Update the Data Choose the Update Menu\n\n")
    else:
         print("⚠️ Invalid Option")

def staff_view():
    print("Whether you want view your \n1. Students Data \n(or) \n2. Your Data")
    view_choice=int(input("Enter your Choice: "))
    if view_choice==1:
          view_stu=int(input("Whether you want to view\n 1. All Students in your Department\n (or)\n 2. Specific Student in your Department\n Enter your Choice: "))
          dept=input("Department Name: ")
          if view_stu==1:
            users=session.query(People).filter(People.department.ilike(dept)).all()
            if users:
                for i in users:
                    print(f" Name: {i.name}\n Gender: {i.gender}\n Date of Birth: {i.dob} Department: {i.department}\n Email: {i.email}\n Phone: {i.phone}\n Address: {i.address}\n Role: {i.role}\n Date of Join: {i.dateofjoin}")
            else:
                 print(f"⚠️  {dept} Not Exist in the Database")
          elif view_stu==2:
               stu_name=input("Student Name: ")
               users=session.query(People).filter(People.name.ilike(stu_name),People.department.ilike(dept)).first()
               i=users
               if users:
                    print(f" Name: {i.name}\n Gender: {i.gender}\n Date of Birth: {i.dob} Department: {i.department}\n Email: {i.email}\n Phone: {i.phone}\n Address: {i.address}\n Role: {i.role}\n Date of Join: {i.dateofjoin}")
               else:
                    print(f"⚠️  {stu_name} Data Not Found in {dept} Database")
    else:
        print("⚠️ Invalid Choice")

               
               
          
            
#     elif user_==2:
          
         
         

# def stu_delete():
#         print("Your are Now in the Delete Dashboard")
#         del_id=(input("Enter the name of the user: ")).lower()
#         users=session.query(People).filter(func.lower(People.name)==del_id).first()
#         if users:
#             session.delete(users)
#             session.commit()
#             print(f"{del_id} Data Deleted Successfully")
#         else:
#              print(f"{del_id} Not Exists in the Database")

# def view_all():
#      users=session.query(People).all()
#      data=[]
#      for i in users:
          
#           new_data=i.name,i.gender,i.department,i.email,i.address,i.dateofjoin
#           data.append(new_data)
#      print(data)


# # user_choice=int(input("\nAll users = 1\nSpecific user = 2\nEnter your option: "))
# #     if user_choice==1:
# #         users=session.query(People).all()
# #         for i in users:
# #             print(f" Name: {i.name}\n Gender: {i.gender}\n Department: {i.department}\n Email: {i.email}\n Phone: {i.phone}\n Address: {i.address}\n Role: {i.role}\n Date of Join: {i.dateofjoin}")
# #     elif user_choice==2: