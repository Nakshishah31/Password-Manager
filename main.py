import csv
from cryptography.fernet import Fernet
import os
file1='\'passwd.csv\''
file2='\'passwd_edit.csv\''
def key():

    return Fernet.generate_key()



def save(key1,cat,tit,passwd):
    f=Fernet(key1)

    encrypt=f.encrypt(passwd.encode())
    file_exists=os.path.exists('passwd.csv')
    with open(file1,mode='a',newline='') as file:
        filedname=[cat,tit,encrypt]
        writer=csv.DictWriter(file,fieldnames=filedname)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'cat':cat,'tit':tit,'encrypt':encrypt})

        file.close()


def remove(cat,tit):
    print(2)
    with open(file1,mode="r") as inp, open(file2,mode='a',newline='') as op:
        writer=csv.writer(op)
        for row in csv.reader(inp):
            if row[1]!=cat and row[2]!=tit:
                writer.writerow(row)
                return 0




def disp():
    print(3)

print("<---------------------------------------------->")
print("<--------- Welcome To Password Manager -------->")
print("<---------------------------------------------->")

key1=key()

while True:
    print("1.Save New Password\n2.Remove From Saved Passwords\n3.Display Password\n4.Exit")
    ch=int(input(("Enter Choice: ")))
    match ch:
        case 1:
            cat=input("Enter Cstegory To Save Password:")
            tit=input("Enter Title To Save Password:")
            passwd=input("Enter Password:")
            save(key1,cat,tit,passwd)
        case 2:
            cat1=input("Enter Category To Delete Password:")
            tit1=input("Enter Title To Delete Password:")
            val=remove(cat1,tit1)
            if val==0:
             print("Password Succesfully Removed...")

            else:
                print("No Password Found...")
        case 3:
            disp() 
        case 4:
            print("Thanks For Visiting Our Password Manager.....")
            break
