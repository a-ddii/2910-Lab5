import requests
import json

monster = input("What monster do you want: ")

URL = f"https://www.dnd5eapi.co/api/monsters/{monster}"
user_response = requests.get(URL)

if user_response.status_code == 200:
    data = user_response.json() 
else:
    print(f"Failed to retrieve data. Status code: {user_response.status_code}")
    data = None

if data:
    with open(f'{monster}.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data successfully written to '{monster}.json'")

rank = input("What rank would you want to put them in your list? ")
user_response = int

ranked = input(f"That monster has been put at rank #{rank}. ")
answer = input ("Would you like another monster? Yes or No: ")
if answer == "Yes":
    monster = input("What monster do you want: ")
    URL = f"https://www.dnd5eapi.co/api/monsters/{monster}"
    user_response = requests.get(URL)
    rank = input("What rank would you want to put them in your list? ")
  
    
elif answer == "No":
    print("Understandable. See you later :). ")

else:
    print("See you later :). ")
    exit



#if ranked == yes:
#####print("Understandable. See you later :). ")