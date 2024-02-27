import qrcode

def generate_qr_code(url, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if _name_ == "_main_":
    url = input("Enter the URL to generate QR code: ")
    file_name = input("Enter the filename to save the QR code as (with extension, e.g., qr_code.png): ")
    generate_qr_code(url, file_name)
    print(f"QR code generated and saved as {file_name}")
