from pyrogram import Client, Filters
import time

TOKAN = "639957559:AAFbwAStH_GXBgUVFxC93CCsbBM5MSA-Piw"

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
 if message.from_user.id == 491634139:

  if len(message.text.split(' ')[1]) == 14:
   file = open("sure.txt" , "r")
   lines = file.readlines()
   file.close()
   for line in lines:
    files = open("sure.txt" , "w") 
    files.write(line + " " + message.text.split(' ')[1])
    files.close()
    message.reply("💾 Done, The chat_id  ```" + message.text.split(' ')[1] +"```🌐 has been added to my database. ✅✅")
  else:
   message.reply("💼 Please write a valid chat id. ✅✅ ")

@app.on_message(Filters.command('remove'))
def forward(client, message):
 if message.from_user.id == 491634139:

  if len(message.text.split(' ')[1]) == 14:
   file = open("sure.txt" , "r")
   u = file.readlines()
   file.close()
   for v in u:
    print(v)
    lines = v.split() 
    del lines[lines.index(message.text.split(' ')[1])]
    y = " ".join(str(x) for x in lines)
    files = open("sure.txt" , "w") 
    files.write(y)
    files.close()
    message.reply("💾 Done, The chat_id  ```" + message.text.split(' ')[1] +"```🌐 has been removed to my database. ✅✅")
  else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")

@app.on_message(Filters.private)
def forward(client, message):
 if not message.from_user.id == 491634139:
   message.reply("♻️ You need admins permission to use my functions. ✅✅")
 

@app.on_message(Filters.command("start"))
def forward(client, message):
 if not message.from_user.id == 491634139:
   message.reply("♻️ Welcome to your LineBot . ✅✅")
 else:
   message.reply("♻️ You need admins permission to use my functions. ✅✅")
 
  
@app.on_message(Filters.command('list'))
def forward(client, message):
 if message.from_user.id == 491634139:

  file = open("sure.txt" , "r")
  u = file.readlines()
  file.close()
  for v in u :
    message.reply("🏘️ List of Chat_ids in my database are ```" + str(v) + "```. Its can be change. ✅✅")
  
 
@app.on_message(Filters.command('sets'))
def forward(client, message):
 if message.from_user.id == 491634139:

  if len(message.text.split(' ')[1]) == 14:
   with open('sue.txt', 'w') as file:
    file.write(message.text.split(' ')[1])
    file.close()
    message.reply("🌐 Done, Now my source chat is ```" + message.text.split(' ')[1] + "```. I will try to forward messages from this chat. ✅✅")
  else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")

app.run()
