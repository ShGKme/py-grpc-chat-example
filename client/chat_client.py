import threading
import grpc

import client.grpc_out.chat_pb2 as chat_proto
import client.grpc_out.chat_pb2_grpc as chat_grpc


class ChatClient:
    """
    Класс - клиент чата.
    В gRPC довольно легко работать с сервером, но мы сделаем прослойку, чтобы было совсем просто.
    """

    def __init__(self, port=5000, host='127.0.0.1'):
        self._port = port
        self._host = host
        self._on_message_receive = None
        # Создаём канал подключения к сервису
        self._channel = grpc.insecure_channel(f'{self._host}:{self._port}')
        # Создаём сервис-клиент по этому каналу
        self._chat_service = chat_grpc.ChattingStub(self._channel)

    def start_listen_messages(self, message_received):
        # Функция, которую будем вызывать, когда придёт сообщение
        self._on_message_receive = message_received
        # Создаём отдельный поток, в котором читаем приходящий стим сообщений от сервера
        threading.Thread(target=self._listen_for_messages, daemon=True).start()

    def _listen_for_messages(self):
        # Цикл будет ждать, пока придут сообщения, обрабатывать все пришедшие и ждать дальше
        for message in self._chat_service.MessageStream(chat_proto.Empty()):
            self._on_message_receive(message)

    def send_message(self, username, text):
        message = chat_proto.Message()
        message.author = username
        message.text = text
        self._chat_service.SendMessage(message)

    def close(self):
        self._channel.close()
