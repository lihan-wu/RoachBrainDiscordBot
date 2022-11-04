import discord
import requests
import json
import datetime
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

hero_data_link = 'https://api.opendota.com/api/heroStats'
hero_data_r = requests.get(hero_data_link)
hero_data = json.loads(hero_data_r.text)

def fix_hero_data_function():
    hero_data.insert(0, "buffer")
    hero_data.insert(24, "buffer")
    hero_data.insert(115, "buffer")
    hero_data.insert(116, "buffer")
    hero_data.insert(117, "buffer")
    hero_data.insert(118, "buffer")
    hero_data.insert(122, "buffer")
    hero_data.insert(124, "buffer")
    hero_data.insert(125, "buffer")
    hero_data.insert(127, "buffer")
    hero_data.insert(130, "buffer")
    hero_data.insert(131, "buffer")
    hero_data.insert(132, "buffer")
    hero_data.insert(133, "buffer")
    hero_data.insert(134, "buffer")

fix_hero_data_function()

game_mode_list = [
	"Unknown",
	"All Pick",
	"Captains Mode",
	"Random Draft",
	"Single Draft",
	"All Random",
	"Intro",
	"Diretide",
	"Reverse Captains Mode",
	"The Greeviling",
	 "Tutorial",
	 "Mid Only",
	 "Least Played",
	 "Limited Heroes",
	 "Compendium",
	 "Custom",
	 "Captains Draft",
	 "Balanced Draft",
	 "Ability Draft",
	 "Diretide",
	 "All Random Deathmatch",
	 "1v1 Solo Mid",
	 "All Draft",
	 "Turbo",
	 "Mutation"
]

lobby_type_list = [
	 "Normal",
	 "Practice",
	 "Tournament",
	 "Tutorial",
	 "Co-Op Bots",
	 "Ranked Team MM (Legacy)",
	 "Ranked Solo MM (Legacy)",
	 "Ranked",
	 "1v1 Mid",
	 "Battle Cup",
     "?",
     "?",
     "Event"
]

rank_list = {
	'11': "Herald 1",
	'12': "Herald 2",
	'13': "Herald 3",
	'14': "Herald 4",
	'15': "Herald 5",
	'21': "Guardian 1",
	'22': "Guardian 2",
	'23': "Guardian 3",
	'24': "Guardian 4",
	'25': "Guardian 5",
	'31': "Crusader 1",
	'32': "Crusader 2",
	'33': "Crusader 3",
	'34': "Crusader 4",
	'35': "Crusader 5",
	'41': "Archon 1",
	'42': "Archon 2",
	'43': "Archon 3",
	'44': "Archon 4",
	'45': "Archon 5",
	'51': "Legend 1",
	'52': "Legend 2",
	'53': "Legend 3",
	'54': "Legend 4",
	'55': "Legend 5",
	'61': "Ancient 1",
	'62': "Ancient 2",
	'63': "Ancient 3",
	'64': "Ancient 4",
	'65': "Ancient 5",
	'71': "Divine 1",
	'72': "Divine 2",
	'73': "Divine 3",
	'74': "Divine 4",
	'75': "Divine 5",
	'81': "Immortal 1",
	'82': "Immortal 2",
	'83': "Immortal 3",
	'84': "Immortal 4",
	'85': "Immortal 5" 
}


