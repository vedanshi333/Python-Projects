print("********* Phone Contact book *********\n")
contact={"Vedanshi":'036912','Vishnu':'36912'}
def displayall():
    print("Name\t : \tContact")
    for key in contact:
        print("{}\t : \t{}".format(key,contact.get(key)))
              
while 1 :
    print("Enter a choice\n 1.Add a new contact\n 2.Select a contact\n 3.Display a contact\n 4.Edit a contact\n 5.Delete a contact\n 6.Exit")
    choice=int(input("\n Enter a choices"))
    if choice==1:
        name=input("Enter a name\n")
        phoneno=input("Enter a phone number\n")
        contact[name]=phoneno
    elif choice==2:
        selectname=input("Select a name\n")
        if selectname in contact:
            print(selectname +":" + phoneno)
        else:
            print("Not found")
    elif choice==3:
        displayall()
    elif choice==4:
        opt=int(input("Enter a choice\n 1.Edit number\n 2.Edit name"))
        if opt==1:
            editno=input("Enter the name whose contact is to be edited ")
            cnumber=input("Enter the number")
            contact[editno]=cnumber
        else:
            editname=input("Enter the name to be edited")
            newname=input ("New namme is")
            editname=newname 
            contact[newname]=number
    elif choice==5:
        deleteno=input("Enter a contact which is to be deleted ")
        contact.pop(deleteno)
    else:
        break
