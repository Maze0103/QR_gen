import qrcode

def url_to_qr(url,filename="qr_code.png"):
    # Create qr code instance
    qr = qrcode.QRCode(version=1, box_size=10,border=5)
    
    # Add data (URL) to the QR Code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR Code
    img = qr.make_image(fill_color="black",back_color="white")
    
    # Save the IMAGE
    img.save(filename)
    print(f"QR Code saved as (filename)")
    
if __name__ == "__main__":
    url = "https://colorhunt.co/"
    url_to_qr(url)
