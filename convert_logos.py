import base64
import os

logos_dir = os.path.dirname(__file__) + '/logos/'
logos = ['isbankasi', 'ziraat', 'koopbank', 'vakiflar', 'poliskoop']

for logo_name in logos:
    png_path = logos_dir + logo_name + '.png'
    with open(png_path, 'rb') as f:
        png_bytes = f.read()
    
    b64_data_url = 'data:image/png;base64,' + base64.b64encode(png_bytes).decode('ascii')
    
    txt_path = logos_dir + logo_name + '.b64.txt'
    with open(txt_path, 'w') as f:
        f.write(b64_data_url)
    
    print(f'{logo_name}: {len(b64_data_url)} chars')

print('Tüm logolar base64 data URL olarak kaydedildi!')
