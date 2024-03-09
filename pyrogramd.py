from pyrogram import Client, filters

bot_token = "7095650662:AAEYj-8VyfwH_oknmrT4ToBUE9Hpxrm--Dw"

api_id = 22523706
api_hash = "6c96d6adf05692af62edaa36cc41a457"
app = Client("nb", api_id, api_hash, bot_token=7095650662:AAEYj-8VyfwH_oknmrT4ToBUE9Hpxrm--Dw)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()