def roach_recent_function():
    link = 'https://api.opendota.com/api/players/311160163/recentMatches?api_key="3a71b2fc-46ee-4333-98f6-e5536c8b4cb5"'
    r = requests.get(link)
    data = json.loads(r.text)


    win_loss_result = []

    for d in data:
        if (d["player_slot"] <= 5) and (d["radiant_win"] == True):
            win = 1
            win_loss_result.append(win)
        elif (d["player_slot"] >= 6) and (d["radiant_win"] == False):
            win = 1
            win_loss_result.append(win)
        else:
            loss = 0
            win_loss_result.append(loss)

    def winrate_function():
        
        recent_wins = 0

        for w in win_loss_result:
            if w == 1:
                recent_wins = recent_wins + 5
        
        global current_winrate
        
        current_winrate = recent_wins

    def if_lose_streak():

        global current_streak

        if win_loss_result[0] == 0 and win_loss_result[1] == 1:
            current_streak = 1
        elif win_loss_result[1] == 0 and win_loss_result[2] == 1:
            current_streak = 2
        elif win_loss_result[2] == 0 and win_loss_result[3] == 1:
            current_streak = 3
        elif win_loss_result[3] == 0 and win_loss_result[4] == 1:
            current_streak = 4
        elif win_loss_result[4] == 0 and win_loss_result[5] == 1:
            current_streak = 5
        elif win_loss_result[5] == 0 and win_loss_result[6] == 1:
            current_streak = 6
        elif win_loss_result[6] == 0 and win_loss_result[7] == 1:
            current_streak = 7
        elif win_loss_result[7] == 0 and win_loss_result[8] == 1:
            current_streak = 8
        elif win_loss_result[8] == 0 and win_loss_result[9] == 1:
            current_streak = 9        
        elif win_loss_result[9] == 0 and win_loss_result[10] == 1:
            current_streak = 10
        elif win_loss_result[10] == 0 and win_loss_result[11] == 1:
            current_streak = 11
        elif win_loss_result[11] == 0 and win_loss_result[12] == 1:
            current_streak = 12
        elif win_loss_result[12] == 0 and win_loss_result[13] == 1:
            current_streak = 13
        elif win_loss_result[13] == 0 and win_loss_result[14] == 1:
            current_streak = 14
        elif win_loss_result[14] == 0 and win_loss_result[15] == 1:
            current_streak = 15
        elif win_loss_result[15] == 0 and win_loss_result[16] == 1:
            current_streak = 16
        elif win_loss_result[16] == 0 and win_loss_result[17] == 1:
            current_streak = 17 
        elif win_loss_result[17] == 0 and win_loss_result[18] == 1:
            current_streak = 18
        elif win_loss_result[18] == 0 and win_loss_result[19] == 1:
            current_streak = 19
        elif win_loss_result[19] == 0:
            current_streak = 20  

    # calculates streak if the player is on a win streak
    def if_win_streak():

        global current_streak

        if win_loss_result[0] == 1 and win_loss_result[1] == 0:
            current_streak = 1
        elif win_loss_result[1] == 1 and win_loss_result[2] == 0:
            current_streak = 2
        elif win_loss_result[2] == 1 and win_loss_result[3] == 0:
            current_streak = 3
        elif win_loss_result[3] == 1 and win_loss_result[4] == 0:
            current_streak = 4
        elif win_loss_result[4] == 1 and win_loss_result[5] == 0:
            current_streak = 5
        elif win_loss_result[5] == 1 and win_loss_result[6] == 0:
            current_streak = 6
        elif win_loss_result[6] == 1 and win_loss_result[7] == 0:
            current_streak = 7
        elif win_loss_result[7] == 1 and win_loss_result[8] == 0:
            current_streak = 8
        elif win_loss_result[8] == 1 and win_loss_result[9] == 0:
            current_streak = 9        
        elif win_loss_result[9] == 1 and win_loss_result[10] == 0:
            current_streak = 10
        elif win_loss_result[10] == 1 and win_loss_result[11] == 0:
            current_streak = 11
        elif win_loss_result[11] == 1 and win_loss_result[12] == 0:
            current_streak = 12
        elif win_loss_result[12] == 1 and win_loss_result[13] == 0:
            current_streak = 13
        elif win_loss_result[13] == 1 and win_loss_result[14] == 0:
            current_streak = 14
        elif win_loss_result[14] == 1 and win_loss_result[15] == 0:
            current_streak = 15
        elif win_loss_result[15] == 1 and win_loss_result[16] == 0:
            current_streak = 16
        elif win_loss_result[16] == 1 and win_loss_result[17] == 0:
            current_streak = 17  
        elif win_loss_result[17] == 1 and win_loss_result[18] == 0:
            current_streak = 18
        elif win_loss_result[18] == 1 and win_loss_result[19] == 0:
            current_streak = 19
        elif win_loss_result[19] == 1:
            current_streak = 20

    def determine_streak_function():

        global streak_type
        global last_match_result

        if win_loss_result[0] == 0:
            if_lose_streak()
            streak_type = ("Current lose streak")
            last_match_result = ("Lost Match")
        else:
            if_win_streak()
            streak_type = ("Current Win streak")
            last_match_result = ("Won Match")

    global match_id
    global duration
    global start_time_formatted
    global lobby_type
    global tower_damage
    global hero_id
    global kills
    global deaths
    global assists
    global average_rank
    global gold_per_min
    global last_hits
    global hero_damage
    global hero_healing
    global game_mode
    global last_hero_id
    global last_game_mode
    global last_lobby_type
    global duration_formatted
    global rank_formatted
    global match_link
    global player_title

    for match in data[0:1]:
        match_id = (match['match_id'])
        duration = (match['duration'])
        start_time = (match['start_time'])
        lobby_type = (match['lobby_type'])
        tower_damage = (match['tower_damage'])
        hero_id = (match['hero_id'])
        kills = (match['kills'])
        deaths = (match['deaths'])
        assists = (match['assists'])
        average_rank = (match['average_rank'])
        gold_per_min = (match['gold_per_min'])
        last_hits = (match['last_hits'])
        hero_damage = (match['hero_damage'])
        hero_healing = (match['hero_healing'])
        game_mode = (match['game_mode'])
        

    determine_streak_function()
    winrate_function()

    hd = hero_data[hero_id]['img']
    last_hero_id = 'https://api.opendota.com' + hd

    last_game_mode = game_mode_list[game_mode]
    last_lobby_type = lobby_type_list[lobby_type]

    duration_formatted = str(datetime.timedelta(seconds=(duration)))

    start_time_tz_est = datetime.datetime.fromtimestamp(start_time, datetime.timezone(datetime.timedelta(hours=-4)))
    start_time_formatted = start_time_tz_est.strftime('%B %d, %I:%M %p')

    rank_formatted = rank_list[str(average_rank)]

    match_link = "https://www.dotabuff.com/matches/" + str(match_id)

    player_title = "Roach's most recent match"

