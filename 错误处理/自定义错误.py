class MyException(Exception):
    def __init__(self, message: str, *, code) -> None:
        self.message = message
        self.code = code

    def __str__(self) -> str:
        if self.code is None:
            return self.message
        else:
            return f"{self.message}\n\nFor further information visit {self.code}"


if __name__ == "__main__":
    raise MyException("my exception", code=123)
