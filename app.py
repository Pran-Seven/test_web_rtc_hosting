from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room
import logging

app = Flask(__name__)
# app.secret_key = 'random secret key!'
# socketio = SocketIO(app, cors_allowed_origins="")
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")



@socketio.on('connect')
def connect(message):
    app.logger.info("connected")
    # username = message['username']
    # room = message['room']
    # join_room(room)
    # print('RoomEvent: {} has joined the room {}\n'.format(username, room))
    emit('ready',message)


@socketio.on('data')
def transfer_data(message):
    app.logger.info("sent")
    # username = message['username']
    # room = message['room']
    # data = message['data']
    # print('DataEvent: {} has sent the data:\n {}\n'.format(username, data))
    emit('data', message)


@socketio.on_error_default
def default_error_handler(e):
    app.logger.error("Ran into an error, need to resolve")
    # print("Error: {}".format(e))
    socketio.stop()


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5004)
