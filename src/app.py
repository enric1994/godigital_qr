# imports
import os
import io
import sys
from utils import create_QR, create_PDF_medium, create_PDF_large, create_PDF_small
from flask import Flask, jsonify, request

# APP
app = Flask(__name__)

# Static path
STATIC_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"))
OUTPUT_PATH = "/output/"


@app.route('/qr', methods=['GET', 'POST'])
def generate_qr():
    """ Generate QR from URL """

    try:

        # Read Request Data
        output_id = request.headers['output_id']
        restaurant_name = 'GoDigital Menu'
        url = request.headers['url']

        # Create QR Code
        QR_filename = os.path.join(OUTPUT_PATH, 'QR_image_{}.png'.format(output_id))
        create_QR(url, QR_filename)

        # Create PDF
        small_name = os.path.join(OUTPUT_PATH, 'QR_small_{}.pdf'.format(output_id))
        medium_name = os.path.join(OUTPUT_PATH, 'QR_medium_{}.pdf'.format(output_id))
        large_name = os.path.join(OUTPUT_PATH, 'QR_large_{}.pdf'.format(output_id))
        document_title = restaurant_name
        create_PDF_small(small_name, document_title, QR_filename)
        create_PDF_medium(medium_name, document_title, QR_filename)
        create_PDF_large(large_name, document_title, QR_filename)

        # Hurray!
        return '200'

    except Exception as e:

        print('#' * 100)
        print('Exception', e)
        print('#' * 100)

        # Fail!
        return '500'


# If run in localhost
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
