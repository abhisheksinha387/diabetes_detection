import sys

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = self._error_message_detail(error_message, error_detail)

    def _error_message_detail(self, error, error_detail):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error occurred in script: [{file_name}] at line: [{line_number}] - {error}"

    def __str__(self):
        return self.error_message