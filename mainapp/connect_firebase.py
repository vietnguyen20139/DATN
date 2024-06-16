# Imports
#-------------------------------------------------------------------------------
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDmCd14uqnf0Z5d6bnrm9OnWlU9OJRrJl4",
    "authDomain": "datn-43437.firebaseapp.com",
    "databaseURL": "https://datn-43437-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "datn-43437",
    "storageBucket": "datn-43437.appspot.com",
    "messagingSenderId": "529783414922",
    "appId": "1:529783414922:web:d989ca2ddb7825199e8d73",
    "measurementId": "G-FF9SLCD8BX"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def setDriverToFirebase(data, link):
    db.child(link).set(data)

def loadDataFromFirebase(link):
    return db.child(link).get() 

def deleteDataToFirebase(link):
    db.child(link).remove()

# data = {"Age": 21, "Name": "Jenna", "Employed": True}
# #-------------------------------------------------------------------------------
# # Create Data

# # db.push(data)
# db.child("test1").child("FirstPerson").set(data)

# #-------------------------------------------------------------------------------
# # Read Data

# jenna = db.child("Users").child("FirstPerson").get()
# print(jenna.val())
#-------------------------------------------------------------------------------
# Update Data

# db.child("Users").child("FirstPerson").update({"Name": "Larry"})

#-------------------------------------------------------------------------------
# Remove Data

#Delete 1 Value
# db.child("Users").child("FirstPerson").child("Age").remove()

# Delete whole Node
db.child("Users").child("FirstPerson").remove()

#-------------------------------------------------------------------------------