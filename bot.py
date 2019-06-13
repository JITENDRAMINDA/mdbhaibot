from pyrogram import Client, Filters, DeletedMessagesHandler
import time
 

TOKAN = "663574960:AAGWfrBnjGYGSczuGHGLG60RVLMp6ebWteM"

app = Client( TOKAN ,605563,"7f2c2d12880400b88764b9b304e14e0b")

u = '-1001157455913'
s = '-1001171781537'


@app.on_message(Filters.chat(int(s))& Filters.text & ~Filters.edited)
def forward(client, message):
   x = time.time()
   client.send_message(int(u), message.text + "-" + str(message.message_id) )
   print("z")
   time.sleep(1)
  
       





time.sleep(1)
app.run()
