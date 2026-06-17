import struct
import os

def get_png_size(filename):
    with open(filename, 'rb') as f:
        # PNG signature
        f.read(8)
        # IHDR chunk
        f.read(4)  # length
        f.read(4)  # type
        width, height = struct.unpack('>II', f.read(8))
        return width, height

# Check logos folder
logos_dir = 'logos'
print("=== BANKA LOGOLARI ===")
for filename in os.listdir(logos_dir):
    if filename.endswith('.png'):
        filepath = os.path.join(logos_dir, filename)
        try:
            w, h = get_png_size(filepath)
            print(f"{filename}: {w}x{h} piksel")
        except Exception as e:
            print(f"{filename}: Hata - {e}")

# Check POLVAK logo
print("\n=== POLVAK LOGOSU ===")
try:
    w, h = get_png_size("POLVAK MAX Logo.png")
    print(f"POLVAK MAX Logo.png: {w}x{h} piksel")
except Exception as e:
    print(f"POLVAK MAX Logo.png: Hata - {e}")
