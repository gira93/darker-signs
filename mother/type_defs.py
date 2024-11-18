from typing import TypedDict
from enum import Enum

Email = TypedDict("Email", {"from": str, "subject": str, "content": str})
File = tuple[str, str]  # Filename, file content
ChatMessage = TypedDict("ChatMessage", {"op": str, "content": str})
DbEntry = TypedDict("DbEntry", {"title": str, "content": str})
ShopItem = tuple[str, str, int]  # Item name, desc, price


class RequirementType(Enum):
    FILE_PRESENT = 1
    FILE_NOT_PRESENT = 2
    FILE_DOWNLOADED = 3
    SERVER_CRASHED = 4
    EMAIL_NOT_PRESENT = 5


AssignmentRequirement = tuple[
    RequirementType, str
]  # RequirementType, subject (file name ...)

Assignment = TypedDict(
    "Assignment",
    {
        "id": str,
        "title": str,
        "description": str,
        "emails": list[Email],
        "exp_needed": int,
        "credit_reward": int,
        "exp_reward": int,
        "requirements": dict[str, AssignmentRequirement],  # Key: server config id
    },
)


class ServerConfig(TypedDict):
    id: str
    name: str
    font: str | None
    banner: str
    writable: bool
    authentication: list[tuple[str, str]] | None  # username, password
    proxy: str | None
    crashed: bool
    hack_tool: (
        str | None
    )  # roobreaker, rootbreaker2, rootbreaker3, wavehacker, physicalkey
    defense_tool: str | None  # backmirror, backmirror2, backmirror3


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


class AssignmentServerConfig(ServerConfig):
    contents: list[Assignment]
