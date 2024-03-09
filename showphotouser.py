import requests

chat_id = "6646979569"
urlp = "https://t.me/elhyba"
url = f"https://api.telegram.org/bot 7095650662:AAEYj-8VyfwH_oknmrT4ToBUE9Hpxrm--Dw/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
