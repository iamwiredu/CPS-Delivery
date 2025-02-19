# myapp/utils.py

import qrcode
from qrcode.constants import ERROR_CORRECT_L
from io import BytesIO
from django.core.files.base import ContentFile

def generate_qr_code_for_order(order_instance, data):
    """
    Generates a QR code from 'data' in memory and stores it 
    into 'order_instance.qr_code' (an ImageField).
    """

    # Create the QRCode object
    qr = qrcode.QRCode(
        version=1,  # size of the QR code
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image (PIL Image object)
    img = qr.make_image(fill_color='black', back_color='white')

    # Save to an in-memory buffer
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    file_png = buffer.getvalue()

    # Construct a Django-friendly ContentFile
    qr_file = ContentFile(file_png)

    # Generate a filename (e.g., 'order_<id>_qr.png')
    filename = f'order_{order_instance.pk}_qr.png'

    # Save to the model field (this will save the file to your MEDIA_ROOT + upload_to path)
    order_instance.qr_code.save(filename, qr_file, save=True)
