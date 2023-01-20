import discord
import requests
import json
import datetime
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

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

hero_data_link = 'https://api.opendota.com/api/heroStats'
hero_data_r = requests.get(hero_data_link)
hero_data = json.loads(hero_data_r.text)

def get_player_data(player_data_link):
    player_data_r = requests.get(player_data_link)
    player_data = json.loads(player_data_r.text)
    return player_data

def find_hero_id(hero_data, hero):
    for i, dic in enumerate(hero_data):
        if dic["localized_name"] == hero:
            return hero_data[i]["id"]
    return -1

def find_hero_name(hero_id):
    for i, dic in enumerate(hero_data):
        if dic["id"] == hero_id:
            return hero_data[i]["localized_name"]
    return -1

def find_hero_img(api_data, hero):
    for i, dic in enumerate(api_data):
        if dic["localized_name"] == hero:
            return api_data[i]["img"]
    return -1

def find_hero_stats(hero_id, player_data):
    hero_stats = []
    for i, dic in enumerate(player_data):
        if dic["hero_id"] == str(hero_id):
            hero_stats.append(player_data[i]["last_played"])
            hero_stats.append(player_data[i]["games"])
            hero_stats.append(player_data[i]["win"])
            hero_stats.append(player_data[i]["with_games"])
            hero_stats.append(player_data[i]["with_win"])
            hero_stats.append(player_data[i]["against_games"])
            hero_stats.append(player_data[i]["against_win"])
            return hero_stats
    return -1

def find_recent_match_data(player_data):

    recent_match_data = []

    for i in player_data[0:1]:
        recent_match_data.append(i['match_id'])     #0  
        recent_match_data.append(i['player_slot'])  #1
        recent_match_data.append(i['radiant_win'])  #2
        recent_match_data.append(i['duration'])     #3
        recent_match_data.append(i['game_mode'])    #4
        recent_match_data.append(i['lobby_type'])   #5
        recent_match_data.append(i['hero_id'])      #6      
        recent_match_data.append(i['start_time'])   #7
        recent_match_data.append(i['version'])      #8
        recent_match_data.append(i['kills'])        #9
        recent_match_data.append(i['deaths'])       #10
        recent_match_data.append(i['assists'])      #11
        recent_match_data.append(i['skill'])        #12
        recent_match_data.append(i['average_rank']) #13
        recent_match_data.append(i['xp_per_min'])   #14
        recent_match_data.append(i['gold_per_min']) #15
        recent_match_data.append(i['hero_damage'])  #16
        recent_match_data.append(i['tower_damage']) #17
        recent_match_data.append(i['hero_healing']) #18
        recent_match_data.append(i['last_hits'])    #19
        recent_match_data.append(i['lane'])         #20
        recent_match_data.append(i['lane_role'])    #21
        recent_match_data.append(i['is_roaming'])   #22
        recent_match_data.append(i['cluster'])      #23
        recent_match_data.append(i['leaver_status'])#24
        recent_match_data.append(i['party_size'])   #25
        recent_match_data.append(find_hero_name(recent_match_data[6])) #26
        return recent_match_data

def calculate_percentage(num1, num2):
    if num2 == 0:
        return 0
    if num1 == 0:
        return "no data"
    return round(num1 / num2 * 100, 1)

def get_recent_streaks(recent_match_data):

    win_loss_result = [] 

    for d in recent_match_data:   # Compile the win/loss in a list (might be able to simplify this)
        if (d["player_slot"] <= 5) and (d["radiant_win"] == True):
            win = 1
            win_loss_result.append(win)
        elif (d["player_slot"] >= 6) and (d["radiant_win"] == False):
            win = 1
            win_loss_result.append(win)
        else:
            loss = 0
            win_loss_result.append(loss)

    return win_loss_result

def calculate_recent_streaks(win_loss_results): # Calculate the win and loss streaks
    index = 0
    result_length = len(win_loss_results)
    current_win_streak = 0
    current_loss_streak = 0

    for i in range(1):
        if win_loss_results[index] == 1:  # If the last game played is a win
            for game in range(index, result_length): # Count wins until you encounter a loss
                if win_loss_results[game] == 1:
                    current_win_streak += 1
                    index += 1
                else:
                    break   # Loss encountered - Stop counting
        else:
            for game in range(index, result_length): # If the last game played is a loss
                if  win_loss_results[game] == 0:     # Count losses until you encounter a win
                    current_loss_streak += 1
                    index += 1
                else:
                    break

    return (current_win_streak, current_loss_streak) # Returning the values

