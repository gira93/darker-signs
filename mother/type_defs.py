from typing import TypedDict

Email = TypedDict("Email", {"from": str, "subject": str, "content": str})
File = tuple[str, str]  # Filename, file content
ChatMessage = TypedDict("ChatMessage", {"op": str, "content": str})
DbEntry = TypedDict("DbEntry", {"title": str, "content": str})
ShopItem = tuple[str, str, int]  # Item name, desc, price


class ServerConfig(TypedDict):
    id: str
    name: str
    font: str | None
    banner: str
    writable: bool
    authentication: list[tuple[str, str]] | None
    proxy: str | None
    crashed: bool
    hack_tool: str | None
    defense_tool: str | None


class WebServerConfig(ServerConfig):
    contents: list[DbEntry]


class FileServerConfig(ServerConfig):
    contents: dict[str, list[File]]  # Username, file list


class MailServerConfig(ServerConfig):
    contents: dict[str, list[Email]]  # Username, file list


class ChatServerConfig(ServerConfig):
    contents: list[ChatMessage]


class DbServerConfig(ServerConfig):
    contents: list[DbEntry]


class CommerceServerConfig(ServerConfig):
    contents: list[ShopItem]
