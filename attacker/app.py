from flask import Flask, render_template, request
import json

SERVER_NAME = 'Custom Flask Web Server v0.1.0'

class attackerFlask(Flask):
    def process_response(self, response):
        try:
            with open("attacker.json", "r") as f:
                attacker = json.loads(f.read())
        except:
            attacker = {}

        if 'header' in attacker:
            headers = [line.rstrip('\n') for line in attacker['header']]

        print(headers)
        return(response)

app = attackerFlask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        header = request.values.get('header')
        body = request.values.get('body')
        robots = request.values.get('robots')
        attacker = { 'header': header, 'body': body, 'robots': robots }
        with open("attacker.json", "w") as f:
            f.write(json.dumps(attacker))
        f.close()
    else:
        try:
            with open("attacker.json", "r") as f:
                attacker = json.loads(f.read())
        except:
            attacker = {}

    print(attacker)
    return render_template('admin.html', attacker=attacker)

if __name__ == '__main__':
    app.run()
