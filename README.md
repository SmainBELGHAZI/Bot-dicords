# Hi Every One  👋
# <p align="center">Projet Bot discord 🤖 </p>
  
Le but du projet consiste à créer un bot discord qui aura pour objectif de traquer les messages envoyés sur le serveur discord afin de les stocker dans une base de données et de les rediffuser grâce à des commandes.
Le bot devra enregistrer dans la base de données les messages qui auront été envoyés lorsqu'il était connecté.
Ce projet est solo.
Ce projet comporte 5 commandes obligatoires.
3 de ces commandes manipulent une base de données tandis que les 2 autres sont des commandes simples.
Le projet a été réalisé en python 🐍



# <p align="center">Prerequis⚠</p>
  
- Pycharm ;
- API discord ;
- Basse de données.    
    


## 🧐 Features    
- Enregistrer chaque message envoyé ; 
- Proposer plusieurs commandes ;
- Communiquer avec la base de données.

# <p align="center">Utilisation 🕹</p>
Comme dit précédemment le bot sera équipé de 7 commandes principales qui sont :



- /hey : utiliser cette commande pour que le bot vous réponde hey ❤ en retour



- /whoami : utiliser cette commande pour que le bot vous indique votre pseudo, votre ID, votre avatar et le serveur ID. 



- /showmessage : utiliser cette commande en précisant au bot le nom d'un user et le nombre de message à afficher (5 au maximum), le bot vous enverra les derniers messages de l'user



- /show_message_channel : utiliser cette commande en précisant l'ID du channnel ainsi qu'un nombre (5 au maximum), le bot vous enverra les derniers messages du channel



- /talk_to_much : utiliser cette commande en précisant l'ID du channel, le bot vous précisera l'user qui a envoyé le plus de message ainsi que le nombre de messages qu'il a envoyé



- /compare_messages : utiliser cette commande en indiquant deux users du serveur pour afficher celui qui aura envoyé le plus de messages



- /messages_between_date : utiliser cette commande en précisant deux dates, le bot vous enverra un fichier texte avec tous les messages qui auront été envoyés entre ces deux dates

  

# <p align="center">Construit avec 👷 </p>
  
- Langages : Python

- Outils : Pycharm, Postgres, Discord



# <p align="center">Documentation 💼 </p>
  
- Discord.py : https://discordpy.readthedocs.io/en/stable/

- Github : https://github.com/



# <p align="center">Base de données 💾 </p>
  
Pour créer la base de données nécessaire à la réalisation du projet, j'ai décidé de me tourner vers postgres. 

Vous trouverez, ci-après, les différents schémas de la base :

- MCD

![alt text](https://imagizer.imageshack.com/v2/576x325q70/r/923/ZuQ1yC.png)

- MLD

![alt text](https://imagizer.imageshack.com/v2/576x325q70/r/922/J3y8mV.png)

- MPD

![alt text](https://imagizer.imageshack.com/v2/576x325q70/r/922/46ZiI3.png)

- Diagramme de sequence 

![alt text](https://imagizer.imageshack.com/v2/308x325q70/r/922/xY0mG7.jpg)
                
        

## 🛠️ Install Dependencies    
```bash
import discord
import psycopg2
```






## 🙇 Author
#### Smain Belghazi
- Github: [https://github.com/SmainBELGHAZI)
