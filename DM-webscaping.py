#DataFrame avec tous les animes du site : titre, duree, premierediff, saisons, genres
#https://www.senscritique.com/liste/liste_complete_anime/478051
import requests
from bs4 import BeautifulSoup
import pandas as pd

def verif(info): #Cette fonction permet de vérifier si le 'find' trouve quelque chose ou non.
    if info:
        return info.text
    else:
        return " X "
url = "https://www.senscritique.com/liste/liste_complete_anime/478051"
proxies = {"http":"10.0.0.1:3128","https":"10.0.0.1:3128"}

#On crée des listes pour catégoriser les informations obtenues.
liste_titre = []
liste_duree = []
liste_release = []
liste_saison = []
liste_genre = []

for i in range(1,9): #Boucle pour toutes les pages du site.
    new_url = url + "?page=" + str(i)
    response = requests.get(new_url)
    soup = BeautifulSoup(response.content,"html.parser")
    mangas = soup.find_all("div",{"class":"ProductListItem__Content-sc-1jkxxpj-5 jnAqkx"})

    for manga in mangas: #Boucle pour toutes les infos des animes d'une page.
        titre = manga.find("a",{"data-testid":"product-title"})
        liste_titre.append(verif(titre))
        duree = manga.find("span",{"data-testid":"duration"})
        liste_duree.append(verif(duree))
        release = manga.find("span",{"data-testid":"date-release"})          
        liste_release.append(verif(release))
        saison = manga.find("span",{"data-testid":"nb_season"})
        liste_saison.append(verif(saison))
        genre = manga.find("span",{"data-testid":"genres"})
        liste_genre.append(verif(genre))

#Création du DataFrame.
info_manga = pd.DataFrame({
    "Titre":liste_titre,
    "Duree":liste_duree,
    "Diffusion":liste_release,
    "Saisons":liste_saison,
    "Genre":liste_genre
})
print(info_manga) #Affichage