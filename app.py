from flask import Flask, jsonify
from data import teams

app = Flask(__name__)

@app.route('/teams')
def getTeams():
    return jsonify({"teams": teams})

@app.route('/teams/<string:name>')
def getTeam(name):
    teamFound = [team for team in teams if team['name'] == name]
    if len(teamFound) > 0:
        return jsonify({"team": teamFound[0]})
    return jsonify({"team" : 'None'})    


if __name__ == "__main__":
    app.run(port = 8080)
 

