class Data:
    def __init__(self, data: str, ip: int):
        self._data = data
        self._ip = ip

    @property
    def data(self):
        return self._data

    @property
    def ip(self):
        return self._ip

    def __repr__(self):
        return f"Data(data={self._data}, ip={self._ip})"


class Server:
    _next_ip = 1

    def __init__(self):
        self._ip = self._next_ip
        self.__class__._next_ip += 1
        self._buffer = []
        self._router = None

    @property
    def ip(self) -> int:
        return self._ip

    def set_router(self, router) -> None:
        self._router = router

    def put_data_in_buffer(self, data: Data) -> None:
        self._buffer.append(data)

    def send_data(self, data: Data):
        if self._router:
            self._router.put_data_in_buffer(data)
        else:
            raise Warning("Невозможно отправить данные. Сервер не подключен к Роутеру!")

    def get_data(self) -> list[Data]:
        lst = self._buffer
        self._buffer = []
        return lst


class Router:
    def __init__(self):
        self._servers: dict[int:Server] = {}
        self._buffer = []

    def link(self, server: Server) -> None:
        server.set_router(self)
        self._servers[server.ip] = server

    def unlink(self, server: Server) -> None:
        if server.ip in self._servers:
            server.set_router(None)
            del self._servers[server.ip]

    def send_data(self) -> None:
        for data in self._buffer:
            if data.ip in self._servers:
                self._servers[data.ip].put_data_in_buffer(data)
            else:
                raise Warning(f"Данные не были отправлены. Сервер с IP = {data.ip} не подключен к этому роутеру!")
        self._buffer = []

    def put_data_in_buffer(self, data: Data) -> None:
        self._buffer.append(data)
