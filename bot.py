from pyrogram import Client, Filters

app = Client('663574960:AAGWfrBnjGYGSczuGHGLG60RVLMp6ebWteM',605563,"7f2c2d12880400b88764b9b304e14e0b")



u = '-1001157455913'

s = '-1001171781537'


@app.on_message(Filters.chat(int(s))& Filters.text & ~Filters.edited)
def forward(client, message):
   
   mes = client.send_message(int(u), message.text + "-" + str(message.message_id) )
   file = open("sure.txt" , "r")
   lines = file.readlines()
   file.close()
   for line in lines:
         files = open("sure.txt" , "w")
         files.write( line + " " + str(message.message_id) +  " " + str(mes.message_id))
         files.close()
         
@app.on_message(Filters.chat( int(s))& Filters.text & Filters.edited )
def forward(client, message):
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   x = line.split()
   id = str(message.message_id)
   if id in x:
    client.edit_message_text(int(u),int(x[x.index(id)+1]), message.text)
  


@app.on_deleted_messages(int(s))
def forward(client, message):
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   x = line.split()
   id = str(message.message_id)
   if id in x:
     client.delete_messages(int(u),int(x[x.index(id)+1]))
  



    

app.run()
