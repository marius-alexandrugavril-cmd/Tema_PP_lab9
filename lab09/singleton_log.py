import threading

class Logger:
    _instance = None
    _lock = threading.Lock()  

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._logs = []
        return cls._instance

    def log(self, message: str) -> None:
        self._logs.append(message)

    def get_logs(self) -> list[str]:
        return self._logs

    def clear(self) -> None:
        self._logs.clear()