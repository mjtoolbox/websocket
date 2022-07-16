from flask import Flask, render_template, request, redirect, url_for, flash
import json
import random
from datetime import date
from datetime import datetime
from flask_socketio import SocketIO
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mypass'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    user = 'user' + str(random.randrange(0, 9))
    return render_template('session.html', name=user)


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('servertopic')
def handle_chat_event(json, methods=['GET', 'POST']):
    print('Server side received chat msg: ' + str(json))
    socketio.emit('clienttopic', json, callback=messageReceived)


if __name__ == "__main__":
    socketio.run(app, debug=True)
