from pyrogram import Client, Filters, DeletedMessagesHandler
import time

app = Client('663574960:AAGWfrBnjGYGSczuGHGLG60RVLMp6ebWteM',605563,"7f2c2d12880400b88764b9b304e14e0b")



u = '-1001157455913'

s = '-1001171781537'

app.add_handler(DeletedMessagesHandler(callable))


@app.on_message(Filters.chat(int(s))& Filters.text & ~Filters.edited)
def forward(client, message):
  x = time.time()
  files = open("sure.txt" , "w")
  files.write(str(x))
  files.close()
       





def main(client, message):
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  z = time.time() - int(x)
  time.sleep(1)
  for line in lines:
   if z < 30:
      client.send_message(int(u), message.text + "-" + str(message.message_id) )
      print(z)
      time.sleep(1)

         

app.run()
