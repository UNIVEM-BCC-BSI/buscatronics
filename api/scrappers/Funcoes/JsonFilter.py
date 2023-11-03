import json
from website.models import *
from website.serializers import *

class JsonFilter():
    def __init__(self, jsonRequest):
        self.games_ps2 = []
        self.games_ps3 = []
        self.games_ps4 = []
        self.games_ps5 = []
        self.games_wii = []
        self.games_wii_u = []
        self.games_switch = []
        self.games_xbox_360 = []
        self.games_xbox_one = []
        self.games_xbox_series_x = []
        self.new_game_items_list_teste = []
        self.game_items_list_magalu = jsonRequest
        self.plataforma = json.loads(json.dumps(PlataformaSerializer(Plataforma.objects.all(), many=True).data))

    def sorter(self):
        try:
            for game in self.game_items_list_magalu:
                self.game_items_list_magalu[self.game_items_list_magalu.index(game)]['nome'] = game['nome'].lower()

            for x in self.game_items_list_magalu:
                if x['nome'].find('jogo') == 0:
                    self.game_items_list_magalu[self.game_items_list_magalu.index(x)]['nome'] = x['nome'][5:]

            for x in self.game_items_list_magalu:
                if 'ps2' in x['nome'] or 'playstation-2' in x['nome'] or 'playstation 2' in x['nome']:
                    self.games_ps2.append(x)

            for x in self.game_items_list_magalu:
                if 'ps3' in x['nome'] or 'playstation-3' in x['nome'] or 'playstation 3' in x['nome']:
                    self.games_ps3.append(x)

            for x in self.game_items_list_magalu:
                if 'ps4' in x['nome'] or 'playstation-4' in x['nome'] or 'playstation 4' in x['nome']:
                    self.games_ps4.append(x)

            for x in self.game_items_list_magalu:
                if 'ps5' in x['nome'] or 'playstation-5' in x['nome'] or 'playstation 5' in x['nome']:
                    self.games_ps5.append(x)

            for x in self.game_items_list_magalu:
                if 'wii' in x['nome']:
                    self.games_wii.append(x)

            for x in self.game_items_list_magalu:
                if 'wii-u' in x['nome'] or 'wii u' in x['nome']:
                    self.games_wii_u.append(x)

            for x in self.game_items_list_magalu:
                if 'switch' in x['nome']:
                    self.games_switch.append(x)

            for x in self.game_items_list_magalu:
                if 'xbox-360' in x['nome'] or 'xbox 360' in x['nome']:
                    self.games_xbox_360.append(x)

            for x in self.game_items_list_magalu:
                if 'xbox-one' in x['nome'] or 'xbox one' in x['nome']:
                    self.games_xbox_one.append(x)

            for x in self.game_items_list_magalu:
                if 'xbox-series-x' in x['nome'] or 'xbox series x' in x['nome'] or 'xbsx' in x['nome']:
                    self.games_xbox_series_x.append(x)

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

            for x in self.games_ps2:
                if ' para ps2' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' para ps2')]
                if ' para playstation 2' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' para playstation 2')]
                if ' para playstation-2' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' para playstation-2')]

                if ' - ps2' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' - ps2')]
                if ' - playstation 2' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' - playstation 2')]
                if ' - playstation-2' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' - playstation-2')]

                if ' ps2' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' ps2')]
                if ' playstation 2' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' playstation 2')]
                if ' playstation-2' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' playstation-2')]

                if x['nome'].find('ps2') == 0:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][4:]
                if x['nome'].find('playstation 2') == 0:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][14:]
                if x['nome'].find('playstation-2') == 0:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][14:]

                if ' - compativel' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compativel')]
                if ' - compatível' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compatível')]
                if ' compativel' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' compativel')]
                if ' compatível' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' compatível')]

                if ' - jogo' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' - jogo')]
                if ' jogo' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' jogo')]

                if ' - midia' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' - midia')]
                if ' - mídia' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' - mídia')]
                if ' midia' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' midia')]
                if ' mídia' in x['nome']:
                    self.games_ps2[self.games_ps2.index(x)]['nome'] = x['nome'][:x['nome'].find(' mídia')]

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

            for x in self.games_ps3:
                if ' para ps3' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' para ps3')]
                if ' para playstation 3' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' para playstation 3')]
                if ' para playstation-3' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' para playstation-3')]

                if ' - ps3' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' - ps3')]
                if ' - playstation 3' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' - playstation 3')]
                if ' - playstation-3' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' - playstation-3')]

                if ' ps3' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' ps3')]
                if ' playstation 3' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' playstation 3')]
                if ' playstation-3' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' playstation-3')]

                if x['nome'].find('ps3') == 0:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][4:]
                if x['nome'].find('playstation 3') == 0:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][14:]
                if x['nome'].find('playstation-3') == 0:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][14:]

                if ' - compativel' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compativel')]
                if ' - compatível' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compatível')]
                if ' compativel' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' compativel')]
                if ' compatível' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' compatível')]

                if ' - jogo' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' - jogo')]
                if ' jogo' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' jogo')]

                if ' - midia' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' - midia')]
                if ' - mídia' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' - mídia')]
                if ' midia' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' midia')]
                if ' mídia' in x['nome']:
                    self.games_ps3[self.games_ps3.index(x)]['nome'] = x['nome'][:x['nome'].find(' mídia')]

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

            for x in self.games_ps4:
                if ' para ps4' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' para ps4')]
                if ' para playstation 4' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' para playstation 4')]
                if ' para playstation-4' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' para playstation-4')]

                if ' - ps4' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' - ps4')]
                if ' - playstation 4' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' - playstation 4')]
                if ' - playstation-4' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' - playstation-4')]

                if ' ps4' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' ps4')]
                if ' playstation 4' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' playstation 4')]
                if ' playstation-4' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' playstation-4')]

                if x['nome'].find('ps4') == 0:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][4:]
                if x['nome'].find('playstation 4') == 0:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][14:]
                if x['nome'].find('playstation-4') == 0:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][14:]

                if ' - compativel' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compativel')]
                if ' - compatível' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compatível')]
                if ' compativel' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' compativel')]
                if ' compatível' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' compatível')]

                if ' - jogo' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' - jogo')]
                if ' jogo' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' jogo')]

                if ' - midia' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' - midia')]
                if ' - mídia' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' - mídia')]
                if ' midia' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' midia')]
                if ' mídia' in x['nome']:
                    self.games_ps4[self.games_ps4.index(x)]['nome'] = x['nome'][:x['nome'].find(' mídia')]

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

            for x in self.games_ps5:
                if ' para ps5' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' para ps5')]
                if ' para playstation 5' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' para playstation 5')]
                if ' para playstation-5' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' para playstation-5')]

                if ' - ps5' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' - ps5')]
                if ' - playstation 5' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' - playstation 5')]
                if ' - playstation-5' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' - playstation-5')]

                if ' ps5' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' ps5')]
                if ' playstation 5' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' playstation 5')]
                if ' playstation-5' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' playstation-5')]

                if x['nome'].find('ps5') == 0:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][4:]
                if x['nome'].find('playstation 5') == 0:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][14:]
                if x['nome'].find('playstation-5') == 0:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][14:]

                if ' - compativel' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compativel')]
                if ' - compatível' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compatível')]
                if ' compativel' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' compativel')]
                if ' compatível' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' compatível')]

                if ' - jogo' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' - jogo')]
                if ' jogo' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' jogo')]

                if ' - midia' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' - midia')]
                if ' - mídia' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' - mídia')]
                if ' midia' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' midia')]
                if ' mídia' in x['nome']:
                    self.games_ps5[self.games_ps5.index(x)]['nome'] = x['nome'][:x['nome'].find(' mídia')]

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

            for x in self.games_wii:
                if ' para wii' in x['nome']:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][:x['nome'].find(' para wii')]

                if ' - wii' in x['nome']:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][:x['nome'].find(' - wii')]

                if ' wii' in x['nome']:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][:x['nome'].find(' wii')]

                if x['nome'].find('wii') == 0:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][4:]

                if ' - compativel' in x['nome']:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compativel')]
                if ' - compatível' in x['nome']:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compatível')]
                if ' compativel' in x['nome']:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][:x['nome'].find(' compativel')]
                if ' compatível' in x['nome']:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][:x['nome'].find(' compatível')]

                if ' - jogo' in x['nome']:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][:x['nome'].find(' - jogo')]
                if ' jogo' in x['nome']:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][:x['nome'].find(' jogo')]

                if ' - midia' in x['nome']:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][:x['nome'].find(' - midia')]
                if ' - mídia' in x['nome']:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][:x['nome'].find(' - mídia')]
                if ' midia' in x['nome']:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][:x['nome'].find(' midia')]
                if ' mídia' in x['nome']:
                    self.games_wii[self.games_wii.index(x)]['nome'] = x['nome'][:x['nome'].find(' mídia')]

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

            for x in self.games_wii_u:
                if ' para wii u' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' para wii u')]
                if ' para wii-u' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' para wii-u')]

                if ' - wii u' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' - wii u')]
                if ' - wii-u' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' - wii-u')]

                if ' wii u' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' wii u')]
                if ' wii-u' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' wii-u')]

                if x['nome'].find('wii u') == 0:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][6:]
                if x['nome'].find('wii-u') == 0:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][6:]

                if ' - compativel' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compativel')]
                if ' - compatível' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compatível')]
                if ' compativel' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' compativel')]
                if ' compatível' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' compatível')]

                if ' - jogo' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' - jogo')]
                if ' jogo' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' jogo')]

                if ' - midia' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' - midia')]
                if ' - mídia' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' - mídia')]
                if ' midia' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' midia')]
                if ' mídia' in x['nome']:
                    self.games_wii_u[self.games_wii_u.index(x)]['nome'] = x['nome'][:x['nome'].find(' mídia')]

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

            for x in self.games_switch:
                if ' para switch' in x['nome']:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][:x['nome'].find(' para switch')]

                if ' - switch' in x['nome']:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][:x['nome'].find(' - switch')]

                if ' switch' in x['nome']:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][:x['nome'].find(' switch')]

                if x['nome'].find('switch') == 0:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][7:]

                if ' - compativel' in x['nome']:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compativel')]
                if ' - compatível' in x['nome']:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compatível')]
                if ' compativel' in x['nome']:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][:x['nome'].find(' compativel')]
                if ' compatível' in x['nome']:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][:x['nome'].find(' compatível')]

                if ' - jogo' in x['nome']:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][:x['nome'].find(' - jogo')]
                if ' jogo' in x['nome']:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][:x['nome'].find(' jogo')]

                if ' - midia' in x['nome']:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][:x['nome'].find(' - midia')]
                if ' - mídia' in x['nome']:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][:x['nome'].find(' - mídia')]
                if ' midia' in x['nome']:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][:x['nome'].find(' midia')]
                if ' mídia' in x['nome']:
                    self.games_switch[self.games_switch.index(x)]['nome'] = x['nome'][:x['nome'].find(' mídia')]

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

            for x in self.games_xbox_360:
                if ' para xbox 360' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' para xbox 360')]
                if ' para xbox-360' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' para xbox-360')]

                if ' - xbox 360' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' - xbox 360')]
                if ' - xbox-360' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' - xbox-360')]

                if ' xbox 360' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' xbox 360')]
                if ' xbox-360' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' xbox-360')]

                if x['nome'].find('xbox 360') == 0:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][9:]
                if x['nome'].find('xbox-360') == 0:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][9:]

                if ' - compativel' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compativel')]
                if ' - compatível' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compatível')]
                if ' compativel' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' compativel')]
                if ' compatível' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' compatível')]

                if ' - jogo' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' - jogo')]
                if ' jogo' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' jogo')]

                if ' - midia' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' - midia')]
                if ' - mídia' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' - mídia')]
                if ' midia' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' midia')]
                if ' mídia' in x['nome']:
                    self.games_xbox_360[self.games_xbox_360.index(x)]['nome'] = x['nome'][:x['nome'].find(' mídia')]

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

            for x in self.games_xbox_one:
                if ' para xbox one' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' para xbox one')]
                if ' para xbox-one' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' para xbox-one')]

                if ' - xbox one' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' - xbox one')]
                if ' - xbox-one' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' - xbox-one')]

                if ' xbox one' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' xbox one')]
                if ' xbox-one' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' xbox-one')]

                if x['nome'].find('xbox one') == 0:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][9:]
                if x['nome'].find('xbox-one') == 0:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][9:]

                if ' - compativel' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compativel')]
                if ' - compatível' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compatível')]
                if ' compativel' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' compativel')]
                if ' compatível' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' compatível')]

                if ' - jogo' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' - jogo')]
                if ' jogo' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' jogo')]

                if ' - midia' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' - midia')]
                if ' - mídia' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' - mídia')]
                if ' midia' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' midia')]
                if ' mídia' in x['nome']:
                    self.games_xbox_one[self.games_xbox_one.index(x)]['nome'] = x['nome'][:x['nome'].find(' mídia')]

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

            for x in self.games_xbox_series_x:
                if ' para xbsx' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' para xbsx')]
                if ' para xbox series x' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' para xbox series x')]
                if ' para xbox-series-x' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' para xbox-series-x')]

                if ' - xbsx' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' - xbsx')]
                if ' - xbox series x' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' - xbox series x')]
                if ' - xbox-series-x' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' - xbox-series-x')]

                if ' xbsx' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' xbsx')]
                if ' xbox series x' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' xbox series x')]
                if ' xbox-series-x' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' xbox-series-x')]

                if x['nome'].find('xbsx') == 0:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][5:]
                if x['nome'].find('xbox series x') == 0:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][14:]
                if x['nome'].find('xbox-series-x') == 0:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][14:]

                if ' - compativel' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compativel')]
                if ' - compatível' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' - compatível')]
                if ' compativel' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' compativel')]
                if ' compatível' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' compatível')]

                if ' - jogo' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' - jogo')]
                if ' jogo' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' jogo')]

                if ' - midia' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' - midia')]
                if ' - mídia' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' - mídia')]
                if ' midia' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' midia')]
                if ' mídia' in x['nome']:
                    self.games_xbox_series_x[self.games_xbox_series_x.index(x)]['nome'] = x['nome'][:x['nome'].find(' mídia')]

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

            # print()
            # print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            # print()

            # print(len(self.game_items_list_magalu))
            # print(len(self.games_ps2))
            # print(len(self.games_ps3))
            # print(len(self.games_ps4))
            # print(len(self.games_ps5))
            # print(len(self.games_wii))
            # print(len(self.games_wii_u))
            # print(len(self.games_switch))
            # print(len(self.games_xbox_360))
            # print(len(self.games_xbox_one))
            # print(len(self.games_xbox_series_x))

            # print()
            # print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            # print()

            for x in self.games_ps2:
                self.new_game_items_list_teste.append(x.copy())
                self.new_game_items_list_teste[self.new_game_items_list_teste.index(x)].update({'plataforma': next(p["id"] for p in self.plataforma if p["nome"] == "PlayStation")})

            for x in self.games_ps3:
                self.new_game_items_list_teste.append(x.copy())
                self.new_game_items_list_teste[self.new_game_items_list_teste.index(x)].update({'plataforma': next(p["id"] for p in self.plataforma if p["nome"] == "PlayStation")})

            for x in self.games_ps4:
                self.new_game_items_list_teste.append(x.copy())
                self.new_game_items_list_teste[self.new_game_items_list_teste.index(x)].update({'plataforma': next(p["id"] for p in self.plataforma if p["nome"] == "PlayStation")})

            for x in self.games_ps5:
                self.new_game_items_list_teste.append(x.copy())
                self.new_game_items_list_teste[self.new_game_items_list_teste.index(x)].update({'plataforma': next(p["id"] for p in self.plataforma if p["nome"] == "PlayStation")})

            for x in self.games_wii:
                self.new_game_items_list_teste.append(x.copy())
                self.new_game_items_list_teste[self.new_game_items_list_teste.index(x)].update({'plataforma': next(p["id"] for p in self.plataforma if p["nome"] == "Nintendo")})

            for x in self.games_wii_u:
                self.new_game_items_list_teste.append(x.copy())
                self.new_game_items_list_teste[self.new_game_items_list_teste.index(x)].update({'plataforma': next(p["id"] for p in self.plataforma if p["nome"] == "Nintendo")})

            for x in self.games_switch:
                self.new_game_items_list_teste.append(x.copy())
                self.new_game_items_list_teste[self.new_game_items_list_teste.index(x)].update({'plataforma': next(p["id"] for p in self.plataforma if p["nome"] == "Nintendo")})

            for x in self.games_xbox_360:
                self.new_game_items_list_teste.append(x.copy())
                self.new_game_items_list_teste[self.new_game_items_list_teste.index(x)].update({'plataforma': next(p["id"] for p in self.plataforma if p["nome"] == "Xbox")})

            for x in self.games_xbox_one:
                self.new_game_items_list_teste.append(x.copy())
                self.new_game_items_list_teste[self.new_game_items_list_teste.index(x)].update({'plataforma': next(p["id"] for p in self.plataforma if p["nome"] == "Xbox")})

            for x in self.games_xbox_series_x:
                self.new_game_items_list_teste.append(x.copy())
                self.new_game_items_list_teste[self.new_game_items_list_teste.index(x)].update({'plataforma': next(p["id"] for p in self.plataforma if p["nome"] == "Xbox")})

            for x in self.new_game_items_list_teste:
                self.new_game_items_list_teste[self.new_game_items_list_teste.index(x)]['nome'] = x['nome'].title()
        except Exception as e:
            pass
        finally:
            return self.new_game_items_list_teste
        
