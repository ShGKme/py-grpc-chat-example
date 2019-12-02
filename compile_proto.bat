@echo off

echo [1/3] Copying files...
mkdir protos\client\grpc_out
mkdir protos\server\grpc_out
copy protos\chat.proto protos\client\grpc_out
copy protos\chat.proto protos\server\grpc_out

echo [2/3] Generating proto...
python -m grpc_tools.protoc --proto_path=./protos/ --python_out=. --grpc_python_out=. server/grpc_out/chat.proto
python -m grpc_tools.protoc --proto_path=./protos/ --python_out=. --grpc_python_out=. client/grpc_out/chat.proto

echo [3/3] Removing files...
rmdir protos\client /s /q
rmdir protos\server /s /q

echo Competed!
