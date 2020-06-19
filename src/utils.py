# imports
import os
import qrcode
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

def create_QR(url, image_filename):
    """ 
    Create QR Code 
    https://github.com/lincolnloop/python-qrcode
    """

    # Make QR
    # image = qrcode.make(url)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    image = qr.make_image(fill_color="black", back_color="white")

    # Save image
    image.save(image_filename)


def create_PDF(document_name, document_title, image_filename):
    """ Create PDF with QR Code """

    # Create document 
    pdf = canvas.Canvas(document_name, pagesize=A4)
    pdf.setTitle(document_title)

    # Draw image
    pdf.drawInlineImage(image_filename, 0, 0, 275, 275)
    pdf.drawInlineImage(image_filename, 280, 0, 275, 275)
    pdf.drawInlineImage(image_filename, 0, 280, 275, 275)
    pdf.drawInlineImage(image_filename, 280, 280, 275, 275)
    pdf.drawInlineImage(image_filename, 0, 560, 275, 275)
    pdf.drawInlineImage(image_filename, 280, 560, 275, 275)

    # Save PDF!
    pdf.save()
