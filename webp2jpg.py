'''
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
pip install webptools
pip install libwebp

cd /filespath/
python3 webp2jpg.py
'''
import os
from PIL import Image
from pathlib import Path

for root, _, files in os.walk(os.getcwd()):
	for f in files:
		if f.endswith('.webp'):
			fullname = os.path.join(root, f)
			print (fullname)
			caminho = (os.path.join(root))
			filename = (Path(f).stem)
			
			im = Image.open(fullname).convert("RGB")
			im.save(caminho + "/" + filename + ".jpg","jpeg")

print('\nDone!!')
     

