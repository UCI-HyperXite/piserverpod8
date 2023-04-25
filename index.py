import socketio


class PiServer(socketio.AsyncNamespace):
    async def on_connect(self, sid, environ):
        print(sid, environ, "connect")
        self.emit("outp", {'recived': 'yes'})
        pass

    def on_disconnect(self, sid):
        print(sid, "disconnect")
        pass

    async def output_data(self, sid, data):
        print(sid)
        data = {'recived': 'yes'}
        await self.emit("outp", {'recived': 'yes'})
'p'