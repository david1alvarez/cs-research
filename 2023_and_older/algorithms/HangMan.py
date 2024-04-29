"""
post request body is in json
post body is expecting a stringified JSON

vasili@crowdai.com

3:45pm

https://hangman.crowdai.com/api.txt
"""
import requests
response = requests.get("https://hangman.crowdai.com/wordlist.txt")
print(response.json())

# async function getWords() {
#     let response = await fetch("https://hangman.crowdai.com/wordlist.txt")
#     console.log(response)
# }

# getWords()