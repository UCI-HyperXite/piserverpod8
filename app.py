import socketio
import uvicorn
#from index import PiServer
 
   
sio = socketio.AsyncServer(
    async_mode="asgi", cors_allowed_origins="http://localhost:3000"
)

#sio.register_namespace("/pi")

app = socketio.ASGIApp(sio)

buttonSignal = 0;
old_bms = 0;

@sio.event
async def connect(sid, environ):
    print(sid, 'connected')


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

def state1(msg):
    @sio.event
    async def state1(sid):
        sio.emit('Loading State', msg, to=sid)


