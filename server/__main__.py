from server.chat_server import ChatServer

# Строка [::] означает, что мы разрешаем подключение с любого хоста (любого IP и Hostname).
# Можно явно написать localhost или 127.0.0.1, тогда будет работать только на одном компьютере.
chat_server = ChatServer(5000, '[::]')
chat_server.serve()