def zech_recent_function():
    link = 'https://api.opendota.com/api/players/67380505/recentMatches?api_key="3a71b2fc-46ee-4333-98f6-e5536c8b4cb5"'
    r = requests.get(link)
    data = json.loads(r.text)


    win_loss_result = []

    for d in data:
        if (d["player_slot"] <= 5) and (d["radiant_win"] == True):
            win = 1
            win_loss_result.append(win)
        elif (d["player_slot"] >= 6) and (d["radiant_win"] == False):
            win = 1
            win_loss_result.append(win)
        else:
            loss = 0
            win_loss_result.append(loss)

    def winrate_function():
        
        recent_wins = 0

        for w in win_loss_result:
            if w == 1:
                recent_wins = recent_wins + 5
        
        global current_winrate
        
        current_winrate = recent_wins

    def if_lose_streak():

        global current_streak

        if win_loss_result[0] == 0 and win_loss_result[1] == 1:
            current_streak = 1
        elif win_loss_result[1] == 0 and win_loss_result[2] == 1:
            current_streak = 2
        elif win_loss_result[2] == 0 and win_loss_result[3] == 1:
            current_streak = 3
        elif win_loss_result[3] == 0 and win_loss_result[4] == 1:
            current_streak = 4
        elif win_loss_result[4] == 0 and win_loss_result[5] == 1:
            current_streak = 5
        elif win_loss_result[5] == 0 and win_loss_result[6] == 1:
            current_streak = 6
        elif win_loss_result[6] == 0 and win_loss_result[7] == 1:
            current_streak = 7
        elif win_loss_result[7] == 0 and win_loss_result[8] == 1:
            current_streak = 8
        elif win_loss_result[8] == 0 and win_loss_result[9] == 1:
            current_streak = 9        
        elif win_loss_result[9] == 0 and win_loss_result[10] == 1:
            current_streak = 10
        elif win_loss_result[10] == 0 and win_loss_result[11] == 1:
            current_streak = 11
        elif win_loss_result[11] == 0 and win_loss_result[12] == 1:
            current_streak = 12
        elif win_loss_result[12] == 0 and win_loss_result[13] == 1:
            current_streak = 13
        elif win_loss_result[13] == 0 and win_loss_result[14] == 1:
            current_streak = 14
        elif win_loss_result[14] == 0 and win_loss_result[15] == 1:
            current_streak = 15
        elif win_loss_result[15] == 0 and win_loss_result[16] == 1:
            current_streak = 16
        elif win_loss_result[16] == 0 and win_loss_result[17] == 1:
            current_streak = 17 
        elif win_loss_result[17] == 0 and win_loss_result[18] == 1:
            current_streak = 18
        elif win_loss_result[18] == 0 and win_loss_result[19] == 1:
            current_streak = 19
        elif win_loss_result[19] == 0:
            current_streak = 20  

    # calculates streak if the player is on a win streak
    def if_win_streak():

        global current_streak

        if win_loss_result[0] == 1 and win_loss_result[1] == 0:
            current_streak = 1
        elif win_loss_result[1] == 1 and win_loss_result[2] == 0:
            current_streak = 2
        elif win_loss_result[2] == 1 and win_loss_result[3] == 0:
            current_streak = 3
        elif win_loss_result[3] == 1 and win_loss_result[4] == 0:
            current_streak = 4
        elif win_loss_result[4] == 1 and win_loss_result[5] == 0:
            current_streak = 5
        elif win_loss_result[5] == 1 and win_loss_result[6] == 0:
            current_streak = 6
        elif win_loss_result[6] == 1 and win_loss_result[7] == 0:
            current_streak = 7
        elif win_loss_result[7] == 1 and win_loss_result[8] == 0:
            current_streak = 8
        elif win_loss_result[8] == 1 and win_loss_result[9] == 0:
            current_streak = 9        
        elif win_loss_result[9] == 1 and win_loss_result[10] == 0:
            current_streak = 10
        elif win_loss_result[10] == 1 and win_loss_result[11] == 0:
            current_streak = 11
        elif win_loss_result[11] == 1 and win_loss_result[12] == 0:
            current_streak = 12
        elif win_loss_result[12] == 1 and win_loss_result[13] == 0:
            current_streak = 13
        elif win_loss_result[13] == 1 and win_loss_result[14] == 0:
            current_streak = 14
        elif win_loss_result[14] == 1 and win_loss_result[15] == 0:
            current_streak = 15
        elif win_loss_result[15] == 1 and win_loss_result[16] == 0:
            current_streak = 16
        elif win_loss_result[16] == 1 and win_loss_result[17] == 0:
            current_streak = 17  
        elif win_loss_result[17] == 1 and win_loss_result[18] == 0:
            current_streak = 18
        elif win_loss_result[18] == 1 and win_loss_result[19] == 0:
            current_streak = 19
        elif win_loss_result[19] == 1:
            current_streak = 20

    def determine_streak_function():

        global streak_type
        global last_match_result

        if win_loss_result[0] == 0:
            if_lose_streak()
            streak_type = ("Current lose streak")
            last_match_result = ("Lost Match")
        else:
            if_win_streak()
            streak_type = ("Current Win streak")
            last_match_result = ("Won Match")

    global match_id
    global duration
    global start_time_formatted
    global lobby_type
    global tower_damage
    global hero_id
    global kills
    global deaths
    global assists
    global average_rank
    global gold_per_min
    global last_hits
    global hero_damage
    global hero_healing
    global game_mode
    global last_hero_id
    global last_game_mode
    global last_lobby_type
    global duration_formatted
    global rank_formatted
    global match_link
    global player_title

    for match in data[0:1]:
        match_id = (match['match_id'])
        duration = (match['duration'])
        start_time = (match['start_time'])
        lobby_type = (match['lobby_type'])
        tower_damage = (match['tower_damage'])
        hero_id = (match['hero_id'])
        kills = (match['kills'])
        deaths = (match['deaths'])
        assists = (match['assists'])
        average_rank = (match['average_rank'])
        gold_per_min = (match['gold_per_min'])
        last_hits = (match['last_hits'])
        hero_damage = (match['hero_damage'])
        hero_healing = (match['hero_healing'])
        game_mode = (match['game_mode'])

    determine_streak_function()
    winrate_function()

    hd = hero_data[hero_id]['img']
    last_hero_id = 'https://api.opendota.com' + hd

    last_game_mode = game_mode_list[game_mode]
    last_lobby_type = lobby_type_list[lobby_type]

    duration_formatted = str(datetime.timedelta(seconds=(duration)))

    start_time_tz_est = datetime.datetime.fromtimestamp(start_time, datetime.timezone(datetime.timedelta(hours=-4)))
    start_time_formatted = start_time_tz_est.strftime('%B %d, %I:%M %p')

    rank_formatted = rank_list[str(average_rank)]

    match_link = "https://www.dotabuff.com/matches/" + str(match_id)
    player_title = "Zech's most recent match"

