import socketio
#from index import PiServer

sio = socketio.AsyncServer(
    async_mode="asgi", cors_allowed_origins="http://localhost:3000"
)

#sio.register_namespace("/pi")

app = socketio.ASGIApp(sio)

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
    if data == "start":
        await sio.emit('starting pod', "Stage 3: Pod is starting", to=sid)

@sio.event
async def stop(sid, data):
    if data == "stop":
        await sio.emit('stopping pod', "Stage 5: Pod is stopping", to=sid)

@sio.event
async def fstop(sid, data):
    if data == "fstop":
        await sio.emit('fstopping pod', "FORCE STOPPING POD", to=sid)