import requests

word = input("Enter the word : ");

request = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
data = request.json();
meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
print(f"The actual meaning of '{word}' : {meaning}")