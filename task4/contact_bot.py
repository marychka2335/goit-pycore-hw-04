def add_contact(args, contacts):
    if len(args) != 2:
             return "Error: Provide name and phone number."
    name, phone = args
    if name in contacts:
        return f"The name {name} is already exists on your contacts list."
    else:
        contacts[name] = phone
        return "Contact added."
    

def change_contact(args, contacts):
    if len(args) != 2:
             return "Error: Provide name and phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"The name {name} is not on your contacts list yet."          

def get_contact(args, contacts):
    if len(args) != 1:
             return "Error: Provide a name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else: 
        return f"The name {name} is not on your contacts list yet." 
        
    
def get_all_contacts(contacts):
    res = ""  

    if len(contacts) == 0:
        return "Your contact list is empty."
    else:
        for name, phone in contacts.items():
            res += f"{name}: {phone} \n"
        return res.rstrip("\n")  
