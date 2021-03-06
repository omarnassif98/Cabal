from flask import render_template, send_from_directory
from webapp import app
print('View controller online')

@app.route('/')
def Landing():
    return render_template('Landing.html')

@app.route('/browse')
def Login():
    return render_template('browse games.html')

@app.route('/game')
def Game():
    return render_template('game.html')

@app.route('/europe')
def SendEuropeSVG():
    return send_from_directory('static', 'europe.svg')

@app.route('/tank')
def SendTankGraphic():
    return send_from_directory('static', 'tank.svg')

@app.route('/gameState')
def SendProvinceData():
    print('SENDING JSON... HERE GOES')
    return send_from_directory('static', 'GameInfo.json')
