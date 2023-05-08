import socketio
import uvicorn
#from index import PiServer
 
   
sio = socketio.AsyncServer(
    async_mode="asgi", cors_allowed_origins="http://localhost:3000"
)

#sio.register_namespace("/pi")

app = socketio.ASGIApp(sio)

buttonSignal = 0;
sid_save = ""
@sio.event
async def connect(sid, environ):
    print(sid, 'connected')
    global sid_save 
    sid_save = sid

def get_sid_save():
    return sid_save

# export the get_sid_save function
__all__ = ['sio', 'get_sid_save']

@sio.event
async def disconnect(sid):
    print(sid, 'disconnected')


@sio.event
async def sum(sid, data):
    result = data['numbers'][0] + data['numbers'][1]
    await sio.emit('sum_result', {'result': result}, to=sid)


@sio.event
async def start(sid, data):
    if data == 2:
        buttonSignal = 0
        buttonSignal += data
        await sio.emit('starting pod', "Stage 2: Pod is starting", to=sid)

@sio.event
async def stop(sid, data):
    if data == 4:
        buttonSignal = 0
        buttonSignal += data
        await sio.emit('stopping pod', "Stage 4: Pod is stopping", to=sid)


