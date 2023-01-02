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

def calc_recent_streaks(win_loss_results): # Calculate the win and loss streaks
    index = 0
    result_length = len(win_loss_results)
    current_win_streak = 0
    current_loss_streak = 0

    # Do this twice to count the wins then the losses
    for i in range(2):
        if win_loss_results[index] == 1:  # If the last game played is a win
            for game in range(index, result_length): # Count wins until you encounter a loss
                if win_loss_results[game] == 1:
                    current_win_streak += 1
                    index += 1
                else:
                    break   # Loss encountered - Stop counting
        else:
            for game in range(index, result_length): # If the last game played is a loss
                if  win_loss_results[game] == 0:           # Count losses until you encounter a win
                    current_loss_streak += 1
                    index += 1
                else:
                    break

    return (current_win_streak, current_loss_streak) # Returning the values

def get_recent_streaks(link, arg):
    r = requests.get(link)
    data = json.loads(r.text)

    win_loss_result = [] 

    for d in data:   # Compile the win/loss in a list (might be able to simplify this)
        if (d["player_slot"] <= 5) and (d["radiant_win"] == True):
            win = 1
            win_loss_result.append(win)
        elif (d["player_slot"] >= 6) and (d["radiant_win"] == False):
            win = 1
            win_loss_result.append(win)
        else:
            loss = 0
            win_loss_result.append(loss)

    streaks = calc_recent_streaks(win_loss_result)  # index 0 = wins, 1 = losses

    global streak_type
    global last_match_result
    global current_streak

    if win_loss_result[0] == 0:
        current_streak = streaks[1]
        streak_type = ("Current lose streak")
        last_match_result = ("Lost Match")
    else:
        current_streak = streaks[0]
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
        
    global current_winrate
    current_winrate = 0
    for w in win_loss_result:
        if w == 1:
            current_winrate = current_winrate + 5

    hd = hero_data[hero_id]['img']
    last_hero_id = 'https://api.opendota.com' + hd

    last_game_mode = game_mode_list[game_mode]
    last_lobby_type = lobby_type_list[lobby_type]

    duration_formatted = str(datetime.timedelta(seconds=(duration)))

    start_time_tz_est = datetime.datetime.fromtimestamp(start_time, datetime.timezone(datetime.timedelta(hours=-4)))
    start_time_formatted = start_time_tz_est.strftime('%B %d, %I:%M %p')

    rank_formatted = rank_list[str(average_rank)]

    match_link = "https://www.dotabuff.com/matches/" + str(match_id)

    arg = arg.capitalize() # Captialize the first character of the name / command
    player_title = f"{arg}'s most recent match"

nl = '\n'

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.command()
async def recent(ctx, arg=1): # Since all players were basically the same function, we pass in the player's profile link instead of having 6x multiples of the same function
    if arg == "roach":
        link = 'https://api.opendota.com/api/players/311160163/recentMatches?api_key="3a71b2fc-46ee-4333-98f6-e5536c8b4cb5"' # profile links all in one place to make it easier to update
        get_recent_streaks(link, arg) # arg is passed in purely for the player_title string
    if arg == "zech":
        link = 'https://api.opendota.com/api/players/67380505/recentMatches?api_key="3a71b2fc-46ee-4333-98f6-e5536c8b4cb5"'
        get_recent_streaks(link, arg)
    if arg == "daniel":
        link = 'https://api.opendota.com/api/players/28407285/recentMatches?api_key="3a71b2fc-46ee-4333-98f6-e5536c8b4cb5"'
        get_recent_streaks(link, arg)
    if arg == "luke":
        link = 'https://api.opendota.com/api/players/46668454/recentMatches?api_key="3a71b2fc-46ee-4333-98f6-e5536c8b4cb5"'
        get_recent_streaks(link, arg)
    if arg == "david":
        link = 'https://api.opendota.com/api/players/38754201/recentMatches?api_key="3a71b2fc-46ee-4333-98f6-e5536c8b4cb5"'
        get_recent_streaks(link, arg)
    if arg == "sullivan":
        link = 'https://api.opendota.com/api/players/61886077/recentMatches?api_key="3a71b2fc-46ee-4333-98f6-e5536c8b4cb5"'
        get_recent_streaks(link, arg)
    if arg == 1:
        await ctx.send(f'you must provide a player arguement to get recent match data. (e.g., $recent roach)')
        return
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
        value=f'Match ID: {match_id} {nl} End time (EST): {start_time_formatted} {nl}  Gamemode: {last_game_mode} {nl} Match type: {last_lobby_type} {nl} Duration: {duration_formatted} {nl} Average rank: {rank_formatted} {nl} ',
        inline=True
    )   
    embed.add_field(
        name=' --- ',
        value=f'{streak_type}: {current_streak} {nl} {current_winrate} percent win rate over the last 20 games',
        inline=False
    )   

    await ctx.send(embed=embed)


global party_members
party_members = []

@bot.command(name='party')
async def create_party(ctx):

    # clears the party and adds the caller to the party
    print(ctx)
    party_members.clear()
    party_members.append(ctx.author.display_name)
    await ctx.send(f'<@&620867662456553482> {ctx.author.mention} started a party')
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