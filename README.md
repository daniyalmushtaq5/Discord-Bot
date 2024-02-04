Discord Betting Bot
Overview
This is a Discord bot script written in Python that provides betting information and statistics to users. The bot fetches data about active bets and generates statistics based on betting activity over daily, weekly, and monthly intervals.
Features
    • Fetches active bets and updates users in designated channels.
    • Provides statistics on the number of bets, wins, and losses over specified time intervals.
    • Generates pie chart visualizations for betting statistics.
Requirements
    • Python 3.x
    • discord.py library
    • matplotlib library
    • Discord bot token
Installation
    1. Clone or download the repository to your local machine.
    2. Install the required Python packages using pip:
       bashCopy code
       pip install -r requirements.txt
    3. Obtain a Discord bot token from the Discord Developer Portal.
    4. Create a .env file in the project directory and add the following line:
       makefileCopy code
       DISCORD_TOKEN=your_discord_token_here
    5. Customize the bot's behavior and channels using the constants.py file.
Usage
    1. Run the Python script:
       bashCopy code
       python bot.py
    2. The bot will connect to Discord and start running.
    3. Users can interact with the bot using the specified command prefix.
Commands
    • !help: Displays available commands and usage information.
    • Custom commands can be added based on specific requirements.
Contributors
    • Your Name
    • Contributions are welcome through pull requests.
License
This project is licensed under the MIT License.
Disclaimer
    • This bot is provided as-is with no guarantees. Use it responsibly and ensure compliance with Discord's Terms of Service and community guidelines.
    • The bot may require periodic updates or maintenance based on changes in Discord API or dependencies.