def daniel_recent_function():
    link = 'https://api.opendota.com/api/players/28407285/recentMatches?api_key="3a71b2fc-46ee-4333-98f6-e5536c8b4cb5"'
    r = requests.get(link)
    data = json.loads(r.text)


    win_loss_result = []

    for d in data:
        if (d["player_slot"] <= 5) and (d["radiant_win"] == True):
            win = 1
            win_loss_result.append(win)
        elif (d["player_slot"] >= 6) and (d["radiant_win"] == False):
            win = 1
            win_loss_result.append(win)
        else:
            loss = 0
            win_loss_result.append(loss)

    def winrate_function():
        
        recent_wins = 0

        for w in win_loss_result:
            if w == 1:
                recent_wins = recent_wins + 5
        
        global current_winrate
        
        current_winrate = recent_wins

    def if_lose_streak():

        global current_streak

        if win_loss_result[0] == 0 and win_loss_result[1] == 1:
            current_streak = 1
        elif win_loss_result[1] == 0 and win_loss_result[2] == 1:
            current_streak = 2
        elif win_loss_result[2] == 0 and win_loss_result[3] == 1:
            current_streak = 3
        elif win_loss_result[3] == 0 and win_loss_result[4] == 1:
            current_streak = 4
        elif win_loss_result[4] == 0 and win_loss_result[5] == 1:
            current_streak = 5
        elif win_loss_result[5] == 0 and win_loss_result[6] == 1:
            current_streak = 6
        elif win_loss_result[6] == 0 and win_loss_result[7] == 1:
            current_streak = 7
        elif win_loss_result[7] == 0 and win_loss_result[8] == 1:
            current_streak = 8
        elif win_loss_result[8] == 0 and win_loss_result[9] == 1:
            current_streak = 9        
        elif win_loss_result[9] == 0 and win_loss_result[10] == 1:
            current_streak = 10
        elif win_loss_result[10] == 0 and win_loss_result[11] == 1:
            current_streak = 11
        elif win_loss_result[11] == 0 and win_loss_result[12] == 1:
            current_streak = 12
        elif win_loss_result[12] == 0 and win_loss_result[13] == 1:
            current_streak = 13
        elif win_loss_result[13] == 0 and win_loss_result[14] == 1:
            current_streak = 14
        elif win_loss_result[14] == 0 and win_loss_result[15] == 1:
            current_streak = 15
        elif win_loss_result[15] == 0 and win_loss_result[16] == 1:
            current_streak = 16
        elif win_loss_result[16] == 0 and win_loss_result[17] == 1:
            current_streak = 17 
        elif win_loss_result[17] == 0 and win_loss_result[18] == 1:
            current_streak = 18
        elif win_loss_result[18] == 0 and win_loss_result[19] == 1:
            current_streak = 19
        elif win_loss_result[19] == 0:
            current_streak = 20  

    # calculates streak if the player is on a win streak
    def if_win_streak():

        global current_streak

        if win_loss_result[0] == 1 and win_loss_result[1] == 0:
            current_streak = 1
        elif win_loss_result[1] == 1 and win_loss_result[2] == 0:
            current_streak = 2
        elif win_loss_result[2] == 1 and win_loss_result[3] == 0:
            current_streak = 3
        elif win_loss_result[3] == 1 and win_loss_result[4] == 0:
            current_streak = 4
        elif win_loss_result[4] == 1 and win_loss_result[5] == 0:
            current_streak = 5
        elif win_loss_result[5] == 1 and win_loss_result[6] == 0:
            current_streak = 6
        elif win_loss_result[6] == 1 and win_loss_result[7] == 0:
            current_streak = 7
        elif win_loss_result[7] == 1 and win_loss_result[8] == 0:
            current_streak = 8
        elif win_loss_result[8] == 1 and win_loss_result[9] == 0:
            current_streak = 9        
        elif win_loss_result[9] == 1 and win_loss_result[10] == 0:
            current_streak = 10
        elif win_loss_result[10] == 1 and win_loss_result[11] == 0:
            current_streak = 11
        elif win_loss_result[11] == 1 and win_loss_result[12] == 0:
            current_streak = 12
        elif win_loss_result[12] == 1 and win_loss_result[13] == 0:
            current_streak = 13
        elif win_loss_result[13] == 1 and win_loss_result[14] == 0:
            current_streak = 14
        elif win_loss_result[14] == 1 and win_loss_result[15] == 0:
            current_streak = 15
        elif win_loss_result[15] == 1 and win_loss_result[16] == 0:
            current_streak = 16
        elif win_loss_result[16] == 1 and win_loss_result[17] == 0:
            current_streak = 17  
        elif win_loss_result[17] == 1 and win_loss_result[18] == 0:
            current_streak = 18
        elif win_loss_result[18] == 1 and win_loss_result[19] == 0:
            current_streak = 19
        elif win_loss_result[19] == 1:
            current_streak = 20

    def determine_streak_function():

        global streak_type
        global last_match_result

        if win_loss_result[0] == 0:
            if_lose_streak()
            streak_type = ("Current lose streak")
            last_match_result = ("Lost Match")
        else:
            if_win_streak()
            streak_type = ("Current Win streak")
            last_match_result = ("Won Match")

    global match_id
    global duration
    global start_time_formatted
    global lobby_type
    global tower_damage
    global hero_id
    global kills
    global deaths
    global assists
    global average_rank
    global gold_per_min
    global last_hits
    global hero_damage
    global hero_healing
    global game_mode
    global last_hero_id
    global last_game_mode
    global last_lobby_type
    global duration_formatted
    global rank_formatted
    global match_link
    global player_title
    
    for match in data[0:1]:
        match_id = (match['match_id'])
        duration = (match['duration'])
        start_time = (match['start_time'])
        lobby_type = (match['lobby_type'])
        tower_damage = (match['tower_damage'])
        hero_id = (match['hero_id'])
        kills = (match['kills'])
        deaths = (match['deaths'])
        assists = (match['assists'])
        average_rank = (match['average_rank'])
        gold_per_min = (match['gold_per_min'])
        last_hits = (match['last_hits'])
        hero_damage = (match['hero_damage'])
        hero_healing = (match['hero_healing'])
        game_mode = (match['game_mode'])

    determine_streak_function()
    winrate_function()

    hd = hero_data[hero_id]['img']
    last_hero_id = 'https://api.opendota.com' + hd

    last_game_mode = game_mode_list[game_mode]
    last_lobby_type = lobby_type_list[lobby_type]

    duration_formatted = str(datetime.timedelta(seconds=(duration)))

    start_time_tz_est = datetime.datetime.fromtimestamp(start_time, datetime.timezone(datetime.timedelta(hours=-4)))
    start_time_formatted = start_time_tz_est.strftime('%B %d, %I:%M %p')

    rank_formatted = rank_list[str(average_rank)]

    match_link = "https://www.dotabuff.com/matches/" + str(match_id)

    player_title = "Daniel's most recent match"

