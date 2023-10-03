from flask import Flask, render_template, request
from model import  predictions
from song_extraction import play_song

theme = []
songs  = []
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text_analysis', methods=['GET', 'POST'])
def text_analysis():
    global theme , songs
    if request.method == 'POST':
        user_input = request.form['user_input']
        sentences = [user_input]
        results = predictions(sentences)
        theme.append(results[0])
        songs.append(results[1])                       
        return render_template('text_analysis.html', user_input=user_input, results=results)
    return render_template('text_analysis.html', user_input="", results=[])

@app.route('/play_random_song', methods=['GET', 'POST'])
def play_random_song():
    if theme and songs:
        print("Selected Theme:", theme[0])
        print("Selected Song:", songs[0])
        play_song(theme[0] , songs[0])
        return render_template('text_analysis.html')
       
    return render_template('text_analysis.html', user_input="", results=[])     


@app.route('/webcam')
def webcam():
    return render_template('index.html')

@app.route('/playlist')
def playlist():
    return render_template('playlist.html')

@app.route('/artist')
def artist():
    return render_template('artist.html')

@app.route('/about')
def about():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)