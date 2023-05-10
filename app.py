# app.py
import socketio
from utils import get_sid_save, sid_save

sio = socketio.AsyncServer(
    async_mode="asgi", cors_allowed_origins="http://localhost:3000"
)

app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, environ):
    print(sid, 'connected')
    global sid_save 
    sid_save = sid

@sio.event
async def disconnect(sid):
    print(sid, 'disconnected')


@sio.event
async def sum(sid, data):
    result = data['numbers'][0] + data['numbers'][1]
    await sio.emit('sum_result', {'result': result}, to=sid)
