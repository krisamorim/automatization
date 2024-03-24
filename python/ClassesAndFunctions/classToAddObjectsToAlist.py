class Contact:
    def __init__(self,id,name,email,phonenumber):
        """
        class to receive the values and return the object
        """
        self.id=id
        self.name=name
        self.email=email
        self.phonenumber=phonenumber
    def toString(self):
        return {'id': self.id, 'name':self.name, 'email':self.email, 'phonenumber': self.phonenumber}

class ContactList:
    """
    class to add aboject to a list
    """
    listCont = []
    def addContact(self, object):
        self.listCont.append(object)

add = ContactList()
add.addContact(Contact(1,"Kris", "kri@email.com", 11111111).toString())
add.addContact(Contact(2,"Ana", "ana@email.com", 22222222).toString())
add.addContact(Contact(3,"Marlene", "marlene@email.com", 33333333).toString())


print(ContactList.listCont)#Show contac list

print("")#break line

print(ContactList.listCont[0]['name'])#Show 1st element's name