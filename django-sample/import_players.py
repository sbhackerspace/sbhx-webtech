#!/usr/bin/env python
import os, sys
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "allstars.settings")

from players.models import Player, AllStarTeamMember

if __name__ == "__main__":
    player_data = csv.DictReader(open('lahman58-csv/Master.csv', 'r'))
    for player in player_data:
        
        p = Player()
        p.name = "{0} {1}".format(player['nameFirst'], player['nameLast'])
        p.player_id = player['playerID']
        if player['weight']:
            p.weight = int(player['weight'])
        if player['birthYear']:
            p.birth_year = int(player['birthYear'])
        p.save()

    team_data = csv.DictReader(open('lahman58-csv/Allstar.csv', 'r'))
    for team_player in team_data:
        player = Player.objects.get(player_id=team_player['playerID'])
        AllStarTeamMember.objects.create(
                player = player,
                year = int(team_player['yearID']),
                league = team_player['lgID'],
                )
