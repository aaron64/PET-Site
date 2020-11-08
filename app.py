from flask import Flask
from flask import render_template, json

import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output

app =Flask(__name__)

@app.route('/')
def index():
	wifi_networks_cmd = ['ubus', 'call', 'onion', 'wifi-scan', '{"device":"ra0"}']
	session = subprocess.run(wifi_networks_cmd, stdout=subprocess.PIPE)
	wifi_networks = json.loads(session.stdout.decode('utf-8'))
	print(wifi_networks)
	return render_template("index.html", networks=wifi_networks['results'])
