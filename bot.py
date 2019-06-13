from pyrogram import Client, Filters, DeletedMessagesHandler
import time
 

TOKAN = "663574960:AAGWfrBnjGYGSczuGHGLG60RVLMp6ebWteM"

app = Client( TOKAN ,605563,"7f2c2d12880400b88764b9b304e14e0b")

u = '-1001157455913'
s = '-1001171781537'


@app.on_message(Filters.chat(int(s))& Filters.text & ~Filters.edited)
def forward(client, message):
   m = client.send_message(int(u), "1")
   time.sleep(3)
   client.edit_message_text(int(u), m.message_id, "2")
   time.sleep(3)
   client.edit_message_text(int(u), m.message_id, "3")
   time.sleep(3)
   client.edit_message_text(int(u), m.message_id, "4")
   time.sleep(3)
   client.edit_message_text(int(u), m.message_id, "5")
   time.sleep(3)
   client.edit_message_text(int(u), m.message_id, "6")
   time.sleep(3)
   client.edit_message_text(int(u), m.message_id, "7")
   time.sleep(3)
   client.edit_message_text(int(u), m.message_id, "8")
  
       





time.sleep(1)
app.run()
