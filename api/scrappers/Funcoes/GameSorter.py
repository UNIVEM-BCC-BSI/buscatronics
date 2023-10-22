from difflib import SequenceMatcher
from NewMagalu import game_items_list_magalu

user_game_list = []

def titulo_minusculo(json):
    for game in json:
        json[json.index(game)]['titulo'] = game['titulo'].lower()
    return(json)

def game_finder(json):
    for game in json:
        if SequenceMatcher(None, game_usuário, game['titulo']).ratio() > 0.75 and game not in user_game_list:
            user_game_list.append(game)
        elif game_usuário in game['titulo']:
            user_game_list.append(game)

def game_price_organizer():
    return sorted(user_game_list, key=lambda k: k['preco_desconto'])

game_usuário = input('Digite o nome do jogo: ')

titulo_minusculo(game_items_list_magalu)
game_finder(game_items_list_magalu)
user_game_list = game_price_organizer()

print()
for x in user_game_list:
    print(f"{x['titulo']:<100} {x['preco_desconto']:>10.2f}")
