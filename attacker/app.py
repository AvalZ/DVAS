from flask import Flask, render_template, request
import json

class attackerFlask(Flask):
    def process_response(self, response):
        try:
            with open("attacker.json", "r") as f:
                attacker = json.loads(f.read())
        except:
            attacker = {}

        if request.path != '/admin':
            if 'header' in attacker:
                if attacker['header']:
                    for header in  attacker['header'].split('\n'):
                        h = header.split(':', 1)
                        if len(h) > 1:
                            response.headers[h[0]] = h[1].strip('\r')

        return(response)

app = attackerFlask(__name__)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        code = request.values.get('code')
        msg = request.values.get('msg')
        header = request.values.get('header')
        body = request.values.get('body')
        robots = request.values.get('robots')
        attacker = { 'header': header, 'body': body, 'robots': robots, 'code': code, 'message': msg }
        with open("attacker.json", "w") as f:
            f.write(json.dumps(attacker))
        f.close()
    else:
        try:
            with open("attacker.json", "r") as f:
                attacker = json.loads(f.read())
        except:
            attacker = {}

    # print(attacker)
    return render_template('admin.html', attacker=attacker)

@app.route('/robots.txt')
def robots():
    try:
        with open("attacker.json", "r") as f:
            attacker = json.loads(f.read())
    except:
        attacker = {}

    robots = "Disallow: all"
    if 'robots' in attacker:
        robots = attacker['robots']

    t = render_template('robots.txt', robots=robots)

    return t, 200, {'Content-Type': 'text/plain'}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    body = "configure attacker using <a href='/admin'>admin</a> page"
    code = "200"
    message = "I gave too many answers"

    try:
        with open("attacker.json", "r") as f:
            attacker = json.loads(f.read())
    except:
        attacker = {}

    if 'body' in attacker:
        body = attacker['body']

    if 'code' in attacker:
        if attacker['code']:
            code = attacker['code']

    if 'message' in attacker:
        if attacker['message']:
            message = attacker['message']

    t = render_template('page.html', body=body)
    return t, "{} {}".format(code, message)

if __name__ == '__main__':
    app.run()