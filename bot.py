from pyrogram import Client, Filters, DeletedMessagesHandler
import time
 

TOKAN = "663574960:AAGWfrBnjGYGSczuGHGLG60RVLMp6ebWteM"

app = Client( TOKAN ,605563,"7f2c2d12880400b88764b9b304e14e0b")

u = '-1001157455913'
s = '-1001171781537'

@app.on_message(Filters.channel)
def main(client, message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  p = line.split()
  id = str(message.chat.id)
  if id in p:
   client.send_message(int(p[p.index(id)+1]), "**" + message.text + "**" )



@app.on_message(Filters.command('add'))
def forward(client, message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  files = open("sure.txt" , "w") 
  files.write( line + " " + message.text.split(' ')[1] + " " + message.text.split(" ")[2])
  files.close()
  message.reply("done")





app.run()
