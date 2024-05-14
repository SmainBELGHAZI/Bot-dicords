import discord
import os
from discord import app_commands
from discord.ext import commands
import psycopg2

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True
intents.members = True
intents = discord.Intents.all()

#connexion à la base de donnèes 
con = psycopg2.connect(  #connexion BDDos.environ['database']
     database=os.environ['database'], user=os.environ['user'], password=os.environ['password'], host=os.environ['host'], port=os.environ['port']
 )
#ouverteure du curseur qui permet d'executer les requêtes sql

bot = commands.Bot(command_prefix='/', intents=intents)
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
intents = discord.Intents.all()
intents.members=True


@bot.event #à chaque message enregistre le message dans la base de données et si l'user le canal ou le serveur est inconnus l'inclus dans la BDD aussi
async def on_message(message):

 id_user = message.author.id #récupere l'id user
 nom = message.author.name #recuper nom_user
 content = message.content #récupére le contenue du meesage
 serv = message.guild.id #recuper id_serveur
 servname = message.guild.name # recuperer nom_serveur
 discri = message.author.discriminator #rcupere le discriminant
 namechan = message.channel.name  #recupere le canal
 heuremess = message.created_at #récupere l'heure date etc
 heure =heuremess.isoformat(timespec='seconds') #isole l'heure
 heurfinal =heure.split("T")[1][:8] # je la mets sous le format HH:MM:SS
 datemess = message.created_at.date() #recuperer la date

 print(datemess)
 print(heurfinal)
 print(namechan)
 print(servname)
 print(serv)
 print(nom)
 print(id_user)
 print(discri)
 print (content)

 cursor1 = con.cursor()
 compteurmess= "SELECT COUNT(corp) FROM public.messages" #requete sql qui permet de recupere le nb de ligne dans la collonne corpd de la BDD
 cursor1.execute(compteurmess)
 afcompteurmess = cursor1.fetchone()[0]   #recupere le nombre de ligne
 print(afcompteurmess+1)                  #ajoute 1 pour avoir le nombre de message avec celui qui vient d'etre envoyer
 boolserv = False  # variable boolean qui vont definir si O/N +BDD
 booluser = False
 boolcanal = False
 selectServ = 'SELECT nom_serveur FROM serveur'  # recupère tout les nom de serveur
 cursor1.execute(selectServ)
 resserv = cursor1.fetchall()   # récuperer tout les élement de la BDD
 compteur = 0
 print(resserv)
 for i in resserv:
     resserv1 = i[0]         #convertire  la valeur de la BDD en str
     if resserv1 == str(servname):    #si l'element dans la BDD = nom du serveur = TRUE
         boolserv = True
         print('ok')
         print(boolserv)
     else:  compteur+1
 selectCanal = 'SELECT nom_canal FROM public."Canal"'  # recupère tout les nom de Canal dans la BDD
 cursor1.execute(selectCanal)
 resCanal = cursor1.fetchall()  # récuperer tout les élement de la BDD
 compteur1 = 0
 compteurmess = 0 #pour compter les messages dans la BDD
 print(resCanal)
 for i in resCanal:
     resCanal1 = i[0]  # convertire  la valeur de la BDD en str
     if resCanal1 == str(namechan):  # si l'element dans la BDD = nom du serveur = TRUE
         boolcanal= True
         print('ok')
         print(boolcanal)
     else:
         compteur1 + 1
 selectUser = 'SELECT nom_user FROM public."User"'  # recupère tout les nom de User dans la BDD
 cursor1.execute(selectUser)
 resUser = cursor1.fetchall()  # récuperer tout les élement de la BDD
 compteur2 = 0
 print(resUser)
 for i in resUser:
     resUser2 = i[0]  # convertire  la valeur de la BDD en str
     print(resUser2)
     print(nom)
     if resUser2 == str(nom) :  # si l'element dans la BDD = nom du serveur = TRUE
         booluser = True
         print('ok')
         print(booluser)
     else:
         compteur2 + 1
 if boolserv == False :  #si dans la liste de serveur le serveur n'est pas present il ne rentre pas dans la condition précedente et donc = False donc il entre et execute la requete
     sql ="INSERT INTO public.serveur (id_serveur,nom_serveur) VALUES (%s,%s)"  #requete d'insertion
     values = (message.guild.id,message.guild.name )  #valeur %s
     cursor1.execute(sql,values)   # insertion dans la table
     con.commit()  #sauvegarde
 if booluser == False:
     sql1 = "INSERT INTO public.\"User\" (id_user, nom_user, siscriminant) VALUES (%s, %s, %s)"  # Utilisation de guillemets pour "User" car c'est un mot réservé
     values1 = (message.author.id, message.author.name,
                message.author.discriminator)  # Utilisation de message.author.name pour obtenir le nom de l'utilisateur
     cursor1.execute(sql1, values1)
     con.commit()  #  valider la transaction avec commit()
 if boolcanal == False:
     compteur2+1
     sql2 = "INSERT INTO public.\"Canal\" (id_canal,nom_canal) VALUES (%s,%s) "
     values2 = (message.channel.id, message.channel.name)
     cursor1.execute(sql2, values2)
     con.commit()

 compteurmess =compteurmess+1
 sql3 = "INSERT INTO public.messages (id_message,corp,discriminant,id_user,id_serveur,id_canal,date,heure,compteur,name,id_channel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
 values3= (message.id,message.content,message.author.discriminator,message.author.id,message.guild.id,message.channel.id,message.created_at.date(),heurfinal,afcompteurmess+1,message.author.name,message.channel.id)
 cursor1.execute(sql3,values3)
 con.commit()

 print(str(servname))
 print(boolserv)
 print(boolcanal)

