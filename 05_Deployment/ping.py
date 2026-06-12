
# we use flask to turn the ping function into a web service
from flask  import Flask

# Create flask app
app = Flask('ping')

# adding decorators to add extra functionalities to our function
@app.route('/ping', methods =['GET']) # route is (the address where the function will live, the method we will use to access this route)
def ping():
    return "pong"

if __name__ == "__main__":
    app.run(debug= True, host = '0.0.0.0', port = 9696 )