def luke_recent_function():
    link = 'https://api.opendota.com/api/players/46668454/recentMatches?api_key="3a71b2fc-46ee-4333-98f6-e5536c8b4cb5"'
    r = requests.get(link)
    data = json.loads(r.text)


    win_loss_result = []

    for d in data:
        if (d["player_slot"] <= 5) and (d["radiant_win"] == True):
            win = 1
            win_loss_result.append(win)
        elif (d["player_slot"] >= 6) and (d["radiant_win"] == False):
            win = 1
            win_loss_result.append(win)
        else:
            loss = 0
            win_loss_result.append(loss)

    def winrate_function():
        
        recent_wins = 0

        for w in win_loss_result:
            if w == 1:
                recent_wins = recent_wins + 5
        
        global current_winrate
        
        current_winrate = recent_wins

    def if_lose_streak():

        global current_streak

        if win_loss_result[0] == 0 and win_loss_result[1] == 1:
            current_streak = 1
        elif win_loss_result[1] == 0 and win_loss_result[2] == 1:
            current_streak = 2
        elif win_loss_result[2] == 0 and win_loss_result[3] == 1:
            current_streak = 3
        elif win_loss_result[3] == 0 and win_loss_result[4] == 1:
            current_streak = 4
        elif win_loss_result[4] == 0 and win_loss_result[5] == 1:
            current_streak = 5
        elif win_loss_result[5] == 0 and win_loss_result[6] == 1:
            current_streak = 6
        elif win_loss_result[6] == 0 and win_loss_result[7] == 1:
            current_streak = 7
        elif win_loss_result[7] == 0 and win_loss_result[8] == 1:
            current_streak = 8
        elif win_loss_result[8] == 0 and win_loss_result[9] == 1:
            current_streak = 9        
        elif win_loss_result[9] == 0 and win_loss_result[10] == 1:
            current_streak = 10
        elif win_loss_result[10] == 0 and win_loss_result[11] == 1:
            current_streak = 11
        elif win_loss_result[11] == 0 and win_loss_result[12] == 1:
            current_streak = 12
        elif win_loss_result[12] == 0 and win_loss_result[13] == 1:
            current_streak = 13
        elif win_loss_result[13] == 0 and win_loss_result[14] == 1:
            current_streak = 14
        elif win_loss_result[14] == 0 and win_loss_result[15] == 1:
            current_streak = 15
        elif win_loss_result[15] == 0 and win_loss_result[16] == 1:
            current_streak = 16
        elif win_loss_result[16] == 0 and win_loss_result[17] == 1:
            current_streak = 17 
        elif win_loss_result[17] == 0 and win_loss_result[18] == 1:
            current_streak = 18
        elif win_loss_result[18] == 0 and win_loss_result[19] == 1:
            current_streak = 19
        elif win_loss_result[19] == 0:
            current_streak = 20  

    # calculates streak if the player is on a win streak
    def if_win_streak():

        global current_streak

        if win_loss_result[0] == 1 and win_loss_result[1] == 0:
            current_streak = 1
        elif win_loss_result[1] == 1 and win_loss_result[2] == 0:
            current_streak = 2
        elif win_loss_result[2] == 1 and win_loss_result[3] == 0:
            current_streak = 3
        elif win_loss_result[3] == 1 and win_loss_result[4] == 0:
            current_streak = 4
        elif win_loss_result[4] == 1 and win_loss_result[5] == 0:
            current_streak = 5
        elif win_loss_result[5] == 1 and win_loss_result[6] == 0:
            current_streak = 6
        elif win_loss_result[6] == 1 and win_loss_result[7] == 0:
            current_streak = 7
        elif win_loss_result[7] == 1 and win_loss_result[8] == 0:
            current_streak = 8
        elif win_loss_result[8] == 1 and win_loss_result[9] == 0:
            current_streak = 9        
        elif win_loss_result[9] == 1 and win_loss_result[10] == 0:
            current_streak = 10
        elif win_loss_result[10] == 1 and win_loss_result[11] == 0:
            current_streak = 11
        elif win_loss_result[11] == 1 and win_loss_result[12] == 0:
            current_streak = 12
        elif win_loss_result[12] == 1 and win_loss_result[13] == 0:
            current_streak = 13
        elif win_loss_result[13] == 1 and win_loss_result[14] == 0:
            current_streak = 14
        elif win_loss_result[14] == 1 and win_loss_result[15] == 0:
            current_streak = 15
        elif win_loss_result[15] == 1 and win_loss_result[16] == 0:
            current_streak = 16
        elif win_loss_result[16] == 1 and win_loss_result[17] == 0:
            current_streak = 17  
        elif win_loss_result[17] == 1 and win_loss_result[18] == 0:
            current_streak = 18
        elif win_loss_result[18] == 1 and win_loss_result[19] == 0:
            current_streak = 19
        elif win_loss_result[19] == 1:
            current_streak = 20

    def determine_streak_function():

        global streak_type
        global last_match_result

        if win_loss_result[0] == 0:
            if_lose_streak()
            streak_type = ("Current lose streak")
            last_match_result = ("Lost Match")
        else:
            if_win_streak()
            streak_type = ("Current Win streak")
            last_match_result = ("Won Match")

    global match_id
    global duration
    global start_time_formatted
    global lobby_type
    global tower_damage
    global hero_id
    global kills
    global deaths
    global assists
    global average_rank
    global gold_per_min
    global last_hits
    global hero_damage
    global hero_healing
    global game_mode
    global last_hero_id
    global last_game_mode
    global last_lobby_type
    global duration_formatted
    global rank_formatted
    global match_link
    global player_title
    
    for match in data[0:1]:
        match_id = (match['match_id'])
        duration = (match['duration'])
        start_time = (match['start_time'])
        lobby_type = (match['lobby_type'])
        tower_damage = (match['tower_damage'])
        hero_id = (match['hero_id'])
        kills = (match['kills'])
        deaths = (match['deaths'])
        assists = (match['assists'])
        average_rank = (match['average_rank'])
        gold_per_min = (match['gold_per_min'])
        last_hits = (match['last_hits'])
        hero_damage = (match['hero_damage'])
        hero_healing = (match['hero_healing'])
        game_mode = (match['game_mode'])

    determine_streak_function()
    winrate_function()

    hd = hero_data[hero_id]['img']
    last_hero_id = 'https://api.opendota.com' + hd

    last_game_mode = game_mode_list[game_mode]
    last_lobby_type = lobby_type_list[lobby_type]

    duration_formatted = str(datetime.timedelta(seconds=(duration)))

    start_time_tz_est = datetime.datetime.fromtimestamp(start_time, datetime.timezone(datetime.timedelta(hours=-4)))
    start_time_formatted = start_time_tz_est.strftime('%B %d, %I:%M %p')

    rank_formatted = rank_list[str(average_rank)]

    match_link = "https://www.dotabuff.com/matches/" + str(match_id)

    player_title = "Luke's most recent match"

