from django.test import TestCase,Client
import random

# Create your tests here.

#Lassen Sie uns das Kontoerstellungsformular testen

tester = Client()

response = tester.get('register')

print(response.json())

# response = tester.post('/register/',{"username":"testnumber"+str(random.randint(0,155555555555555)),"password":"test","confirm":"test"})

# print(response.status_code)