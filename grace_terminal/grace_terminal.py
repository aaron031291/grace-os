import asyncio
import websockets
import json
import uuid

async def handler(websocket, path):
    print("Client connected")
    try:
        async for message in websocket:
            data = json.loads(message)
            response = {
                "type": "grace_response",
                "message": f"Grace received: {data.get('content', '')}",
                "trace_id": str(uuid.uuid4())
            }
            await websocket.send(json.dumps(response))
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("Grace Terminal running on ws://0.0.0.0:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
