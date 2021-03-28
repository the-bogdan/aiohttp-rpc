class ExecutionException(Exception):
    def __init__(self, error_type: str, message: str, http_code: int = 400):
        super().__init__(error_type)

        self.message = message
        self.http_code = http_code
        self.error_type = error_type
