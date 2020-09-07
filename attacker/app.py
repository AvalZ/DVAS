from flask import Flask, render_template, request
import json, base64

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

app = attackerFlask(__name__,
                    static_url_path='/assets',
                    static_folder='static',
                    template_folder='templates')


@app.route("/update", methods=['POST'])
def update():
    code = request.values.get('code')
    msg = request.values.get('msg')
    header = request.values.get('header')
    body = request.values.get('body')
    robots = request.values.get('robots')
    path = request.values.get('path')

    attacker = {'header': header, 'body': body, 'robots': robots, 'code': code, 'message': msg, 'path': path}

    if path[1:]:
        fname = base64.b64encode(path.encode('ascii')).decode('ascii') + ".json"
    else:
        fname = "attacker.json"

    with open(fname, "w") as f:
        f.write(json.dumps(attacker))
    f.close()

    return "{}"

@app.route('/admin', defaults={'path': ''})
@app.route('/admin/<path:path>', methods=['GET', 'POST'])
def admin(path):
    if path:
        fname = base64.b64encode(path.encode('ascii')).decode('ascii') + ".json"
    else:
        fname = None

    try:
        with open(fname, "r") as f:
            attacker = json.loads(f.read())
    except:
        try:
            with open("attacker.json", "r") as f:
                attacker = json.loads(f.read())
        except:
            attacker = { 'path': path }

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
    body = "configure the catch-all attacker using the <a href='/admin'>admin</a> URL or a single-path attacker specifing a <i>path</i> after the admin URL (e.g., the <a href='/admin/example.html'>example.html</a> page attacker)"
    code = "200"
    message = "OK"

    if path:
        fname = base64.b64encode(path.encode('ascii')).decode('ascii') + ".json"
    else:
        fname = None

    try:
        with open(fname, "r") as f:
            attacker = json.loads(f.read())
    except:
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
