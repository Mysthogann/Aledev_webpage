from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/lsi')
def lsi():
    return render_template('lsi.html')

@app.route('/pixelFighters')
def pixelFighters():
    return render_template('pixelFighters.html')

@app.route('/play_pixelFighters')
def playpixelFighters():
    return render_template('play_pixelFighters.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
