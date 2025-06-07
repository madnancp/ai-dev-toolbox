from fastapi import WebSocket
from typing import Any


class WsConnectionManager:
    def __init__(self) -> None:
        self.connections: list[Any] = []

    @property
    def get_connections(self) -> list:
        return self.connections

    def add_connection(self, connection: WebSocket) -> None:
        self.connections.append(connection)

    async def send_message_to(self, connection: WebSocket, message: str) -> None:
        await connection.send_text(message)

    def remove_connection(self, connection: WebSocket) -> None:
        self.connections.remove(connection)

    async def broadcast(self, message: str) -> None:
        for con in self.connections:
            await con.send_text(message)
