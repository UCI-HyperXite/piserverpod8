# app.py
import socketio
from utils import get_sid_save, get_current_state, set_current_state

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
async def start(sid, data):
    if data == 2:
        set_current_state(2)
        await sio.emit('starting pod', "Stage 2: Pod is starting", to=sid)


@sio.event
async def stop(sid, data):
    if data == 4:
        set_current_state(4)
        await sio.emit('stopping pod', "Stage 4: Pod is stoppingu78", to=sid)

@sio.event
async def load(sid, data):
    if data == 5:
        set_current_state(5)
        await sio.emit('stopping pod', "Stage 5: Pod is loading", to=sid)
@sio.event
async def sum(sid, data):
    result = data['numbers'][0] + data['numbers'][1]
    await sio.emit('sum_result', {'result': result}, to=sid)
