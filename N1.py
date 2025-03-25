import webbrowser
import urllib.parse
import requests
from bs4 import BeautifulSoup

def ouvrir_youtube():
    url = "https://www.youtube.com"
    webbrowser.open(url)

def rechercher_video():
    titre = input("Entrez le titre de la vidéo que vous recherchez : ")
    query = urllib.parse.quote(titre)
    url = f"https://www.youtube.com/results?search_query={query}"
    
    # Récupérer la page de résultats
    response = requests.get(url)
    if response.status_code != 200:
        print("Erreur lors de la récupération des résultats de recherche.")
        return
    
    # Analyser la page pour extraire les liens des vidéos
    soup = BeautifulSoup(response.text, 'html.parser')
    videos = soup.find_all('a', href=True)
    video_links = [link['href'] for link in videos if '/watch?v=' in link['href']]
    
    if not video_links:
        print("Aucune vidéo trouvée.")
        return
    
    # Afficher les 5 premiers résultats
    print("Sélectionnez une vidéo :")
    for i, link in enumerate(video_links[:5]):
        print(f"{i + 1}. https://www.youtube.com{link}")
    
    choix = int(input("Entrez le numéro de la vidéo à ouvrir : "))
    if 1 <= choix <= len(video_links[:5]):
        webbrowser.open(f"https://www.youtube.com{video_links[choix - 1]}")
    else:
        print("Choix invalide.")

# Exécuter la fonction
rechercher_video()
