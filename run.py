from flask import Flask, render_template, jsonify, request
import json
import requests
app = Flask(__name__)

@app.route('/coolors.co')
def CoolorsCo():
	return render_template('coolors.co/main.html')

@app.route('/colorhunt.co')
def ColorhuntCo():
	return render_template('colorhunt.co/main.html')

@app.route('/api/coolors.co', methods=['POST'])
def CoolorsCoAPI():
	if request.method == 'POST':
		page = request.form.get('page')
		sort = request.form.get('sort')
		search = request.form.getlist('search[]')
		s = requests.Session()
		s.get('https://coolors.co')
		data = {'page': page, 'sort': sort, 'search': search, 'session_token': s.cookies.get_dict()['__Secure-PHPSESSID']}
		return requests.post('https://coolors.co/ajax/list_palettes', data=data, cookies=s.cookies.get_dict()).json()['data']

@app.route('/api/colorhunt.co', methods=['POST'])
def ColorhuntCoAPI():
	if request.method == 'POST':
		step = request.form.get('step')
		sort = request.form.get('sort')
		return requests.post('https://colorhunt.co/hunt.php', data = {'step': step, 'sort': sort}).content

if __name__ == "__main__":
    app.run(debug=True)