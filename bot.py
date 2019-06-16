from pyrogram import Client, Filters, DeletedMessagesHandler, MessageHandler
import time
 

TOKAN = "663574960:AAGWfrBnjGYGSczuGHGLG60RVLMp6ebWteM"

app = Client( TOKAN ,605563,"7f2c2d12880400b88764b9b304e14e0b")


u = '-1001157455913'
s = '-1001171781537'

@app.on_message(Filters.channel)
def main(client, message):
 file = open("sue.txt" , "r")
 s = file.readlines()
 file.close()
 for d in s:
  if message.chat.id == int(d):
   file = open("sure.txt" , "r")
   lines = file.readlines()
   file.close()
   for line in lines:
    p = line.split()
    z = [int(i) for i in p]
    for x in p:
     print (z)
     client.send_message( int(x), "**" + message.text + "**" )



@app.on_message(Filters.command('add'))
def forward(client, message):
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   files = open("sure.txt" , "w") 
   files.write(line + " " + message.text.split(' ')[1])
   files.close()
   message.reply(line + " " + message.text.split(' ')[1])
   

@app.on_message(Filters.command('remove'))
def forward(client, message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  x = line.split() 
  del x[x.index(message.text.split(' ')[1])]
  files = open("sure.txt" , "w") 
  files.write( x + " " + message.text.split(' ')[1])
  files.close()
  print (x)
  
@app.on_message(Filters.command('sets'))
def forward(client, message):
 file = open("sue.txt" , "r")
 file.write(message.text.split(' ')[1])
 file.close()
 message.reply("done")

app.run()