def david_recent_function():
    link = 'https://api.opendota.com/api/players/38754201/recentMatches?api_key="3a71b2fc-46ee-4333-98f6-e5536c8b4cb5"'
    r = requests.get(link)
    data = json.loads(r.text)


    win_loss_result = []

    for d in data:
        if (d["player_slot"] <= 5) and (d["radiant_win"] == True):
            win = 1
            win_loss_result.append(win)
        elif (d["player_slot"] >= 6) and (d["radiant_win"] == False):
            win = 1
            win_loss_result.append(win)
        else:
            loss = 0
            win_loss_result.append(loss)

    def winrate_function():
        
        recent_wins = 0

        for w in win_loss_result:
            if w == 1:
                recent_wins = recent_wins + 5
        
        global current_winrate
        
        current_winrate = recent_wins

    def if_lose_streak():

        global current_streak

        if win_loss_result[0] == 0 and win_loss_result[1] == 1:
            current_streak = 1
        elif win_loss_result[1] == 0 and win_loss_result[2] == 1:
            current_streak = 2
        elif win_loss_result[2] == 0 and win_loss_result[3] == 1:
            current_streak = 3
        elif win_loss_result[3] == 0 and win_loss_result[4] == 1:
            current_streak = 4
        elif win_loss_result[4] == 0 and win_loss_result[5] == 1:
            current_streak = 5
        elif win_loss_result[5] == 0 and win_loss_result[6] == 1:
            current_streak = 6
        elif win_loss_result[6] == 0 and win_loss_result[7] == 1:
            current_streak = 7
        elif win_loss_result[7] == 0 and win_loss_result[8] == 1:
            current_streak = 8
        elif win_loss_result[8] == 0 and win_loss_result[9] == 1:
            current_streak = 9        
        elif win_loss_result[9] == 0 and win_loss_result[10] == 1:
            current_streak = 10
        elif win_loss_result[10] == 0 and win_loss_result[11] == 1:
            current_streak = 11
        elif win_loss_result[11] == 0 and win_loss_result[12] == 1:
            current_streak = 12
        elif win_loss_result[12] == 0 and win_loss_result[13] == 1:
            current_streak = 13
        elif win_loss_result[13] == 0 and win_loss_result[14] == 1:
            current_streak = 14
        elif win_loss_result[14] == 0 and win_loss_result[15] == 1:
            current_streak = 15
        elif win_loss_result[15] == 0 and win_loss_result[16] == 1:
            current_streak = 16
        elif win_loss_result[16] == 0 and win_loss_result[17] == 1:
            current_streak = 17 
        elif win_loss_result[17] == 0 and win_loss_result[18] == 1:
            current_streak = 18
        elif win_loss_result[18] == 0 and win_loss_result[19] == 1:
            current_streak = 19
        elif win_loss_result[19] == 0:
            current_streak = 20  

    # calculates streak if the player is on a win streak
    def if_win_streak():

        global current_streak

        if win_loss_result[0] == 1 and win_loss_result[1] == 0:
            current_streak = 1
        elif win_loss_result[1] == 1 and win_loss_result[2] == 0:
            current_streak = 2
        elif win_loss_result[2] == 1 and win_loss_result[3] == 0:
            current_streak = 3
        elif win_loss_result[3] == 1 and win_loss_result[4] == 0:
            current_streak = 4
        elif win_loss_result[4] == 1 and win_loss_result[5] == 0:
            current_streak = 5
        elif win_loss_result[5] == 1 and win_loss_result[6] == 0:
            current_streak = 6
        elif win_loss_result[6] == 1 and win_loss_result[7] == 0:
            current_streak = 7
        elif win_loss_result[7] == 1 and win_loss_result[8] == 0:
            current_streak = 8
        elif win_loss_result[8] == 1 and win_loss_result[9] == 0:
            current_streak = 9        
        elif win_loss_result[9] == 1 and win_loss_result[10] == 0:
            current_streak = 10
        elif win_loss_result[10] == 1 and win_loss_result[11] == 0:
            current_streak = 11
        elif win_loss_result[11] == 1 and win_loss_result[12] == 0:
            current_streak = 12
        elif win_loss_result[12] == 1 and win_loss_result[13] == 0:
            current_streak = 13
        elif win_loss_result[13] == 1 and win_loss_result[14] == 0:
            current_streak = 14
        elif win_loss_result[14] == 1 and win_loss_result[15] == 0:
            current_streak = 15
        elif win_loss_result[15] == 1 and win_loss_result[16] == 0:
            current_streak = 16
        elif win_loss_result[16] == 1 and win_loss_result[17] == 0:
            current_streak = 17  
        elif win_loss_result[17] == 1 and win_loss_result[18] == 0:
            current_streak = 18
        elif win_loss_result[18] == 1 and win_loss_result[19] == 0:
            current_streak = 19
        elif win_loss_result[19] == 1:
            current_streak = 20

    def determine_streak_function():

        global streak_type
        global last_match_result

        if win_loss_result[0] == 0:
            if_lose_streak()
            streak_type = ("Current lose streak")
            last_match_result = ("Lost Match")
        else:
            if_win_streak()
            streak_type = ("Current Win streak")
            last_match_result = ("Won Match")

    global match_id
    global duration
    global start_time_formatted
    global lobby_type
    global tower_damage
    global hero_id
    global kills
    global deaths
    global assists
    global average_rank
    global gold_per_min
    global last_hits
    global hero_damage
    global hero_healing
    global game_mode
    global last_hero_id
    global last_game_mode
    global last_lobby_type
    global duration_formatted
    global rank_formatted
    global match_link
    global player_title
    
    for match in data[0:1]:
        match_id = (match['match_id'])
        duration = (match['duration'])
        start_time = (match['start_time'])
        lobby_type = (match['lobby_type'])
        tower_damage = (match['tower_damage'])
        hero_id = (match['hero_id'])
        kills = (match['kills'])
        deaths = (match['deaths'])
        assists = (match['assists'])
        average_rank = (match['average_rank'])
        gold_per_min = (match['gold_per_min'])
        last_hits = (match['last_hits'])
        hero_damage = (match['hero_damage'])
        hero_healing = (match['hero_healing'])
        game_mode = (match['game_mode'])

    determine_streak_function()
    winrate_function()

    hd = hero_data[hero_id]['img']
    last_hero_id = 'https://api.opendota.com' + hd

    last_game_mode = game_mode_list[game_mode]
    last_lobby_type = lobby_type_list[lobby_type]

    duration_formatted = str(datetime.timedelta(seconds=(duration)))

    start_time_tz_est = datetime.datetime.fromtimestamp(start_time, datetime.timezone(datetime.timedelta(hours=-4)))
    start_time_formatted = start_time_tz_est.strftime('%B %d, %I:%M %p')

    rank_formatted = rank_list[str(average_rank)]

    match_link = "https://www.dotabuff.com/matches/" + str(match_id)

    player_title = "David's most recent match"