def find_winrate(win_loss_results):
    current_winrate = 0
    for w in win_loss_results:
        if w == 1:
            current_winrate = current_winrate + 5
    return current_winrate


bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.command(name='herostats')
# the additioanl arguements are here for heros that have more than one word in their name
async def send_hero_stats(ctx, player, hero=None, string_arg1='', string_arg2='', string_arg3=''):
    if player == "daniel":
        link = "https://api.opendota.com/api/players/28407285/heroes"
    if player == "zech":
        link = "https://api.opendota.com/api/players/67380505/heroes"
    if player == "luke":
        link = "https://api.opendota.com/api/players/46668454/heroes"
    if player == "david":
        link = "https://api.opendota.com/api/players/38754201/heroes"
    if player == "sullivan":
        link = "https://api.opendota.com/api/players/61886077/heroes"
    if player == "roach":
        link = "https://api.opendota.com/api/players/311160163/heroes"
    if string_arg3 != '':
        hero = hero.capitalize() + ' ' + string_arg1.lower() + ' ' + string_arg2.lower() + ' ' +string_arg3.capitalize()
    elif string_arg2 != '':
        hero = hero.capitalize() + ' ' + string_arg1.lower() + ' ' + string_arg2.capitalize()  
    elif string_arg1 != '':
        hero = hero.capitalize() + ' ' + string_arg1.capitalize()
    elif string_arg1 == '':
        hero = hero.capitalize()

    stats = find_hero_stats(find_hero_id(hero_data, hero), get_player_data(link))

    if stats[0] == 0:
        last_played = "Never"
    else:
        last_played = datetime.datetime.fromtimestamp(stats[0]).strftime("%B %d %Y")

    embed = discord.Embed(
        title= f'{player.capitalize()}\'s stats with {hero}',
        color=discord.Colour.dark_green()
    )

    embed.set_thumbnail(
        url=('https://api.opendota.com' + find_hero_img(hero_data, hero))
    )

    embed.add_field(
        name="Stats",
        value=f'Last played: {last_played}\n\n'
              f'Games played as: {stats[1]}\n'
              f'Win percentage as: {calculate_percentage(stats[2],stats[1])}\n\n'
              f'Games played with: {stats[3]}\n'
              f'Win percentage with: {calculate_percentage(stats[4], stats[3])}\n\n'
              f'Games played against: {stats[5]}\n'
              f'Win percentage against: {calculate_percentage(stats[6], stats[5])}'
    )

    await ctx.send(embed=embed)


