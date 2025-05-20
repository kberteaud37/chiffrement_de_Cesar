import os
# Module pour enlever les caracères spéciaux
from enlever_caracteres import lire_liste_mots, enlever_caracteres_speciaux

def ouverture_fichier(dossier, fichier="message.txt"):
    # teste si le fichier existe
    full_filename = os.path.join(dossier,fichier)
    if not os.path.isfile(full_filename):
        raise RuntimeError(f'Je ne trouve pas le fichier {full_filename} !')

# Ouvrir le fichier en mode lecture
    with open("message.txt", "r", encoding = "utf-8") as fio:
# Lire le contenu du fichier
        contenu = fio.read()
        for lettre_avec_accent in contenu[-6:]:
            lettre_sans_accent = enlever_caracteres_speciaux(lettre_avec_accent)
            print(f'    {lettre_avec_accent} -> {lettre_sans_accent}')

# On crée un fichier txt et on écrit dedans
with open("message_encrypte.txt", "w") as fio:
    contenu=""
    fio.write(contenu)
