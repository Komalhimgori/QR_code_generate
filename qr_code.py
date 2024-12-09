import qrcode
def generate_qr_code(data, filename):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
 # Add data to the QR code
    qr.add_data("https://www.youtube.com/")
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")
     # Save the image to a file
    img.save(filename)

# Example usage
data = "(https://www.youtube.com/)"
filename = "qr_code.png"
generate_qr_code(data, filename)

    
    