# Ouvrir le fichier en mode lecture
with open("message.txt", "r", encoding = "utf-8") as fio:
# Lire le contenu du fichier
    contenu = fio.read()

# On crée un fichier txt et on écrit dedans
with open("message_encrypte.txt", "w") as fio:
    fio.write(contenu)
