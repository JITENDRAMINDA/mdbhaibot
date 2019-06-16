from pyrogram import Client, Filters
import time

TOKAN = "663574960:AAGWfrBnjGYGSczuGHGLG60RVLMp6ebWteM"

app = Client( TOKAN ,605563,"7f2c2d12880400b88764b9b304e14e0b")



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
    for x in p:
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
 v = file.readlines()
 file.close()
 x = v.split() 
 print(x)
 del x[x.index(message.text.split(' ')[1])]
 files = open("sure.txt" , "w") 
 files.write(x)
 files.close()
 
  
@app.on_message(Filters.command('sets'))
def forward(client, message):
 with open('sue.txt', 'w') as file:

  file.write(message.text.split(' ')[1])
  file.close()
  message.reply("Done, Now my source chat - " + message.text.split(' ')[1])

app.run()
