# imports
import os
import qrcode
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

WEB = 'www.godigital.menu'

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
    image = qr.make_image(
        fill_color="black", 
        back_color="white")

    # Save image
    image.save(image_filename)


def create_PDF(document_name, document_title, image_filename):
    """ 
    Create PDF with QR Code 
    https://realpython.com/creating-modifying-pdf/#creating-a-pdf-file-from-scratch
    https://www.reportlab.com/docs/reportlab-userguide.pdf
    """

    # Create document 
    pdf = canvas.Canvas(document_name, pagesize=A4)
    width, height = A4
    pdf.setTitle(document_title)

    # Draw QRs
    pdf.drawInlineImage(image_filename, 0, 0, height / 3, height / 3)
    pdf.drawInlineImage(image_filename, height / 2.75, 0, height / 3, height / 3)
    pdf.drawInlineImage(image_filename, 0, height / 3, height / 3, height / 3)
    pdf.drawInlineImage(image_filename, height / 2.75, height / 3, height / 3, height / 3)
    pdf.drawInlineImage(image_filename, 0, height * 2 / 3, height / 3, height / 3)
    pdf.drawInlineImage(image_filename, height / 2.75, height * 2 / 3, height / 3, height / 3)

    # Draw text
    # Fonts
    # print('Available fonts: {}'.format(pdf.getAvailableFonts()))
    # Set font
    pdf.setFont('Helvetica-Bold', 18)
    # Draw blue text
    pdf.setFillColor(colors.blue)
    # Middle ones
    pdf.drawCentredString(height / 1.9, width / 2, WEB)
    pdf.drawCentredString(height / 6.2, width / 2, WEB)

    # Draw Line
    pdf.setDash(6, 3)
    pdf.line(0, height / 3, width, height / 3) # horizontal
    pdf.line(0, height * 2 / 3, width, height * 2 / 3) # horizontal
    pdf.line(width / 2, 0, width / 2, height) # vertical

    # Save PDF!
    pdf.save()
