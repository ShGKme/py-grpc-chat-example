from client.chat_client import ChatClient
from client.console_chat import ConsoleChat

console_chat = ConsoleChat(ChatClient(5000, '127.0.0.1'))
console_chat.start()
