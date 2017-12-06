from flask import Flask, jsonify
# import api_server
# from findARestaurant import findARestaurant
# import geocode

app = Flask(__name__)


@app.route('/')
def hello_world():
    # myVar = findARestaurant("Pizza", "Tokyo, Japan")
    myVar = "test"
    return myVar

@app.route('/_get_current_user')
def get_current_user():
    return jsonify(username=g.user.username, email=g.user.email, id=g.user.id)

if __name__ == '__main__':
    app.run()
