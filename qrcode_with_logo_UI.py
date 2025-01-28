import qrcode
from PIL import Image
import PySimpleGUI as sg
from base64 import b64encode
from io import BytesIO
from os import getcwd

# PyInstaller  -F --clean --onefile --windowed --icon=qrcode_icon.ico qrcode_with_logo_UI.py

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    rgb_int = int(hex_color, 16)
    blue = rgb_int & 0xFF
    green = (rgb_int >> 8) & 0xFF
    red = (rgb_int >> 16) & 0xFF

    return (red, green, blue)


def qrcode_create(data,fill_color="black",back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create QR-code
    # img1 = qr.make_image(fill_color="black", back_color="white")
    img1 = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img1


def create_colored_qr_code(data, logo_path, fill_color_palette, back_color_palette, aggiungi_immagine):
    img = qrcode_create(data,fill_color_palette,back_color_palette)
    img = img.convert('RGB')
    if aggiungi_immagine==True:
        try:
            logo = Image.open(logo_path)
            basewidth = 50
            wpercent = (basewidth/float(logo.size[0]))
            hsize = int((float(logo.size[1])*float(wpercent)))
            logo = logo.resize((basewidth, hsize))

            pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
            img.paste(logo, pos)
        except:
            sg.popup("If the checkbox is selected, choose an image", keep_on_top=True, icon = name_icon, title=title_project) 
    return img


#------------------------------------------------------------------------------------------
name_qrcode = 'qrcode_generated.png'
name_icon = b'iVBORw0KGgoAAAANSUhEUgAAAOwAAADqCAYAAAChiqkJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAQgSURBVHhe7dwxjttAEADBO///z7aDCwyYEChopdkmqxI70mnJbUwy0Pfvv76AhF8//wIBgoUQwUKIYCFEsBAiWAgRLIQIFkIECyGChZCnVhO/v79//se/zj7Cs89v6vNWc1+OvfI+TFgIESyECBZCBAshgoUQwUKIYCFEsBAiWAh5y6bT1GbNalPnXb0hNPU+3Jdjr5zXhIUQwUKIYCFEsBAiWAgRLIQIFkIECyGChZDRTafVGz1nrf5+Vznvau7LsVfehwkLIYKFEMFCiGAhRLAQIlgIESyECBZCBAshNp0emDqv53fsbuc9YsJCiGAhRLAQIlgIESyECBZCBAshgoUQwUKITacHps77xCtZavfz3u2+HDFhIUSwECJYCBEshAgWQgQLIYKFEMFCiGAhZHTTaXdXOe/UOdyXY6+c14SFEMFCiGAhRLAQIlgIESyECBZCBAshgoWQt2w63c3ZR7h6E+Yqn3c3TyT3HxMWQgQLIYKFEMFCiGAhRLAQIlgIESyECBZCntp0AmaZsBAiWAgRLIQIFkIECyGChRDBQohgIUSwEHKp33RavbR1t99gOmv3v7vaTu/DhIUQwUKIYCFEsBAiWAgRLIQIFkIECyGChZDR33Sa2lw5a2pTZ6fNmk9YfQ9WP7+zPvGcTVgIESyECBZCBAshgoUQwUKIYCFEsBAiWAh5y6bT1AbO1CbRaqu/3xte8Sm734Mpr5zXhIUQwUKIYCFEsBAiWAgRLIQIFkIECyGChRCbTgus3qw5+/1Wn/duz6/IhIUQwUKIYCFEsBAiWAgRLIQIFkIECyGChZDRTacpu2/+nHWVTSfOM2EhRLAQIlgIESyECBZCBAshgoUQwUKIYCHkLZtOHNv9t4umNtSmNrF2P+8RExZCBAshgoUQwUKIYCFEsBAiWAgRLIQIFkKe2nSa2gzZ3SubK5+wekPorN3vy+7v7YgJCyGChRDBQohgIUSwECJYCBEshAgWQgQLIW/ZdCpukBzZ/bxX2SRa/Zynnssn7oEJCyGChRDBQohgIUSwECJYCBEshAgWQgQLIaObTrtvpKw+71mrn8vq77fa1L2aem+v/F0TFkIECyGChRDBQohgIUSwECJYCBEshAgWQmw6PbD7Bs7un8d6JiyECBZCBAshgoUQwUKIYCFEsBAiWAgRLITYdHrgKued8sTVWurKG1smLIQIFkIECyGChRDBQohgIUSwECJYCBEshIxuOu1uatNp9efdzdT9+0QfJiyECBZCBAshgoUQwUKIYCFEsBAiWAgRLIS8ZdPpbqY2k6b+7pRXNoSOfGIzaTUTFkIECyGChRDBQohgIUSwECJYCBEshAgWQp7adAJmmbAQIlgIESyECBZCBAshgoUQwUKIYCFEsBAiWAgRLIQIFjK+vv4Ay06kcX0DUNAAAAAASUVORK5CYII='

vers='R.01.1 - 2025-01-23'
title_project= 'QR-Code Generator'
theme_UI='Default1'
#------------------------------------------------------------------------------------------

sg.theme(theme_UI)
menu_def = [
    ['&Help', '&About...'], ]
#------------------------------------------------------------------------------------------

figure_w = 400
figure_h = 300
folder_or_file = ""
fill_color_qrcode = 'black'
back_color_qrcode = 'white'

#Create layout
layout_qrcode_generator1 = [
    [sg.Text('', size=(15,1)),],
    [sg.Text('URL or text to display', size=(18,1)), sg.Input(default_text='', size=(35,1), enable_events=True, k='k_txt_url', disabled=False, tooltip='URL or text to display')],
    [sg.Text('', size=(15,1))],
    [sg.Checkbox('Add an image to the qr-code', enable_events=True, default=False, k='k_cb_image'),
     sg.Button('Select image', k='k_bt_image', tooltip='Select the image to add to the qr-code', disabled=True)],
    [sg.Text('', size=(15,1)),],

    [sg.Text('Change colors to the qr-code. Fill color:', size=(29,1)),
    sg.In("", visible=False, enable_events=True, key='k_c_fill_qrcode', disabled=False), sg.ColorChooserButton("", size=(1, 1), target='k_c_fill_qrcode', button_color=(fill_color_qrcode, fill_color_qrcode), border_width=1, key='k_c_fill_qrcode_chooser', disabled=False),
    sg.Text('Back color:', size=(8,1)),
    sg.In("", visible=False, enable_events=True, key='k_c_back_qrcode', disabled=False), sg.ColorChooserButton("", size=(1, 1), target='k_c_back_qrcode', button_color=(back_color_qrcode, back_color_qrcode), border_width=1, key='k_c_back_qrcode_chooser', disabled=False)],

    [sg.Text('', size=(15,1)),],
    [sg.Text("      Generate qr-code  "), sg.Button('Generate', k='k_bt_generate', tooltip='Generate qr-code')],
    [sg.Text('', size=(15,1)),],
    [sg.Text("      Save qr-code       "), sg.Button('Save', k='k_bt_save', tooltip='Save qr-code', disabled=True)],
    [sg.Text('', size=(15,1)),],
    [sg.Text('', size=(5,1)), sg.Button("Reset", size=(10, 1), key='bt_reset'), sg.Text('', size=(5,1)), sg.Exit('Exit', size=(10, 1), button_color=("white", "#191919"))],
    [sg.Text('', size=(15,1)),],    
]

layout_qrcode_generator2=[
    [sg.Text('', size=(7,1)),
    sg.Image(key='k_imgs', size=(200,200)),
    sg.Text('', size=(7,1)),],
]

layout= [ 
    [sg.Menu(menu_def, )],
    [sg.vtop(sg.Frame('', layout_qrcode_generator1, border_width=1, font='Any 8')), ],
    [sg.vtop(sg.Frame('QR-Code View', layout_qrcode_generator2, font='Any 8', size=(425,320))) ]
]


title_window= title_project +' - '+vers
window=sg.Window(title_window, font=("Helvetica", 10), resizable=True).Layout(layout)
window.finalize()
window.set_icon(name_icon)

while True:
    event, values = window.read()
    sg.SetOptions(text_justification='left')

    #------------------------------------------------------------------------------------------
    if event in (None, 'Exit'):
        break
    
    #------------------------------------------------------------------------------------------
    elif event == "About...":
        mess="\n\t   Version: " + str(vers) +"\n\n  Software developed by Intelisano Utvikling\n\nFor info contact: intelisano.marco@gmail.com\n"
        sg.popup(mess, keep_on_top=True, title = title_project, icon = name_icon)

    #------------------------------------------------------------------------------------------
    elif event == "k_bt_generate":
        data=values['k_txt_url']
        img_view=values['k_cb_image']

        if folder_or_file:
            logo_path = folder_or_file
        else:
            logo_path = getcwd()
        qrcode_imgdata=create_colored_qr_code(data, logo_path, fill_color_qrcode, back_color_qrcode, img_view)
        if qrcode_imgdata :
            larghezza_orig, altezza_orig = qrcode_imgdata.size
            rapporto = larghezza_orig / altezza_orig
            nuova_larghezza = int(figure_h * rapporto)
            img_ridimensionata = qrcode_imgdata.resize((nuova_larghezza, figure_h), Image.LANCZOS)

            buf = BytesIO()
            img_ridimensionata.save(buf, format="png")
            imgdata = b64encode(buf.getbuffer()).decode()

            window['k_imgs'].Update(data=imgdata, visible=True)
            window.refresh()
            window['k_bt_save'].Update(disabled=False)
        
    #------------------------------------------------------------------------------------------
    elif event == "k_cb_image":
        if values['k_cb_image'] == True:
            window['k_bt_image'].Update(disabled=False)
        else:
            window['k_bt_image'].Update(disabled=True)

    #------------------------------------------------------------------------------------------
    elif event == "bt_reset":
        window['k_imgs'].Update(data="", visible=True)
        window['k_txt_url'].Update('')
        window['k_cb_image'].Update(False)
        window['k_bt_image'].Update(disabled=True)
        window['k_bt_save'].Update(disabled=True)
        window['k_c_fill_qrcode_chooser'].Update(button_color=('black', 'black'))
        fill_color_qrcode = (0, 0, 0)
        window['k_c_back_qrcode_chooser'].Update(button_color=('white', 'white'))
        back_color_qrcode = (255, 255, 255)
        window.refresh()

    #------------------------------------------------------------------------------------------
    elif event == "k_bt_image":
        try:
            current_directory = getcwd()
            folder_or_file = sg.popup_get_file('Select your file', initial_folder=current_directory, keep_on_top=True, file_types=(('PNG','*.png'),), icon = name_icon, title=title_project, no_window=True)
            logo = Image.open(folder_or_file)
            larghezza_orig, altezza_orig = logo.size
            rapporto = larghezza_orig / altezza_orig
            nuova_larghezza = int(figure_h * rapporto)
            img_ridimensionata = logo.resize((nuova_larghezza, figure_h), Image.LANCZOS)

            buf = BytesIO()
            img_ridimensionata.save(buf, format="png")
            imgdata = b64encode(buf.getbuffer()).decode()

            window['k_imgs'].Update(data=imgdata, visible=True)
            window.refresh()
        except:
            sg.popup("Select an image to add to the qr-code", keep_on_top=True, icon = name_icon, title=title_project) 

    #------------------------------------------------------------------------------------------
    elif event == "k_bt_save":
        try:
            qrcode_imgdata.save("".join([getcwd(),"\\", name_qrcode]))
        except:
            sg.popup("Generate qr-code before", keep_on_top=True, icon = name_icon, title=title_project) 

    #------------------------------------------------------------------------------------------
    elif event == 'k_c_fill_qrcode':        
        try:
            window['k_c_fill_qrcode_chooser'].Update(button_color=(values[event], values[event]))
            fill_color_qrcode = hex_to_rgb(values[event])
        except:
            sg.popup("Select the color for the  qr-code filling", keep_on_top=True, icon = name_icon, title=title_project)

    #------------------------------------------------------------------------------------------
    elif event == 'k_c_back_qrcode':        
        try:
            window['k_c_back_qrcode_chooser'].Update(button_color=(values[event], values[event]))
            back_color_qrcode = hex_to_rgb(values[event])
        except:
            sg.popup("Select the color for the back of the qr-code", keep_on_top=True, icon = name_icon, title=title_project)





