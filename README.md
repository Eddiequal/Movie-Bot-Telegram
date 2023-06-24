# Movie-Bot-Telegram
This Telegram bot is designed to provide users with random movie recommendations based on their preferred genre. It utilizes the Telebot module in Python and integrates with the Telegram platform.

Features
Generates random movie recommendations from a wide range of genres.
Retrieves movie details such as title, release date, overview, and poster image.
Provides an interactive interface for users to select genres and receive movie recommendations.

Prerequisites
Before running the bot, make sure you have the following prerequisites:
Python 3.x installed on your machine.
The telebot module installed. You can install it using the following command:
- pip install pyTelegramBotAPI -

An API key from The Movie Database (TMDb) to access movie data. You can obtain an API key by creating an account on their website.
Installation
1. Clone the repository to your local machine:
- git clone https://github.com/Eddiequal/movie-bot.git -
2. Navigate to the project directory:
- cd movie-bot -
3. Open the movie_bot.py file in a text editor.
4. Replace 'BOT_TOKEN' with your Telegram bot token obtained from the BotFather.
5. Replace 'API_KEY' with your TMDb API key.

Usage
To run the Movie Bot, execute the following command:
- python movie_bot.py -

Once the bot is up and running, you can interact with it on Telegram.

Start the bot by sending the /start command.
- The bot will display a welcome message and a photo.
- To view the list of genres, click on the button labeled "Go to list of genres".
- Select a genre by clicking on the corresponding button.
- The bot will respond with a random movie recommendation from the selected genre, including the title, release date, overview, and poster image.
- You can navigate back to the genre list or choose another genre by using the provided buttons.
- To stop the bot, send the /stop command.


