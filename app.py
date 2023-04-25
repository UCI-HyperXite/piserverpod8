import socketio
from index import PiServer

sio = socketio.AsyncServer(
    async_mode="asgi", cors_allowed_origins="http://localhost:3000"
)

sio.register_namespace(PiServer("/pi"))

app = socketio.ASGIApp(sio)