@bot.tree.command(name= "hey",description="reponse au hey", guild=discord.Object(id=os.environ['id']))
async def hey_slash(interaction : discord.Interaction):
 await interaction.response.send_message("Hey <3")
 
@bot.tree.command(name="showmessage",description="montre les dernier message user",guild=discord.Object(id=os.environ['id']))
async def hey_showmessage(interaction : discord.Interaction,user_name: discord.Member,number_of_message :int ):

    con.commit()
   # await interaction.response.send_message("From User :"+ interaction.user.name)

    #recupere les messages
    sql3 = "SELECT corp FROM messages WHERE name = %s ORDER BY id_message DESC "
    sql4 = "SELECT compteur FROM messages WHERE name = %s ORDER BY id_message DESC "
    sql5 = "SELECT heure FROM messages WHERE name = %s ORDER BY id_message DESC "
    sql6 = "SELECT date FROM messages WHERE name = %s ORDER BY id_message DESC "


    cursor2 = con.cursor()

    cursor2.execute(sql3, (str(user_name),))  # Fournir les valeurs des paramètres sous forme de tuple
    show = cursor2.fetchall()
    cursor2.execute(sql4, (str(user_name),))
    show1 =cursor2.fetchall()
    cursor2.execute(sql5, (str(user_name),))
    show2 =cursor2.fetchall()
    cursor2.execute(sql6, (str(user_name),))
    show3 =cursor2.fetchall()


    listmess = []
    listcompteur =[]
    listheure = []
    listdate = []
    x = 0
    max= 0
    if number_of_message > 5:
        await interaction.response.send_message("Désolé, la demande est limitée à 5 messages maximum.")
        max =5
    else :

      while x < min(number_of_message, len(show)):


        listmess.append(show[x][0])
        listcompteur.append(show1[x][0])
        listheure.append(show2[x][0])
        listdate.append(show3[x][0])

        x += 1

    if max != 5 :
     await interaction.response.send_message("From User :" + str(user_name) + "\n".join(
        [f" \n-----------------\n message {count}  {heure}  {date} : {msg} " for count,heure,date ,msg in
         zip(listcompteur,listheure,listdate,listmess)]))

    print(listmess)
    print(listcompteur)
    print(listheure)
    print(listdate)
@bot.tree.command(name="show_message_channel", description="montre les dernier message d'un channel",   guild=discord.Object(id=os.environ['id']))
async def hey_showmessage_channel(interaction: discord.Interaction, id_channel:str, number_of_message:int):

    sql3 = "SELECT corp FROM messages WHERE id_channel = %s AND name != 'Test01'  ORDER BY id_message DESC"
    sql4 = "SELECT name FROM messages WHERE id_channel = %s AND name != 'Test01'  ORDER BY id_message DESC "
    sql5 = "SELECT heure FROM messages WHERE id_channel = %s AND name != 'Test01'  ORDER BY id_message DESC"
    sql6 = "SELECT date FROM messages WHERE id_channel = %s AND name != 'Test01'  ORDER BY id_message DESC "
    cursor2 = con.cursor()

    cursor2.execute(sql3, (int(id_channel),))  # Fournir les valeurs des paramètres sous forme de tuple
    shower = cursor2.fetchall()
    cursor2.execute(sql4, (id_channel,))
    shower1 = cursor2.fetchall()
    cursor2.execute(sql5, (id_channel,))
    shower2 = cursor2.fetchall()
    cursor2.execute(sql6, (id_channel,))
    shower3 = cursor2.fetchall()

    listmess1 = []
    listname1 = []
    listheure1 = []
    listdate1 = []

    x4 = 0
    max2 = 0

    if number_of_message > 5:
        await interaction.response.send_message("Désolé, la demande est limitée à 5 messages maximum.",)

        max2 = 5
    else:

      while x4 < min(number_of_message, len(shower)):
            listmess1.append(shower[x4][0])
            listname1.append(shower1[x4][0])
            listheure1.append(shower2[x4][0])
            listdate1.append(shower3[x4][0])

            x4 += 1

    print(listmess1)
    print(listname1)
    print(listheure1)
    print(listdate1)

    if max2 != 5:
     await interaction.response.send_message( "\n".join(
            [f" -----------------\n  {name}  {heure}  {date} : {msg} " for name, heure, date, msg in
             zip(listname1, listheure1, listdate1, listmess1)]))

