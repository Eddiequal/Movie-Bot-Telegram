import telebot
import schedule
from telebot.types import  ReplyKeyboardMarkup
import time
import random
from telebot import types
import requests

BOT_TOKEN = '6190201255:AAECBWRJa3EaE0MpeBiojSfVyMh6jU7OvC0'
API_KEY = 'cf12207688575407453bac28c488bd1f'

bot = telebot.TeleBot(BOT_TOKEN)

def get_movie_ids_by_genre(genre):
    response = requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres={genre}')
    response_json = response.json()
    movie_ids = [movie['id'] for movie in response_json['results']]
    return movie_ids


def get_movie_details(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US')
    response_json = response.json()
    title = response_json['title']
    overview = response_json['overview']
    release_date = response_json['release_date']
    poster_path = response_json['poster_path']
    poster_url = f'https://image.tmdb.org/t/p/w500/{poster_path}'
    return {'title': title, 'release_date': release_date, 'overview': overview, 'poster_url': poster_url}


genres = {
    28: 'Action',
    12: 'Adventure',
    16: 'Animation',
    35: 'Comedy',
    80: 'Crime',
    99: 'Documentary',
    18: 'Drama',
    10751: 'Family',
    14: 'Fantasy',
    36: 'History',
    27: 'Horror',
    10402: 'Music',
    9648: 'Mystery',
    10749: 'Romance',
    878: 'Science Fiction',
    10770: 'TV Movie',
    53: 'Thriller',
    10752: 'War',
    37: 'Western'
}


@bot.message_handler(commands=['start', 'stop'])
def send_photo(message):
    command = message.text.split()[0]
    if command == '/start':
        bot.send_photo(message.chat.id, 'https://www.creativefabrica.com/wp-content/uploads/2020/09/24/Cinema-Illustration-Graphics-5660618-1-580x386.jpg', caption='Hello! I am a Movie Bot and I will choose a random movie for you!',)
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Go to list of genres')
        markup.add(item1)
        bot.send_message(message.chat.id, 'Please go to list of genres', reply_markup=markup )
        
        
    elif command == '/stop':
        bot.send_message(message.chat.id, "stopping")
        schedule.clear('schedule')
        time.sleep(1)
        bot.send_message(message.chat.id, "Have a great movie time!")
        exit()

button_texts = ["28", "12", "16", "35", "27", "9648", "878", "14", "80"]
        
@bot.message_handler(content_types=['text'])
def handle_buttons(message):
    if message.text == 'Go to list of genres':
        bot.send_photo(message.chat.id, 'https://support.musicgateway.com/wp-content/uploads/2021/06/most-popular-movie-genres.png', caption='Here is the list of genres:')
        handle_start(message)
        button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        action_button = types.KeyboardButton('28')
        adv_button = types.KeyboardButton('12')
        anim_button = types.KeyboardButton('16')
        com_button = types.KeyboardButton('35')
        hor_button = types.KeyboardButton('27')
        mys_button = types.KeyboardButton('9648')
        sci_button = types.KeyboardButton('878')
        fan_button = types.KeyboardButton('14')
        cri_button = types.KeyboardButton('80')
        thr_button = types.KeyboardButton('53')
        his_button = types.KeyboardButton('36')
        back_button = types.KeyboardButton('Go back to genres')

        
        
        button.add(action_button, adv_button,anim_button,com_button,hor_button,mys_button,sci_button,fan_button, cri_button,thr_button,his_button,back_button)
        bot.send_message(message.chat.id, 'Choose a number', reply_markup=button)
        
    if message.text == 'Go back to genres':
        handle_start(message)
        
    if message.text in button_texts:
        selected_genre_id = message.text
        
        movie_ids = get_movie_ids_by_genre(selected_genre_id)

        random_movie_id = random.choice(movie_ids)

        movie_details = get_movie_details(random_movie_id)
    
        bot.send_message(message.chat.id, f'Title: {movie_details["title"]}\nRelease: {movie_details["release_date"]}\nOverview: {movie_details["overview"]}')
        bot.send_photo(message.chat.id, photo=movie_details["poster_url"]) 
        

    
@bot.message_handler(commands=['stop'])
def bot_stop(message):
    bot.send_message(message.chat.id, 'Bot is stopped')
     
        
@bot.message_handler(func=lambda message: True)
def handle_start(message):
    # Send a message to the user with the available genres
    genre_message = 'List:\n'
    for genre_id, genre_name in genres.items():
        genre_message += f'{genre_id}: {genre_name}\n'
    bot.send_message(message.chat.id, genre_message)
        
    
bot.infinity_polling()
