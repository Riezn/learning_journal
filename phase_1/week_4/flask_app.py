from flask import Flask, jsonify, request

app = Flask(__name__) #__name__ = nama file

profile = {'nama': 'Tes',
           'hobby': 'Membaca'}

@app.route("/profile")
def my_profile():
    return jsonify(profile)

@app.route("/modify", methods=['POST'])
def modify_data():
    global profile
    data = request.json
    profile['nama'] = data['nama']


app.run(debug=True)