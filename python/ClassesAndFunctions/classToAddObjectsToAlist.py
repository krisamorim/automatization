
########## Just one classe without  return ################

class Contact:
    def __init__(self,id,name,email,phonenumber):
        """
        class to receive the values and return the object
        """
        self.id=id
        self.name=name
        self.email=email
        self.phonenumber=phonenumber

list = []  
list.append( Contact(1,'kris', 'kris@email.com', 11111111)) 
list.append( Contact(2,'Ana', 'ana@email.com', 22222222)) 

for obj in list: 
    print( obj.id, obj.name, sep =' ' )




########## With two classes without return ################
# class numb:  
#     def __init__(self, num1, num2):  
#         self.x = num1  
#         self.y = num2 
          
#     def Sum(self): 
#         print( self.num1 + self.num2 ) 
   
# list = []  
# list.append(numb(1, 3)) 
# list.append(numb(2, 2)) 
# list.append(numb(10, 30)) 
  
# for obj in list: 
#     obj.Sum() 



########## With two classes and return ################
# class Contact:
#     def __init__(self,id,name,email,phonenumber):
#         """
#         class to receive the values and return the object
#         """
#         self.id=id
#         self.name=name
#         self.email=email
#         self.phonenumber=phonenumber
#     def toString(self):
#         return {'id': self.id, 'name':self.name, 'email':self.email, 'phonenumber': self.phonenumber}

# class ContactList:
#     """
#     class to add aboject to a list
#     """
#     listCont = []
#     def addContact(self, object):
#         self.listCont.append(object)

# add = ContactList()
# add.addContact(Contact(1,"Kris", "kri@email.com", 11111111).toString())
# add.addContact(Contact(2,"Ana", "ana@email.com", 22222222).toString())
# add.addContact(Contact(3,"Marlene", "marlene@email.com", 33333333).toString())


# print(ContactList.listCont)#Show contac list

# print("")#break line

# print(ContactList.listCont[0]['name'])#Show 1st element's name