@bot.command(name='recent')
async def send_recent_match(ctx, player):
    if player == "daniel":
        link = "https://api.opendota.com/api/players/28407285/recentMatches"
    if player == "zech":
        link = "https://api.opendota.com/api/players/67380505/recentMatches"
    if player == "luke":
        link = "https://api.opendota.com/api/players/46668454/recentMatches"
    if player == "david":
        link = "https://api.opendota.com/api/players/38754201/recentMatches"
    if player == "sullivan":
        link = "https://api.opendota.com/api/players/61886077/recentMatches"
    if player == "roach":
        link = "https://api.opendota.com/api/players/311160163/recentMatches"
    if player == "test":
        link = "https://api.opendota.com/api/players/136241973/recentMatches"
    
    player_data = get_player_data(link)
    last_match_stats = find_recent_match_data(player_data)
    hero = last_match_stats[26]
    match_end_time = datetime.datetime.fromtimestamp(last_match_stats[7], datetime.timezone(datetime.timedelta(hours=-4))).strftime('%B %d, %I:%M %p')
    match_duration = str(datetime.timedelta(seconds=(last_match_stats[3])))
    recent_streak = get_recent_streaks(player_data)
    winrate = find_winrate(recent_streak)
    calculated_streak = calculate_recent_streaks(recent_streak)

    if calculated_streak[0] > 0:
        streak_type = "Win"
        streak_length = calculated_streak[0]
    else:
        streak_type = "Loss"
        streak_length = calculated_streak[1]


    embed = discord.Embed(
        title= f'{player.capitalize()}\'s most recent match',
        url='https://www.dotabuff.com/matches/' + str(last_match_stats[0]),
        color=discord.Colour.dark_gold()
    )

    embed.set_thumbnail(url=('https://api.opendota.com' + find_hero_img(hero_data, hero)))
    embed.add_field(
        name='Result',
        value=(streak_type), # <-- win/loss of last match
        inline=False
    )

    embed.add_field(
        name='Stats',
        value=f'Kills: {last_match_stats[9]}\n'
              f'Deaths: {last_match_stats[10]}\n'
              f'Assists: {last_match_stats[11]}\n'
              f'GPM: {last_match_stats[15]}\n'
              f'Last hits: {last_match_stats[19]}\n'
              f'Hero damage: {last_match_stats[16]}\n'
              f'Hero healing: {last_match_stats[18]}\n'
              f'Building damage: {last_match_stats[17]}\n',
        inline=True
    )
    embed.add_field(
        name='Match info',
        value=f'Match ID: {last_match_stats[0]}\n'
              f'Start time (EST): {match_end_time}\n'
              f'Gamemode: {game_mode_list[last_match_stats[4]]}\n'
              f'Match type: {lobby_type_list[last_match_stats[5]]}\n'
              f'Duration: {match_duration}\n'
              f'Average rank: {rank_list[str(last_match_stats[13])]}\n'
              f'Party size: {last_match_stats[25]}\n',
        inline=True
    )
    embed.add_field(
        name=' --- ',
        value=f'Current {streak_type} streak: {streak_length}\n'
              f'{winrate} percent win rate over the last 20 games',
        inline=False
    )

    await ctx.send(embed=embed)


global party_members
party_members = []

@bot.command(name='party')
async def create_party(ctx, time=None, gamemode=None):

    # clears the party and adds the caller to the party
    party_members.clear()
    party_members.append(ctx.author.display_name)
    if time == None:
        await ctx.send(f'<@&620867662456553482> {ctx.author.mention} started a party')
    elif time[0] == "@":
        await ctx.send(f'<@&620867662456553482> {ctx.author.mention} is playing {time}')
    elif time[0] != "@":
        await ctx.send(f'<@&620867662456553482> {ctx.author.mention} is playing in {time}')
    await ctx.send(f'Members: {", ".join(party_members)}')

@bot.command(name='join')
async def join_party(ctx):

    # check if user is in the party and sends an error if they are
    if ctx.author.display_name in party_members:
        await ctx.send(f'{ctx.author.mention} is already in the party')
        return


    # if ther is no party, send an error
    if len(party_members) == 0:
        await ctx.send(f'{ctx.author.mention} no party has been started. you can start a party with the $party command')
        return


    # if the party is full, send an error message 
    if len(party_members) == 5:
        await ctx.send(f'party is full.')
        await ctx.send(f'Members: {", ".join(party_members)}')
        return


    # add member to the party and send a message
    party_members.append(ctx.author.display_name)
    await ctx.send(f'{ctx.author.mention} joined the party')


    # some various messages at certain party sizes
    if len(party_members) == 4:
        await ctx.send(f'<@&620867662456553482> need one more for a five stack')

    if len(party_members) == 5:
        await ctx.send(f'five stack time let\'s go. don\'t let luke random')


    # print the names of all members in the party
    await ctx.send(f'Members: {", ".join(party_members)}')



@bot.command(name='leave')
async def leave_party(ctx):

    # find the party that the user is a member of
    if ctx.author.display_name in party_members:
        party_members.remove(ctx.author.display_name)
        await ctx.send(f'{ctx.author.mention} left the party')
        await ctx.send(f'Members: {", ".join(party_members)}')
        

    # if the user is not a member of any party, send an error message
    if len(party_members) == 0:
        await ctx.send(f'party is empty. you can start one with the $party command')
        return

discord_api_key = os.getenv('discord_api_key')

bot.run(discord_api_key)