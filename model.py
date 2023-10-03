import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import random
from textblob import TextBlob
data = pd.read_csv('playlist_data.csv')

theme_mapping = {
    'romantic': ['romantic', 'love story', 'couples', 'heartfelt', 'affectionate', 'passionate', 'intimate', 'surprise', 'tender', 'intimate', 'amorous', 'fond', 'lovers', 'beloved', 'valentine', 'infatuated'],
    'love': ['love', 'affection', 'passion', 'adoration', 'infatuation', 'tenderness', 'endearment', 'warmth', 'fondness', 'attachment', 'devotion', 'emotion', 'care', 'admiration', 'crush', 'sweetheart'],
    'party': ['party', 'celebration', 'festive', 'fun', 'festivity', 'merriment', 'revelry', 'jovial', 'fiesta', 'festoon', 'gala', 'festal', 'bash', 'get-together', 'fiesta', 'celebrate'],
    'happy': ['happy', 'joy', 'elated', 'ecstatic', 'cheerful', 'blissful', 'radiant', 'delighted', 'pleased', 'content', 'upbeat', 'gleeful', 'smile', 'laugh', 'jubilant', 'exhilarated'],
    'neutral': ['neutral', 'okay', 'fine', 'not bad', 'indifferent', 'nonchalant', 'apathetic', 'disinterested', 'uninvolved', 'unconcerned', 'unemotional', 'dispassionate', 'unbiased', 'detached', 'impartial', 'objective'],
    'sad': ['sad', 'breakup','break up', 'unhappy', 'heartbroken', 'melancholy', 'gloomy', 'desolate', 'dejected', 'downcast', 'mournful', 'sorrowful', 'depressed', 'down', 'tearful', 'grief', 'disheartened','low'],
    'devotional': ['devotional', 'god','spiritual', 'divine', 'worship', 'sacred', 'holy', 'reverent', 'sacrosanct', 'pious', 'religious', 'faithful', 'reverential', 'pray', 'meditate', 'church', 'temple'],
}
def predict_theme(user_input):
    blob = TextBlob(user_input)
    sentiment_score = blob.sentiment.polarity
    best_matched_theme = None
    best_match_score = -1
    for theme, keywords in theme_mapping.items():
        match_score = sum(blob.words.count(keyword) for keyword in keywords) + sentiment_score
        if match_score > best_match_score:
            best_matched_theme = theme
            best_match_score = match_score

    if best_matched_theme:
        return best_matched_theme
    else:
        print("No specific theme matches the input.")
    return best_matched_theme
sentences = ["The party was a celebration of their success."]

def predictions(text):
    results = []
    for i in text:
        results.append(predict_theme(i))
        for i in range(len(results)):
            if results[i] == 'neutral':
                results[i] = 'happy'
            if results[i] == 'sad':
                results[i] = 'breakup'
    print( results)
    theme_songs = data.groupby('Theme')['Song Name'].apply(list).to_dict()
    song_suggestions = []
    for theme in results:
        songs_for_theme = theme_songs.get(theme, [])
        num_songs_to_select = min(5, len(songs_for_theme)) 
        suggestions = random.sample(songs_for_theme, num_songs_to_select)
        song_suggestions.append(suggestions)

    for theme, suggestions in zip(results, song_suggestions):
        print(f"Predicted Theme: {theme}")
        for song in suggestions:
            print(f"- {song}")
        print()
    return results,song_suggestions[0]
# predictions(sentences)
