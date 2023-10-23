import qrcode
from datetime import datetime

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Get the current time as a string
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Combine the creation time with the file extension
    filename = f"qrcode_{current_time}.png"

    img.save(filename)
    return filename

# Prompt the user to enter the text
data = input("Enter the text for the QR code: ")

# Generate the QR code based on the entered text
output_filename = generate_qr_code(data)
print("QR code has been created in the file", output_filename)
