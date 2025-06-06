import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    This function takes an error and its details and returns a formatted string with the error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"

    return error_message


class CustomException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class.
    It takes an error and its details and formats them using the error_message_detail function.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message   
    
# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.info("Division by zero error")
#         raise CustomException(e, sys) from e