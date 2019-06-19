from pyrogram import Client, Filters

TOKAN = "639957559:AAFbwAStH_GXBgUVFxC93CCsbBM5MSA-Piw"

app = Client( TOKAN ,605563,"7f2c2d12880400b88764b9b304e14e0b")

@app.on_message(Filters.command("delete"))
def main(client, message):
  for message.message_id in range(int(message.text.split(' ')[1]), int(message.text.split(' ')[2])):
    try:
        client.delete_messages(message.chat.id,message.message_id)
    except:
        continue

@app.on_message(Filters.channel & ~ Filters.edited)
def main(client, message):
  file = open("bullets.txt" , "r")
  s = file.readlines()
  file.close()
  for d in s:
   if message.chat.id == int(d):
    file = open("bulleti.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
     p = line.split()
     for x in p:
       try:
          mes = client.send_message( int(x), "**" + message.text + "**" )
          fille = open(str(x)+".txt","r")
          n = fille.readlines()
          fille.close()
          for t in n:
           fie = open(str(x)+".txt","w")
           fie.write(t +" " + str(message.message_id) + " " + str(mes.message_id))
           fie.close()
       except:
           continue

  fil = open("ferraris.txt" , "r")
  q = fil.readlines()
  fil.close()
  for e in q:
   if message.chat.id == int(e):
    file = open("ferrarii.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
     p = line.split()
     for x in p:
       try:
          mes = client.send_message( int(x), "**" + message.text + "**" )
          fille = open(str(x)+".txt","r")
          n = fille.readlines()
          fille.close()
          for t in n:
           fie = open(str(x)+".txt","w")
           fie.write(t +" " + str(message.message_id) + " " + str(mes.message_id))
           fie.close()
       except:
           continue
  fi = open("sessionss.txt" , "r")
  h = fil.readlines()
  fi.close()
  for e in h:
   if message.chat.id == int(e):
    file = open("sessionsi.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
     p = line.split()
     for x in p:
       try:
          mes = client.send_message( int(x), "**" + message.text + "**" )
          fille = open(str(x)+".txt","r")
          n = fille.readlines()
          fille.close()
          for t in n:
           fie = open(str(x)+".txt","w")
           fie.write(t +" " + str(message.message_id) + " " + str(mes.message_id))
           fie.close()
       except:
           continue


  
@app.on_message(Filters.channel & Filters.edited)
def main(client, message):
  file = open("ferraris.txt" , "r")
  s = file.readlines()
  file.close()
  for d in s:
   if message.chat.id == int(d):
    filer = open("update.txt" , "r")
    m = filer.readlines()
    filer.close()
    for l in m:
     if l == "on":
      file = open("ferrarii.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
       p = line.split()
       for o in p:
        files = open(str(o)+".txt" , "r")
        d = files.readlines()
        files.close()
        for c in d:
         x = c.split()
         id = str(message.message_id)
         if id in x:
           try:
             client.edit_message_text(int(o),int(x[x.index(id)+1]), "**" + message.text + "**" )
           except:
             continue
          

  fil = open("bullets.txt" , "r")
  f = file.readlines()
  fil.close()
  for d in f:
   if message.chat.id == int(d):
    filer = open("update.txt" , "r")
    m = filer.readlines()
    filer.close()
    for l in m:
     if l == "on":
      file = open("bulleti.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
       p = line.split()
       for o in p:
        files = open(str(o)+".txt" , "r")
        d = files.readlines()
        files.close()
        for c in d:
         x = c.split()
         id = str(message.message_id)
         if id in x:
           try:
             client.edit_message_text(int(o),int(x[x.index(id)+1]), "**" + message.text + "**" )
           except:
             continue
 
  fl = open("sessionss.txt" , "r")
  f = file.readlines()
  fl.close()
  for d in f:
   if message.chat.id == int(d):
    filer = open("update.txt" , "r")
    m = filer.readlines()
    filer.close()
    for l in m:
     if l == "on":
      file = open("sessionsi.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
       p = line.split()
       for o in p:
        files = open(str(o)+".txt" , "r")
        d = files.readlines()
        files.close()
        for c in d:
         x = c.split()
         id = str(message.message_id)
         if id in x:
           try:
             client.edit_message_text(int(o),int(x[x.index(id)+1]), "**" + message.text + "**" )
           except:
             continue
                
     

@app.on_message(Filters.command('add') & Filters.user(491634139) )
def forward(client, message):
 if len(message.text.split(' ')) > 2:
  if len(message.text.split(' ')[1]) == 14:
   with open(message.text.split(" ")[2] + ".txt" , "r") as file:
    lines = file.readlines()
    file.close()
    for line in lines:
     files = open(message.text.split(" ")[2] + ".txt" , "w") 
     files.write(line + " " + message.text.split(' ')[1])
     files.close()
     with open(message.text.split(' ')[1]+".txt" , "w") as g:
       g.write("001 002")
       g.close()
     message.reply("💾 Done, The chat_id  ```" + message.text.split(' ')[1] +"```🌐 has been added to my database. ✅✅")
  else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
   message.reply("💼 Please write a valid chat id. ✅✅ ")


@app.on_message(Filters.command('remove') & Filters.user(491634139))
def forward(client, message):
 if len(message.text.split(' ')) > 2:
  if len(message.text.split(' ')[1]) == 14:
   file = open(message.text.split(" ")[2] + ".txt" , "r")
   u = file.readlines()
   file.close()
   for v in u:

     lines = v.split() 
     del lines[lines.index(message.text.split(' ')[1])]
     y = " ".join(str(x) for x in lines)
     files = open(message.text.split(" ")[2] + ".txt" , "w") 
     files.write(y)
     files.close()
     message.reply("💾 Done, The chat_id  ```" + message.text.split(' ')[1] +"```🌐 has been removed to my database. ✅✅")
  else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")

@app.on_message(Filters.command('clear') & Filters.user(491634139))
def forward(client, message):
    file = open(message.text.split(" ")[1] + ".txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
     p = line.split()
     for x in p:
        fie = open(str(x)+".txt","w")
        fie.write("001 002")
        fie.close()
        message.reply("☢️ Done, Editing data cleared ✅✅")



@app.on_message(Filters.command('list') & Filters.user(491634139))
def forward(client, message):
  file = open(message.text.split(" ")[1] + ".txt" , "r")
  u = file.readlines()
  file.close()
  for v in u :
      message.reply("🏘️ List of Chat_ids in my database are ```" + str(v) + "```. Its can be change. ✅✅")
  
 
@app.on_message(Filters.command('sets') & Filters.user(491634139) )
def forward(client, message):
 if len(message.text.split(' ')) > 2:
  if len(message.text.split(' ')[1]) == 14:
   with open(message.text.split(' ')[2] + '.txt', 'w') as file:
    file.write(message.text.split(' ')[1])
    file.close()
    message.reply("🌐 Done, Now my source chat is ```" + message.text.split(' ')[1] + "```. I will try to forward messages from this chat. ✅✅")
  else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")

   
@app.on_message(Filters.command('setupdate') & Filters.user(491634139) )
def forward(client, message):
 if len(message.text.split(' ')) > 1:
   with open('update.txt', 'w') as file:
    file.write(message.text.split(' ')[1])
    file.close()
    message.reply("🌐 Done,Now my message update status is ```" + message.text.split(' ')[1] + "```.✅✅")
 else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")


@app.on_message(Filters.command('source') & Filters.user(491634139) )
def forward(client, message):
   with open(message.text.split(" ")[1] + '.txt', 'r') as file:
    x = file.readlines()
    file.close()
    for y in x:
     message.reply("🌐 My source chat is ```" + y + "```. I am trying to forward messages from this chat. ✅✅")
 
@app.on_message(Filters.command('get') & Filters.user(491634139) )
def forward(client, message):
 if len(message.text.split(' ')) > 1:
  if len(message.text.split(' ')[1]) == 14:
      x = client.get_chat(int(message.text.split(' ')[1])).title
      message.reply("📶 This chat name is - "+str(x)+" ✅")
  else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")

@app.on_message(Filters.command('update') & Filters.user(491634139) )
def forward(client, message):
    with open('update.txt', 'r') as file:
     x = file.readlines()
     file.close()
     for y in x:
       message.reply("🌐 My current message update status is ```" + y + "```. ✅✅")
 
@app.on_message(Filters.command("start"))
def forward(client, message):
 if message.from_user.id == 491634139:
   message.reply("♻️ Welcome to your LineBot . ✅✅")
 else:
   message.reply("♻️ You need admins permission to use my functions. ✅✅")
  
  
  

                 
    
@app.on_message(Filters.private)
def forward(client, message):
 if not message.from_user.id == 491634139:
   message.reply("♻️ You need admins permission to use my functions. ✅✅")
 


  
app.run()
