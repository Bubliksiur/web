from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutMe')
def aboutMe():
    return render_template('aboutMe.html')

#1
@app.route('/firstProject')
def moveToFirst():
    return render_template('first.html')

#2
@app.route('/secondProject')
def moveToSecond():
    return render_template('second.html')

#3
@app.route('/thirdProject')
def moveToThird():
    return render_template('third.html')

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(debug=True)
