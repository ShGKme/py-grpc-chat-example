# Простой консольный чат на Python и gRPC

Пример простейшего консольного чата на gRPC и Python.

## Требования

- Python 3.7+

## Установка зависимостей
```shell script
pip install -r requirements.txt
```

## Генерация Python модулей по proto файлам
```shell script
compile_proto.bat
```

## Запуск

#### Запуск из терминала

##### Запуск сервера
```shell script
python -m server
```

##### Запуск клиента
```shell script
python -m client
```

#### Запуск из PyCharm 

В PyCharm доступны `Start Server` и `Start Client` конфгурации запуска (можно запускать множество клиентов параллельно). 

## Примечания

### Генерация Python модулей по proto файлам

Для компиляции Proto файлов в Python модули используется модуль `grpc_tools.protoc`.  

Но для компиляции файлов требуется использовать скрипт `compile_proto.bat`. В целом он просто запускает `grpc_tools.protoc`, но до этого создаёт структуру папок, аналогичную структуре пакетов в python. 

Это требуется для того, чтобы корректно работал импорт в скомпилированных модулях.

Описание проблемы: https://github.com/protocolbuffers/protobuf/issues/1491  
Решение из: https://github.com/grpc/grpc/issues/9575#issuecomment-293934506  

### О генерируемых файлах

Генерируется два файла.
- Оканчивающийся на `_pb2.py`: модуль с описанием типов и сервиса;
- Оканчивающийся на `_pb2_grpc.py`: модуль, реализующий gRPC.

### Другие примечания

pb2 - сокращение от ProtoBuf v.2. 

## Полезные ссылки

- gRPC: https://grpc.io/docs/guides/concepts/
- gRPC туториал для Python: https://grpc.io/docs/tutorials/basic/python/
- Примеры на Python: https://github.com/grpc/grpc/tree/master/examples/python
- Полный API библиотеки grpcio для Python: https://grpc.github.io/grpc/python/
- GUI приложение для тестирования gRPC сервера: https://github.com/uw-labs/bloomrpc

## TODO

1. Добавить простую авторизацию (метод "регистрации");
2. Добавить в чат сообщения вида "Клиент подключился", "Клиент отключился".
