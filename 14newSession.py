import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#
class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def showCustomerDetails(self):
        print(">> Name: {} Phone: {} Email:{}".format(self.name, self.phone, self.email))
# Use a service account
cred = credentials.Certificate('savefirebase.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
cRef = Customer("maxwell", "987745233642","maxwell12@gamilcom")

data = cRef.__dict__
db.collection("Customer").document().set(data)
print("done")
