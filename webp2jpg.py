'''
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
pip install webptools
pip install libwebp

cd /filespath/
python3 webp2jpg.py
'''
from PIL import Image
import glob
from pathlib import Path

for f in glob.glob("*.webp"):
    filename = (Path(f).stem)
    im = Image.open(filename + ".webp").convert("RGB")
    im.save(filename + ".jpg","jpeg")

print('\nDone!')
     

