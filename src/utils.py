# imports
import os
import qrcode
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors


# Static path
STATIC_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"))

# Parameters
SCISSORS_PATH = os.path.join(STATIC_PATH, 'img', 'scissors.png')
HEADER = 'Scan the QR code to see our menu'
FOOTER = 'Powered by godigital.menu'



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


def create_PDF_multi8(document_name, document_title, image_filename):
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


    # Set font
    pdf.setFont('Helvetica-Bold', 16)

    # Text color
    pdf.setFillColor(colors.black)

    # Headers
    # Top ones
    pdf.drawCentredString(height / 1.9, width / 0.73, HEADER)
    pdf.drawCentredString(height / 5.5, width / 0.73, HEADER)

    # Middle ones
    pdf.drawCentredString(height / 1.9, width / 1.12, HEADER)
    pdf.drawCentredString(height / 5.5, width / 1.12, HEADER)
    
    # Bottom ones
    pdf.drawCentredString(height / 1.9, width / 2.35, HEADER)
    pdf.drawCentredString(height / 5.5, width / 2.35, HEADER)

    # Set font
    pdf.setFont('Helvetica-Bold', 10)

    # Text color
    pdf.setFillColor(colors.grey)

    # Footers
    # Top ones
    pdf.drawCentredString(height / 1.9, width / 1.025, FOOTER)
    pdf.drawCentredString(height / 6.2, width / 1.025, FOOTER)

    # Middle ones
    pdf.drawCentredString(height / 1.9, width / 2, FOOTER)
    pdf.drawCentredString(height / 6.2, width / 2, FOOTER)

    # Bottom ones
    pdf.drawCentredString(height / 1.9, width / 32, FOOTER)
    pdf.drawCentredString(height / 6.2, width / 32, FOOTER)

    # Draw Lines
    pdf.setDash(6, 3)
    pdf.line(0, height / 3, width, height / 3) # horizontal
    pdf.line(0, height * 2 / 3, width, height * 2 / 3) # horizontal
    pdf.line(width / 2, 0, width / 2, height) # vertical

    # Draw scissors on the horizontal lines
    SCISSORS_SIZE = 20
    pdf.drawImage(SCISSORS_PATH, 0, height / 3 - SCISSORS_SIZE / 1.5, SCISSORS_SIZE, SCISSORS_SIZE, mask='auto')
    pdf.drawImage(SCISSORS_PATH, 0, height * 2 / 3 - SCISSORS_SIZE / 1.5, SCISSORS_SIZE, SCISSORS_SIZE, mask='auto')

    # Save PDF!
    pdf.save()

def create_PDF_large(document_name, document_title, image_filename):
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
    pdf.drawInlineImage(image_filename, height/10, width/2, height / 2, height / 2)

    # Set font
    pdf.setFont('Helvetica-Bold', 32)

    # Text color
    pdf.setFillColor(colors.black)

    # Header
    pdf.drawCentredString(height / 2.9, width / 0.8, HEADER)
    
    # Set font
    pdf.setFont('Helvetica-Bold', 16)

    # Text color
    pdf.setFillColor(colors.grey)

    # Footers
    pdf.drawCentredString(height / 2.7, width / 25, FOOTER)

    # Save PDF!
    pdf.save()
