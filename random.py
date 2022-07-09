# from posixpath import split
# from sklearn.feature_selection import SelectorMixin
# from yaml.error import MarkedYAMLError


# data [60:20:20]

# 100  rows of data

# data[80]  --> EDA / FE / Data Transformation

# model Selecto
# train test split(

# )




# train[60] validation -  [20] - validation - hyperparamter tuning -  model.pkl
# final model.pkl for deployment

# 80% - 100%

# 80 rows of data
# cv - 4

# 20| 20 |20 | #20
# 20|20| #20 | 20



# data[20] - test





# x = 10
# y = 20

# z = x+y

# print(z)

# print(f"sum of {x} and {y} is {z}")

# def sum_two_int(x,y):
#     return x+y

# sum_two_int()


# def sum_two_int_context(x:int, y:int)-> int:
#     return x,y

# _,b = sum_two_int_context()

# #Process-1
# x = int(input())

# #Check if Process-1 is ok or not
# if x == "":
#     my_inpt_ok = False
# else:
#     my_inpt_ok = True


# #Process-2
# if x=="": #Process-1
#     sum_two_int() #Process-2

# else:
#     pass

# d = {"a":1, "b":2}

# d["a"] --> 1



# project hld           root project - housing

# config ->  {constant -> entity(config(input)/artifact(output)) -> configuration -> data_ingestion -> pipeline}







import sys

class DemoError(Exception):
    def __init__(self, error_message:Exception, error_details:sys):
        super().__init__(error_message)
        self.error_message = self.custom_error_message(e_message=error_message, details=error_details)


    def custom_error_message(self, e_message:Exception, details:sys):

        _,_,exec_tb = details.exc_info()

        # exception_block_lin_no = exec_tb.tb_frame.f_lineno # get the line number of the exception block error

        try_block_line_no = exec_tb.tb_lineno # get the line number of the error in the try block
        file_name = exec_tb.tb_frame.f_code.co_filename # get the file name from the traceback

        function_name = exec_tb.tb_frame.f_code.co_name # get the function name from the traceback

        error_message = f"""
        Error occurred in script: [{file_name}] 
        at try block line number: [{try_block_line_no}]  
        in function : {function_name} 
        error message:\n{e_message}
        """

        return error_message

    def __str__(self):
        return self.error_message

try:
    a = 10
    b = 0
    c = a/b
    print(c)
except Exception as e:
    raise DemoError(e, sys) from e



















