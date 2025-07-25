phonebook = {}
def add_contact () :
    name = input ("enter name . :").strip()
    number = input ("enter phone number. :").strip()
    if name in phonebook :
        print("contact already exist")
    else :
        phonebook [ name ] = number
        print(f"contact '{name}' added .")
def search_contact():
            name = input ("enter name to search . :").strip()
            if name in phonebook :
                print(f"{name} :{phonebook [name]}")
            else :
                print("contact not found")
def delete_contact():
     name = input ("enter name to delete . :").strip()
     if name in phonebook :
          del phonebook [name]
          print(f"contact'{name}' deleted")
     else :
          print ("contact not found")
def display_contact ():
     if not phonebook:
          print("phonebook is empty")
     else :
          print("contacts")
          for name,number in phonebook.items():
               print(f"{name}: {number}")
def main():
                    while True:
                         print("/n---phonebook menu----")
                         print("1:add contact")
                         print("2:search contact")
                         print("3:delete contact")
                         print("4:display all contacts")
                         print("5:exit")
                         choice = input("choose an option (1-5):").strip()
                         if choice =='1':
                              add_contact()
                         elif choice =='2':
                              search_contact()
                         elif choice =='3':
                            delete_contact()
                         elif choice =='4':
                              display_contact()
                         elif choice =='5':
                              print ("exiting phonebook.Goodbye!")
                              break
                         print("invalid option.pls try again")
main()