
DEV_ERROR_DOCS_URL = "https://www.baidu.com/"
class PydanticErrorMixin:
    """A mixin class for common functionality shared by all Pydantic-specific errors.

    Attributes:
        message: A message describing the error.
        code: An optional error code from PydanticErrorCodes enum.
    """

    def __init__(self, message: str, *, code) -> None:
        self.message = message
        self.code = code

    def __str__(self) -> str:
        if self.code is None:
            return self.message
        else:
            return f'{self.message}\n\nFor further information visit {DEV_ERROR_DOCS_URL}{self.code}'


# 继承exception 才能raise抛出
class PydanticImportError(PydanticErrorMixin, Exception):
    """An error raised when an import fails due to module changes between V1 and V2.

    Attributes:
        message: Description of the error.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message, code='import-error')



if __name__ == '__main__':
    raise PydanticImportError("test")