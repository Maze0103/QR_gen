from flask import Flask, render_template, request, Response
import qrcode
import io
import traceback

app = Flask(__name__)

def generate_qr(url):
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        return img_io
    except Exception as e:
        print(f"Error generating QR code: {e}")
        traceback.print_exc()
        return None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            return "Error: URL is required", 400
        qr_image = generate_qr(url)
        if qr_image:
            return Response(qr_image.getvalue(), mimetype='image/png')
        else:
            return "Error generating QR code", 500
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5051)