def sullivan_recent_function():
    link = 'https://api.opendota.com/api/players/61886077/recentMatches?api_key="3a71b2fc-46ee-4333-98f6-e5536c8b4cb5"'
    r = requests.get(link)
    data = json.loads(r.text)


    win_loss_result = []

    for d in data:
        if (d["player_slot"] <= 5) and (d["radiant_win"] == True):
            win = 1
            win_loss_result.append(win)
        elif (d["player_slot"] >= 6) and (d["radiant_win"] == False):
            win = 1
            win_loss_result.append(win)
        else:
            loss = 0
            win_loss_result.append(loss)

    def winrate_function():
        
        recent_wins = 0

        for w in win_loss_result:
            if w == 1:
                recent_wins = recent_wins + 5
        
        global current_winrate
        
        current_winrate = recent_wins

    def if_lose_streak():

        global current_streak

        if win_loss_result[0] == 0 and win_loss_result[1] == 1:
            current_streak = 1
        elif win_loss_result[1] == 0 and win_loss_result[2] == 1:
            current_streak = 2
        elif win_loss_result[2] == 0 and win_loss_result[3] == 1:
            current_streak = 3
        elif win_loss_result[3] == 0 and win_loss_result[4] == 1:
            current_streak = 4
        elif win_loss_result[4] == 0 and win_loss_result[5] == 1:
            current_streak = 5
        elif win_loss_result[5] == 0 and win_loss_result[6] == 1:
            current_streak = 6
        elif win_loss_result[6] == 0 and win_loss_result[7] == 1:
            current_streak = 7
        elif win_loss_result[7] == 0 and win_loss_result[8] == 1:
            current_streak = 8
        elif win_loss_result[8] == 0 and win_loss_result[9] == 1:
            current_streak = 9        
        elif win_loss_result[9] == 0 and win_loss_result[10] == 1:
            current_streak = 10
        elif win_loss_result[10] == 0 and win_loss_result[11] == 1:
            current_streak = 11
        elif win_loss_result[11] == 0 and win_loss_result[12] == 1:
            current_streak = 12
        elif win_loss_result[12] == 0 and win_loss_result[13] == 1:
            current_streak = 13
        elif win_loss_result[13] == 0 and win_loss_result[14] == 1:
            current_streak = 14
        elif win_loss_result[14] == 0 and win_loss_result[15] == 1:
            current_streak = 15
        elif win_loss_result[15] == 0 and win_loss_result[16] == 1:
            current_streak = 16
        elif win_loss_result[16] == 0 and win_loss_result[17] == 1:
            current_streak = 17 
        elif win_loss_result[17] == 0 and win_loss_result[18] == 1:
            current_streak = 18
        elif win_loss_result[18] == 0 and win_loss_result[19] == 1:
            current_streak = 19
        elif win_loss_result[19] == 0:
            current_streak = 20  

    # calculates streak if the player is on a win streak
    def if_win_streak():

        global current_streak

        if win_loss_result[0] == 1 and win_loss_result[1] == 0:
            current_streak = 1
        elif win_loss_result[1] == 1 and win_loss_result[2] == 0:
            current_streak = 2
        elif win_loss_result[2] == 1 and win_loss_result[3] == 0:
            current_streak = 3
        elif win_loss_result[3] == 1 and win_loss_result[4] == 0:
            current_streak = 4
        elif win_loss_result[4] == 1 and win_loss_result[5] == 0:
            current_streak = 5
        elif win_loss_result[5] == 1 and win_loss_result[6] == 0:
            current_streak = 6
        elif win_loss_result[6] == 1 and win_loss_result[7] == 0:
            current_streak = 7
        elif win_loss_result[7] == 1 and win_loss_result[8] == 0:
            current_streak = 8
        elif win_loss_result[8] == 1 and win_loss_result[9] == 0:
            current_streak = 9        
        elif win_loss_result[9] == 1 and win_loss_result[10] == 0:
            current_streak = 10
        elif win_loss_result[10] == 1 and win_loss_result[11] == 0:
            current_streak = 11
        elif win_loss_result[11] == 1 and win_loss_result[12] == 0:
            current_streak = 12
        elif win_loss_result[12] == 1 and win_loss_result[13] == 0:
            current_streak = 13
        elif win_loss_result[13] == 1 and win_loss_result[14] == 0:
            current_streak = 14
        elif win_loss_result[14] == 1 and win_loss_result[15] == 0:
            current_streak = 15
        elif win_loss_result[15] == 1 and win_loss_result[16] == 0:
            current_streak = 16
        elif win_loss_result[16] == 1 and win_loss_result[17] == 0:
            current_streak = 17  
        elif win_loss_result[17] == 1 and win_loss_result[18] == 0:
            current_streak = 18
        elif win_loss_result[18] == 1 and win_loss_result[19] == 0:
            current_streak = 19
        elif win_loss_result[19] == 1:
            current_streak = 20

    def determine_streak_function():

        global streak_type
        global last_match_result

        if win_loss_result[0] == 0:
            if_lose_streak()
            streak_type = ("Current lose streak")
            last_match_result = ("Lost Match")
        else:
            if_win_streak()
            streak_type = ("Current Win streak")
            last_match_result = ("Won Match")

    global match_id
    global duration
    global start_time_formatted
    global lobby_type
    global tower_damage
    global hero_id
    global kills
    global deaths
    global assists
    global average_rank
    global gold_per_min
    global last_hits
    global hero_damage
    global hero_healing
    global game_mode
    global last_hero_id
    global last_game_mode
    global last_lobby_type
    global duration_formatted
    global rank_formatted
    global match_link
    global player_title
    
    for match in data[0:1]:
        match_id = (match['match_id'])
        duration = (match['duration'])
        start_time = (match['start_time'])
        lobby_type = (match['lobby_type'])
        tower_damage = (match['tower_damage'])
        hero_id = (match['hero_id'])
        kills = (match['kills'])
        deaths = (match['deaths'])
        assists = (match['assists'])
        average_rank = (match['average_rank'])
        gold_per_min = (match['gold_per_min'])
        last_hits = (match['last_hits'])
        hero_damage = (match['hero_damage'])
        hero_healing = (match['hero_healing'])
        game_mode = (match['game_mode'])

    determine_streak_function()
    winrate_function()

    hd = hero_data[hero_id]['img']
    last_hero_id = 'https://api.opendota.com' + hd

    last_game_mode = game_mode_list[game_mode]
    last_lobby_type = lobby_type_list[lobby_type]

    duration_formatted = str(datetime.timedelta(seconds=(duration)))

    start_time_tz_est = datetime.datetime.fromtimestamp(start_time, datetime.timezone(datetime.timedelta(hours=-4)))
    start_time_formatted = start_time_tz_est.strftime('%B %d, %I:%M %p')

    rank_formatted = rank_list[str(average_rank)]

    match_link = "https://www.dotabuff.com/matches/" + str(match_id)

    player_title = "Sullivan's most recent match"



