import base64
import json
import os

# Logo dizini
logos_dir = os.path.dirname(os.path.abspath(__file__))
logos_folder = os.path.join(logos_dir, 'logos')

# Logo dosyaları
logos = ['isbankasi', 'ziraat', 'koopbank', 'vakiflar', 'poliskoop']

base64_data = {}

for logo_name in logos:
    png_path = os.path.join(logos_folder, f'{logo_name}.png')
    
    if not os.path.exists(png_path):
        print(f'HATA: {png_path} bulunamadı!')
        continue
    
    with open(png_path, 'rb') as f:
        png_bytes = f.read()
    
    b64_str = base64.b64encode(png_bytes).decode('ascii')
    base64_data[logo_name] = f'data:image/png;base64,{b64_str}'
    print(f'{logo_name}: {len(base64_data[logo_name])} chars')

# JSON olarak kaydet
json_path = os.path.join(logos_dir, 'logos_base64.json')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(base64_data, f, indent=2, ensure_ascii=False)

print(f'\n✓ Base64 veriler kaydedildi: {json_path}')