@bot.tree.command(name="talk_to_much", description="montre le user qui parle le plus dans le channel",   guild=discord.Object(id=os.environ['id']))
async def hey_showmessage_channel(interaction: discord.Interaction, id_channel:str):

    sql9 = "SELECT name, COUNT (*) FROM messages WHERE id_channel = %s GROUP BY name ;"
    cursor2 = con.cursor()

    cursor2.execute(sql9,(id_channel,))  # Fournir les valeurs des paramètres sous forme de tuple
    showering = cursor2.fetchall()
    print(showering)
    # Liste pour stocker les valeurs uniques
    valeurs_uniques = []
    valeurs_uniques2 = []

    # Parcours des tuples dans le tableau
    for tuple_ in showering:
        # Ajout de la deuxième valeur de chaque tuple à la liste si elle n'est pas déjà présente
        if tuple_[1] not in valeurs_uniques:
            valeurs_uniques.append(tuple_[1])
            valeurs_uniques2.append(tuple_[0])

    indice_max = valeurs_uniques.index(max(valeurs_uniques))

    await interaction.response.send_message(valeurs_uniques2[indice_max] +" with "+str(valeurs_uniques[indice_max])+" Messages")
    print(valeurs_uniques[indice_max])
    print(valeurs_uniques2[indice_max])

    # Affichage des valeurs uniques
    print(valeurs_uniques)
    print(valeurs_uniques2)

@bot.tree.command(name='whoami', description='Tells you your username and ID.',  guild=discord.Object(id=os.environ['id']))
async def slash_command2(interaction : discord.Interaction):

     response = f'Ton username : {interaction.user.name}#{interaction.user.discriminator}\nTon id : {interaction.user.id}\nServeur id : {interaction.guild_id}\nTon avatar id : {interaction.user.avatar}  '
     await interaction.response.send_message(response)



@bot.tree.command(name="compare_messages", description="Compare le nombre de messages envoyés entre deux utilisateurs", guild=discord.Object(id=os.environ['id']))
async def compare_messages(interaction: discord.Interaction, member1: discord.Member, member2: discord.Member):
    con.commit()

    sql_count_messages = "SELECT COUNT(*) FROM messages WHERE name = %s"
    cursor = con.cursor()

    cursor.execute(sql_count_messages, (member1.name,))
    count_member1 = cursor.fetchone()[0]

    cursor.execute(sql_count_messages, (member2.name,))
    count_member2 = cursor.fetchone()[0]

    if count_member1 > count_member2:
        await interaction.response.send_message(f"{member1.display_name} a envoyé plus de messages que {member2.display_name} !")
    elif count_member1 < count_member2:
        await interaction.response.send_message(f"{member2.display_name} a envoyé plus de messages que {member1.display_name} !")
    else:
        await interaction.response.send_message(f"{member1.display_name} et {member2.display_name} ont envoyé le même nombre de messages !")


import datetime

@bot.tree.command(name="messages_between_dates", description="Affiche tous les messages dans un intervalle de dates spécifié", guild=discord.Object(id=os.environ['id']))
async def messages_between_dates(interaction: discord.Interaction, start_date: str, end_date: str):
    con.commit()

    try:
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        await interaction.response.send_message("Format de date incorrect. Utilisez le format YYYY-MM-DD.")
        return

    sql_select_messages = "SELECT name, corp, compteur, heure, date FROM messages WHERE date BETWEEN %s AND %s ORDER BY compteur ASC"
    cursor = con.cursor()

    cursor.execute(sql_select_messages, (start_date, end_date))
    messages = cursor.fetchall()

    if not messages:
        await interaction.response.send_message("Aucun message trouvé dans l'intervalle de dates spécifié.")
        return

    # Création du contenu du fichier texte
    file_content = "\n".join([f"From User: {name}\nMessage {count} - {heure} {date}: {msg}" for name, msg, count, heure, date in messages])

    # Création et envoi du fichier texte
    with open("messages_between_dates.txt", "w", encoding="utf-8") as file:
        file.write(file_content)

    with open("messages_between_dates.txt", "rb") as file:
        await interaction.response.send_message("Voici le fichier texte contenant les messages:", file=discord.File(file, "messages_between_dates.txt"))
@bot.event
async def on_ready():
    print('Ready!')
    await bot.tree.sync()

    try:
        synced = await bot.tree.sync(guild=discord.Object(id=os.environ['id']))
        print(f"Synced {len(synced)} commands")

    except Exception as e:
        print(e)


# Utilisation du token
bot.run(os.environ['key'])










