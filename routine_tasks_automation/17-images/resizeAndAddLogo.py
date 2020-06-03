import os
from PIL import Image

os.chdir('./routine_tasks_automation/17-images/')

SQUARE_FIT_SIZE = 500
LOGO_FILENAME = 'logo.png'

LogoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = LogoIm.size

for filename in os.listdir('./images/'):
    if not (filename.endswith('.png') or
            filename.endswith('jpg')) or filename == LOGO_FILENAME:
        continue
    im = Image.open('./images/' + filename)
    width, heigth = im.size
    if width > SQUARE_FIT_SIZE and heigth > SQUARE_FIT_SIZE:
        if width > heigth:
            heigth = int((SQUARE_FIT_SIZE / heigth) * width)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / heigth) * width)
            heigth = SQUARE_FIT_SIZE
        print(f'Изменение размеров изображения {filename}...')
        im = im.resize((width, heigth))

    # Добавление логотипа
    print(f'Добавление логотипа в изображение {filename}...')
    im.paste(LogoIm, (width - logoWidth, heigth - logoHeight), LogoIm)
    im.save(os.path.join('withLogo', filename))
