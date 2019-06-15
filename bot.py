from pyrogram import Client, Filters, DeletedMessagesHandler
import time
 

TOKAN = "663574960:AAGWfrBnjGYGSczuGHGLG60RVLMp6ebWteM"

app = Client( TOKAN ,605563,"7f2c2d12880400b88764b9b304e14e0b")


@app.on_message(Filters.command('add')& Filters.user(491634139))
def handle(client, message):
    global to_chat 
    to_chat = message.command[2]
    client.add_handler(MessageHandler(han, Filters.chat(message.command[1]& Filters.text)))



def han(client, message):
    global to_chat
    client.send_message(int(to_chat), message.text)





app.run()
