from NewMagalu import game_items_list_magalu
from difflib import SequenceMatcher, get_close_matches

games_ps2 = []
games_ps3 = []
games_ps4 = []
games_ps5 = []
games_wii = []
games_wii_u = []
games_switch = []
games_xbox_360 = []
games_xbox_one = []
games_xbox_series_x = []
games_ps4_repetidos = []

for game in game_items_list_magalu:
    game_items_list_magalu[game_items_list_magalu.index(game)]['titulo'] = game['titulo'].lower()

for x in game_items_list_magalu:
    if x['titulo'].find('jogo') == 0:
        game_items_list_magalu[game_items_list_magalu.index(x)]['titulo'] = x['titulo'][5:]

for x in game_items_list_magalu:
    if 'ps2' in x['titulo'] or 'playstation-2' in x['titulo'] or 'playstation 2' in x['titulo']:
        games_ps2.append(x)

for x in game_items_list_magalu:
    if 'ps3' in x['titulo'] or 'playstation-3' in x['titulo'] or 'playstation 3' in x['titulo']:
        games_ps3.append(x)

for x in game_items_list_magalu:
    if 'ps4' in x['titulo'] or 'playstation-4' in x['titulo'] or 'playstation 4' in x['titulo']:
        games_ps4.append(x)

for x in game_items_list_magalu:
    if 'ps5' in x['titulo'] or 'playstation-5' in x['titulo'] or 'playstation 5' in x['titulo']:
        games_ps5.append(x)

for x in game_items_list_magalu:
    if 'wii' in x['titulo']:
        games_wii.append(x)

for x in game_items_list_magalu:
    if 'wii-u' in x['titulo'] or 'wii u' in x['titulo']:
        games_wii_u.append(x)

for x in game_items_list_magalu:
    if 'switch' in x['titulo']:
        games_switch.append(x)

for x in game_items_list_magalu:
    if 'xbox-360' in x['titulo'] or 'xbox 360' in x['titulo']:
        games_xbox_360.append(x)

for x in game_items_list_magalu:
    if 'xbox-one' in x['titulo'] or 'xbox one' in x['titulo']:
        games_xbox_one.append(x)

for x in game_items_list_magalu:
    if 'xbox-series-x' in x['titulo'] or 'xbox series x' in x['titulo'] or 'xbsx' in x['titulo']:
        games_xbox_series_x.append(x)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

for x in games_ps2:
    if ' para ps2' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' para ps2')]
    if ' para playstation 2' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' para playstation 2')]
    if ' para playstation-2' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' para playstation-2')]

    if ' - ps2' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - ps2')]
    if ' - playstation 2' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - playstation 2')]
    if ' - playstation-2' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - playstation-2')]

    if ' ps2' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' ps2')]
    if ' playstation 2' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' playstation 2')]
    if ' playstation-2' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' playstation-2')]

    if x['titulo'].find('ps2') == 0:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][4:]
    if x['titulo'].find('playstation 2') == 0:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][14:]
    if x['titulo'].find('playstation-2') == 0:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][14:]

    if ' compativel' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' compativel')]
    if ' compatível' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' compatível')]
    if ' - compativel' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - compativel')]
    if ' - compatível' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - compatível')]

    if ' jogo' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' jogo')]
    if ' - jogo' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - jogo')]

    if ' midia' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' midia')]
    if ' mídia' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' mídia')]
    if ' - midia' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - midia')]
    if ' - mídia' in x['titulo']:
        games_ps2[games_ps2.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - mídia')]

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

for x in games_ps3:
    if ' para ps3' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' para ps3')]
    if ' para playstation 3' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' para playstation 3')]
    if ' para playstation-3' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' para playstation-3')]

    if ' - ps3' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - ps3')]
    if ' - playstation 3' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - playstation 3')]
    if ' - playstation-3' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - playstation-3')]

    if ' ps3' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' ps3')]
    if ' playstation 3' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' playstation 3')]
    if ' playstation-3' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' playstation-3')]

    if x['titulo'].find('ps3') == 0:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][4:]
    if x['titulo'].find('playstation 3') == 0:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][14:]
    if x['titulo'].find('playstation-3') == 0:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][14:]

    if ' compativel' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' compativel')]
    if ' compatível' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' compatível')]
    if ' - compativel' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - compativel')]
    if ' - compatível' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - compatível')]

    if ' jogo' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' jogo')]
    if ' - jogo' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - jogo')]

    if ' midia' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' midia')]
    if ' mídia' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' mídia')]
    if ' - midia' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - midia')]
    if ' - mídia' in x['titulo']:
        games_ps3[games_ps3.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - mídia')]

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

for x in games_ps4:
    if ' para ps4' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' para ps4')]
    if ' para playstation 4' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' para playstation 4')]
    if ' para playstation-4' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' para playstation-4')]

    if ' - ps4' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - ps4')]
    if ' - playstation 4' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - playstation 4')]
    if ' - playstation-4' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - playstation-4')]

    if ' ps4' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' ps4')]
    if ' playstation 4' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' playstation 4')]
    if ' playstation-4' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' playstation-4')]

    if x['titulo'].find('ps4') == 0:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][4:]
    if x['titulo'].find('playstation 4') == 0:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][14:]
    if x['titulo'].find('playstation-4') == 0:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][14:]

    if ' compativel' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' compativel')]
    if ' compatível' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' compatível')]
    if ' - compativel' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - compativel')]
    if ' - compatível' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - compatível')]

    if ' jogo' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' jogo')]
    if ' - jogo' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - jogo')]

    if ' midia' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' midia')]
    if ' mídia' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' mídia')]
    if ' - midia' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - midia')]
    if ' - mídia' in x['titulo']:
        games_ps4[games_ps4.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - mídia')]

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

for x in games_ps5:
    if ' para ps5' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' para ps5')]
    if ' para playstation 5' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' para playstation 5')]
    if ' para playstation-5' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' para playstation-5')]

    if ' - ps5' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - ps5')]
    if ' - playstation 5' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - playstation 5')]
    if ' - playstation-5' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - playstation-5')]

    if ' ps5' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' ps5')]
    if ' playstation 5' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' playstation 5')]
    if ' playstation-5' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' playstation-5')]

    if x['titulo'].find('ps5') == 0:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][4:]
    if x['titulo'].find('playstation 5') == 0:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][14:]
    if x['titulo'].find('playstation-5') == 0:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][14:]

    if ' compativel' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' compativel')]
    if ' compatível' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' compatível')]
    if ' - compativel' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - compativel')]
    if ' - compatível' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - compatível')]

    if ' jogo' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' jogo')]
    if ' - jogo' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - jogo')]

    if ' midia' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' midia')]
    if ' mídia' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' mídia')]
    if ' - midia' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - midia')]
    if ' - mídia' in x['titulo']:
        games_ps5[games_ps5.index(x)]['titulo'] = x['titulo'][:x['titulo'].find(' - mídia')]

print(len(game_items_list_magalu))
print(len(games_ps2))
print(len(games_ps3))
print(len(games_ps4))
print(len(games_ps5))
print(len(games_wii))
print(len(games_wii_u))
print(len(games_switch))
print(len(games_xbox_360))
print(len(games_xbox_one))
print(len(games_xbox_series_x))

for x in games_ps2:
    print(x)
print()

for x in games_ps3:
    print(x)
print()

for x in games_ps4:
    print(x)
print()

for x in games_ps5:
    print(x)
print()
