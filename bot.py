from pyrogram import Client, Filters, DeletedMessagesHandler
import time
 

TOKAN = "663574960:AAGWfrBnjGYGSczuGHGLG60RVLMp6ebWteM"

app = Client( TOKAN ,605563,"7f2c2d12880400b88764b9b304e14e0b")

u = '-1001157455913'
s = '-1001171781537'

@app.on_message(Filters.chat(int(s)))
def main(client, message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  p = line.split()
  for x in p:
   print(str(p))
   client.send_message(x , "**" + message.text + "**" )



@app.on_message(Filters.command('add'))
def forward(client, message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  files = open("sure.txt" , "w") 
  files.write( line + " " + message.text.split(' ')[1] + " " + message.text.split(" ")[2])
  files.close()
  message.reply(line)
  print("done")





app.run()
