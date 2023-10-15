import sqlite3
con=sqlite3.connect("student attendance.db")

def insert(reg_no,name,department,status):
    qry="insert into students(REG_NO,NAME,DEPARTMENT,STATUS)values (?,?,?,?);"
    con.execute(qry,(reg_no,name,department,status))
    con.commit()
    print("New Record added successfully...")

def update(name,department,status,reg_no):
    qry="update students set NAME=?,DEPARTMENT=?,STATUS=? WHERE REG_NO=?;"
    con.execute(qry,(name,department,status,reg_no))
    con.commit()
    print("Details are updated successfully...")
    
def remove(reg_no):
    qry="DELETE from students where REG_NO=?;"
    con.execute(qry,(reg_no,))
    con.commit()
    print("Deleted successfully..")
def show():
    qry=("select*from students;")
    result=con.execute(qry)
    con.commit()
    for i in result:
        print(i)
    
    

    
print("""
1.INSERT
2.UPDATE
3.REMOVE
4.SELECT
5.EXIT""")
while True:
         choice=int(input("Enter your choice :"))
         if choice==1:  
            print("Add new record:")
            reg_no=int(input("Enter your Register number:"))
            name=input("Enter your name:")
            department=input("Enter your Department:")
            status=input("Enter your status(Present (or) Absent):")
            insert(reg_no,name,department,status)
            
         elif choice==2:
            print("Update your record :")
            reg_no=int(input("Enter your Register number:"))
            name=input("Enter your New name:")
            department=input("Enter your Department:")
            status=input("Enter your status(Present (or) Absent):")
            update(name,department,status,reg_no)

         elif choice==3:
            print("Delete the record:")
            reg_no=int(input("Enter your Register number:"))
            remove(reg_no)
            
         elif choice==4:
            print("The existing records are:")
            show()
            
         elif choice==5:
            exit()
         else:
            print("You selected wrong choice,Try again!")
print("Thank you")            

