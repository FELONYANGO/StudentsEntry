from flask import Flask,jsonify
from flask_cors import CORS

# instantate the app

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app,resources={r'/*':{'origins':'*'}})

# rauting to the root page
@app.route('/',methods=['GET'])
def home():
    """
    the home landing page method
    """
    return jsonify('students')


# run the app
if __name__ == '__main__':
    app.run(debug=True)

