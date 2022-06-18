from codebase.ui import *
from codebase.gogoplay import *
from codebase.animix import *
from codebase.search import *
import os
from colorama import Fore, Style


#soem global shit
dub_prefix = False
player = "mpv"
lmagenta = lambda a: f"{Fore.LIGHTMAGENTA_EX}{a}{Style.RESET_ALL}"



provider = ask_provider()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')




clear()
query = input(lmagenta("Enter the anime name: "))
animes = search(query)
x = [i.replace("/v1/","") for i in animes]

anime_name = ask_anime_name(x)
anime_to_watch = animes[x.index(anime_name)]
#print(anime_to_watch)

if provider == "gogoplay":
    from_al = False

    data = extract_episode_info(anime_to_watch)
    p = input(lmagenta(f"[*]Enter episode(total {data['eptotal']}): "))
    link = "https:" + data[str(int(p)-1)]
    try:
        qualities , links = extract_final_links(from_al,link)
        clear()

        quality = ask_quality(qualities)
        final_link = links[qualities.index(quality)]
        #print(final_link)
        os.system(f'{player} --referrer="https://goload.pro" {final_link}')
    except:
        print(red("[*]Change provider"))

else:
    data = extract_episode_info(anime_to_watch)
    p = input(lmagenta(f"[*]Enter episode(total {data['eptotal']}): "))
    links = data[str(int(p)-1)]
    #print(links)
    link = generate_link(links)
    
    #referrer,link = al_return_link(x)
    
    #os.system(f'{player} --referrer="{referrer}" "{link}"' if len(referrer)>0 else f'{player} "{link}"')
    os.system(f'{player} "{link}"')