# Endpoints
#'/api/v1/details'
#'/api/v1/healthz'

from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World from root'

@app.route('/api/v1/details')
def details():
  # return '<h1>Hello World (details)</h1>'
  return jsonify({
    'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
    'hostname': socket.gethostname(),
    'message': 'You are great in Python and Github Action and Kubernetes and DevOps and GitOps'
  })

@app.route('/api/v1/healthz')
def health():
  return jsonify({'status':'up'})

if __name__ == '__main__':
  # Need to set the host for reaching the docker container from host
  app.run(host="0.0.0.0")
