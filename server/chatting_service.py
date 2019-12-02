from queue import Queue
from time import sleep

import grpc

import server.grpc_out.chat_pb2 as chat_proto
import server.grpc_out.chat_pb2_grpc as chat_grpc


class ChattingService(chat_grpc.ChattingServicer):
    """
    Класс, который реализует описанный в Proto файле сервис
    """

    MESSAGE_STREAM_INTERVAL: 0.1

    def __init__(self):
        # История всех сообщений
        self._history = []
        self._is_working = True

    def MessageStream(self, request, context: grpc.ServicerContext):
        last_read = len(self._history) - 1
        # Бесконечно отправляем сообщения, пока соединение активно
        while context.is_active():
            # Отправляем все сообщения из очереди неотправленных
            while last_read < len(self._history) - 1:
                last_read += 1
                message = self._history[last_read]
                # yield - это как бесконечный return.
                # Функция будет возвращать значения снова и снова, когда вызывается yield.
                # А с другой стороны мы сможем их получать просто циклом for in (вспоминаем итераторы в Python)
                # P.S. см. генераторы в Python
                yield message
            # Добавим маленький sleep, чтобы снизить нагрузку на сервер постоянными проверками новых сообщений
            sleep(0.1)

    def SendMessage(self, message: chat_proto.Message, context):
        print(f'[{message.author}] {message.text}')
        # self._sending_messages_queue.put(message)
        self._history.append(message)
        return chat_proto.Nothing()
