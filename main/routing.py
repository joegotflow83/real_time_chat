from . import consumers


channel_routing = {
    'websocket.connect': consumers.ws_connect,
    'websocket.retrieve': consumers.ws_recieve,
    'websocket.disconnect': consumers.ws_disconnect,
}
