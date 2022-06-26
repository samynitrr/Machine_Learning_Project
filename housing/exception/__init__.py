import os
import sys

class HousingException(Exception):
    """
    Base exception class for housing.
    """
    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(error_message) # passing the error to the parent class
        self.error_message = HousingException.get_detailed_error_message(error_message=error_message, error_detail=error_detail)

    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys) -> str:

        """
        error_message: Exception object
        error_detail: object of sys module
        """

        _, _, exec_tb = error_detail.exc_info() # from the error details, get the traceback of the error. 
                                                # It returns tuples of (filename, line number, function name, text)

        exception_block_lin_no = exec_tb.tb_frame.f_lineno # get the line number of the exception block error
        try_block_line_no = exec_tb.tb_lineno # get the line number of the error in the try block
        file_name = exec_tb.tb_frame.f_code.co_filename # get the file name from the traceback
        function_name = exec_tb.tb_frame.f_code.co_name # get the function name from the traceback

        error_message = f"""
        Error occurred in script: [{file_name}] 
        at try block line number: [{try_block_line_no}] and exception block line number: [{exception_block_lin_no}] 
        in function : {function_name} 
        error message:\n{error_message}
        """

        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self)->str:
        return HousingException.__name__.str()

