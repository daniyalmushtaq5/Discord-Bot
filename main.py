import matplotlib.pyplot as plt
import datetime
import asyncio
from typing import Final, Literal
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents, Embed, Color, File
from responses import get_active_bets, get_bets_stats_in_time_interval
import constants as ct


load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

intents: Intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

wager_filter = 40

async def send_active_bets_update():
    print("Sending active bets update...")
    channel = bot.get_channel(ct.PREMIUM_PICKS_CHANNEL_ID)
    fdp_channel = bot.get_channel(ct.FREE_DAILY_PICKS_CHANNEL_ID)

    if not channel or not fdp_channel:
        return

    bets_data = get_active_bets()

    embed = Embed(title="Active Bets Information", color=Color.purple())
    fdp_embed = Embed(title="Bets Information", color=Color.purple())

    bet_number = 1
    for bet in bets_data:
        if bet["risk"]["units"] != wager_filter:
            continue
        field_title = f"Bet {bet_number}"
        field_value = (
            f"**Label:** {bet['label']}\n"
            f"**Sub Label:** {bet['sub_label']}\n"
            f"**Sport:** {bet['sport']}\n"
            f"**Odds:** {bet['line']['cost']}\n"
            f"**Date and Time:** {bet['event_time']}\n"
        )

        try:
            participants = f"**Participants:** {bet['event']['participants'][0]['id']} vs {bet['event']['participants'][1]['id']}"
            field_value += participants
        except:
            field_value += "**Participants:**"
            for sub_bet_idx, sub_bet in enumerate(bet["parlay"]):
                participants = f"{sub_bet['event']['participants'][0]['id']} vs {sub_bet['event']['participants'][1]['id']}"
                field_value += f"\n   {sub_bet_idx + 1}) {participants}"

        embed.add_field(name=field_title, value=field_value, inline=False)

        if bet_number <= 2:
            fdp_embed.add_field(name=field_title, value=field_value, inline=False)

        bet_number += 1

    await channel.purge()
    await channel.send(embed=embed)

    await fdp_channel.purge()
    await fdp_channel.send(embed=fdp_embed)

async def send_bets_in_time_interval(duration: Literal["D", "W", "M"]):
    time_interval = {
        "D": "Daily",
        "W": "Weekly",
        "M": "Monthly",
    }

    print(f"Sending {time_interval[duration]} Bets update...")
    channel = bot.get_channel(ct.INTERVAL_TO_CHANNEL_ID[duration])
    if not channel:
        return
    
    num_of_bets, num_of_wins, num_of_losses = await bot.loop.run_in_executor(
        None, get_bets_stats_in_time_interval, duration, wager_filter
    )

    if num_of_bets == 0:
        embed = Embed(
        title=f"{time_interval[duration]} Bets Stats", color=Color.purple())

        embed.add_field(
            name="Number of Bets",
            value=str(num_of_bets),
            inline=True,
        )
        embed.add_field(
            name="Number of Wins",
            value=str(num_of_wins),
            inline=True,
        )
        embed.add_field(
            name="Number of Losses",
            value=str(num_of_losses),
            inline=True,
        )

        await channel.purge()
        await channel.send(embed=embed)

    else:

        chart_filename = "bet_stats_pie_chart.png"

        labels = ["Wins", "Losses"]
        sizes = [num_of_wins, num_of_losses]
        colors = ["green", "red"]

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
        ax.axis("equal") 

        plt.savefig(chart_filename)
        plt.close()

        chart_image = File(chart_filename)
        embed = Embed(
            title=f"{time_interval[duration]} Bets Stats", color=Color.purple()
        )
        embed.add_field(
            name="Number of Bets",
            value=str(num_of_bets),
            inline=True,
        )
        embed.add_field(
            name="Number of Wins",
            value=str(num_of_wins),
            inline=True,
        )
        embed.add_field(
            name="Number of Losses",
            value=str(num_of_losses),
            inline=True,
        )

        embed.set_image(url=f"attachment://{chart_filename}")

        await channel.purge()
        await channel.send(embed=embed, file=chart_image)

async def send_bet_updates():
    await send_active_bets_update()
    await send_bets_in_time_interval("D")
    await send_bets_in_time_interval("W")
    await send_bets_in_time_interval("M")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is now running!")
    print("==============================================")
    await send_bet_updates()
    await bot.close()



bot.run(token=TOKEN)
