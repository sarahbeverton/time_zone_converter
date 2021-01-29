from flask import Flask
from flask_cors import CORS
from pytz import timezone
from datetime import datetime
import urllib.parse

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/")
def home():
    return "Time Zone Converter Flask API"


@app.route('/<path:new_timezone>', methods=['GET'])
def convert_time(new_timezone):
    converted_time = None
    current_time = datetime.now()
    tz_to_convert = timezone(urllib.parse.unquote(new_timezone))
    converted_time = current_time.astimezone(tz_to_convert)
    return converted_time.strftime("%m/%d/%Y %H:%M:%S %Z %z")


if __name__ == '__main__':
    app.run(debug=True)
