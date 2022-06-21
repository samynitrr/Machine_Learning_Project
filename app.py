from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

app =Flask(__name__);



@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are purposefully raising an exception to test our custom exception package")
    except Exception as e:
        housing =  HousingException(e, sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return "CI CD Pipeline has been established and deployed successfully"



if __name__ == "__main__":
    app.run(debug=True, port= 9000 )