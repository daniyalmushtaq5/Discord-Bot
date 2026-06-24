# Discord Bot

## Overview

A Discord bot built with Python that provides betting information and performance statistics to users. The bot tracks betting activity, retrieves active bets, and generates statistical insights over daily, weekly, and monthly periods. It also creates visual pie charts to help users analyze betting performance.

---

## Features

* Fetches active bets and posts updates to designated Discord channels.
* Tracks betting performance over multiple time periods.
* Displays:

  * Total Bets
  * Wins
  * Losses
* Generates pie chart visualizations for betting statistics.
* Provides betting summaries through Discord commands.
* Easily customizable and extendable for additional betting-related functionality.

---

## Requirements

* Python 3.x
* `discord.py`
* `matplotlib`
* Discord Bot Token

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/discord-betting-bot.git
cd discord-betting-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a Discord Bot

1. Visit the Discord Developer Portal.
2. Create a new application.
3. Create a bot under the application.
4. Copy the bot token.

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
DISCORD_TOKEN=your_discord_token_here
```

### 5. Configure Bot Settings

Customize the bot's behavior, channels, and other settings in:

```text
constants.py
```

---

## Usage

Start the bot by running:

```bash
python bot.py
```

Once started:

1. The bot connects to Discord.
2. Begins monitoring betting activity.
3. Responds to user commands in configured servers and channels.

---

## Commands

### `!help`

Displays available commands and usage information.

```text
!help
```

### Custom Commands

Additional commands can be implemented based on project requirements.

---

## Statistics & Reporting

The bot provides statistics for:

* Daily betting activity
* Weekly betting activity
* Monthly betting activity

Metrics include:

* Total Bets
* Total Wins
* Total Losses
* Win/Loss Ratios

### Visualization

The bot automatically generates pie charts to visually represent betting performance and outcomes.

---

## Project Structure

```text
discord-betting-bot/
│
├── bot.py
├── constants.py
├── requirements.txt
├── .env
└── README.md
```

---

## Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project in accordance with the license terms.

---

## Disclaimer

* This bot is provided **as-is** without any warranties or guarantees.
* Users are responsible for ensuring compliance with Discord's Terms of Service and Community Guidelines.
* Periodic updates may be required due to changes in the Discord API, third-party services, or project dependencies.

---

## Author

**Daniyal Mushtaq**

Python Developer | Automation Engineer | Discord Bot Developer

GitHub: https://github.com/daniyalmushtaq5
