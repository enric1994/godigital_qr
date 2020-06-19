# imports
import os
import io
import sys
import qrcode
from flask import Flask, jsonify, request

# APP
app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is my secret key!'


# Static path
STATIC_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"))
OUTPUT_PATH = "/data/outputs/"


@app.route('/qr', methods=['GET', 'POST'])
def generate_qr():
    """ Generate Menu from CSV """

    try:

        # Read Request Data
        restaurant_name = request.headers['restaurant_name']
        url = request.headers['url']

        # Make QR
        image = qrcode.make(url)

        # Save image
        filename = os.path.join(OUTPUT_PATH, 'qr.png')
        image.save(filename)

        # Hurray!
        return jsonify(success=True)

    except Exception as e:

        print('#' * 100)
        print('Exception', e)
        print('#' * 100)

        # Fail!
        return jsonify(success=False)


# If run in localhost
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
