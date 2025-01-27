import qrcode
from PIL import Image
from os import getcwd


def qrcode_create(data,fill_color="black",back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img1 = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img1


def create_colored_qr_code(data, logo_path, fill_color_palette, back_color_palette, aggiungi_immagine):
    img = qrcode_create(data,fill_color_palette,back_color_palette)
    img = img.convert('RGB')
    if aggiungi_immagine==True:
        logo = Image.open(logo_path)
        basewidth = 50
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize))

        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos)
    return img


#------------------------------------------------------------------------------------------
name_qrcode = 'qrcode_generated1.png'   # Name of the QR-Code
data = 'QR-Code Generator'              # Text or URL to visualize in the QR-Code

logo_path = 'image.png'                 # *.png image to add in the QR-Code
img_view = False                        # Add image to the QR-Code


folder_or_file = ""
fill_color_qrcode = (255, 0, 0)         # can use the text 'red'
back_color_qrcode = (255, 255, 255)     # can use the text 'white'


qrcode_imgdata=create_colored_qr_code(data, logo_path, fill_color_qrcode, back_color_qrcode, img_view)
qrcode_imgdata.save("".join([getcwd(),"\\", name_qrcode]))