nl = '\n'

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.command()
async def recent(ctx, arg):
    if arg == "roach":
        roach_recent_function()
    if arg == "zech":
        zech_recent_function()
    if arg == "daniel":
        daniel_recent_function()
    if arg == "luke":
        luke_recent_function()
    if arg == "david":
        david_recent_function()
    if arg == "sullivan":
        sullivan_recent_function()
    embed = discord.Embed(
        title=player_title,
        url=match_link,
        color=discord.Colour.dark_gold()
    )

    embed.set_thumbnail(url=(last_hero_id))
    embed.add_field(
        name='Result',
        value=(last_match_result),
        inline=False
    )        
    embed.add_field(
        name='Stats',
        value=f' Kills: {kills} {nl} Deaths: {deaths} {nl} Assists: {assists} {nl} GPM: {gold_per_min} {nl} Last hits: {last_hits} {nl} Hero damage: {hero_damage} {nl} Hero healing: {hero_healing} {nl} Building damage: {tower_damage}',
        inline=True
    )
    embed.add_field(
        name='Match info',
        value=f'Match ID: {match_id} {nl} Start time: {start_time_formatted} {nl}  Gamemode: {last_game_mode} {nl} Match type: {last_lobby_type} {nl} Duration: {duration_formatted} {nl} Average rank: {rank_formatted} {nl} ',
        inline=True
    )   
    embed.add_field(
        name=' --- ',
        value=f'{streak_type}: {current_streak} {nl} {current_winrate} percent win rate over the last 20 games',
        inline=False
    )   

    await ctx.send(embed=embed)

discord_api_key = os.getenv('discord_api_key')

bot.run(discord_api_key)