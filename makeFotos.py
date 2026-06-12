from PIL import Image
from tkinter import Tk, filedialog
import os
import math

# =====================================
# CONFIGURAÇÕES
# =====================================

PAGE_WIDTH = 2480
PAGE_HEIGHT = 3508

MARGIN = 80
SPACING = 30

PHOTOS_PER_ROW = 2
PHOTOS_PER_COLUMN = 2

JPEG_QUALITY = 95

# =====================================
# SELECIONAR FOTOS
# =====================================

root = Tk()
root.withdraw()

fotos = filedialog.askopenfilenames(
    title="Selecione as fotos",
    filetypes=[
        ("Imagens", "*.jpg *.jpeg *.png *.webp")
    ]
)

if not fotos:
    print("Nenhuma foto selecionada.")
    exit()

# =====================================
# ESCOLHER PASTA DE SAÍDA
# =====================================

output_dir = filedialog.askdirectory(
    title="Selecione a pasta de saída"
)

if not output_dir:
    print("Nenhuma pasta selecionada.")
    exit()

# =====================================
# FUNÇÕES
# =====================================

def resize_and_crop(img, target_width, target_height):

    img_ratio = img.width / img.height
    target_ratio = target_width / target_height

    if img_ratio > target_ratio:

        new_height = target_height
        new_width = int(new_height * img_ratio)

        img = img.resize(
            (new_width, new_height),
            Image.LANCZOS
        )

        left = (new_width - target_width) // 2

        img = img.crop(
            (
                left,
                0,
                left + target_width,
                target_height
            )
        )

    else:

        new_width = target_width
        new_height = int(new_width / img_ratio)

        img = img.resize(
            (new_width, new_height),
            Image.LANCZOS
        )

        top = (new_height - target_height) // 2

        img = img.crop(
            (
                0,
                top,
                target_width,
                top + target_height
            )
        )

    return img

# =====================================
# CÁLCULOS
# =====================================

photos_per_page = (
    PHOTOS_PER_ROW *
    PHOTOS_PER_COLUMN
)

usable_width = (
    PAGE_WIDTH -
    (2 * MARGIN) -
    ((PHOTOS_PER_ROW - 1) * SPACING)
)

usable_height = (
    PAGE_HEIGHT -
    (2 * MARGIN) -
    ((PHOTOS_PER_COLUMN - 1) * SPACING)
)

photo_width = usable_width // PHOTOS_PER_ROW
photo_height = usable_height // PHOTOS_PER_COLUMN

total_pages = math.ceil(
    len(fotos) / photos_per_page
)

print(f"Fotos selecionadas: {len(fotos)}")
print(f"Páginas necessárias: {total_pages}")

# =====================================
# GERAR PÁGINAS
# =====================================

for page_number in range(total_pages):

    folha = Image.new(
        "RGB",
        (PAGE_WIDTH, PAGE_HEIGHT),
        "white"
    )

    start = page_number * photos_per_page
    end = start + photos_per_page

    fotos_pagina = fotos[start:end]

    for idx, foto_path in enumerate(fotos_pagina):

        try:

            img = Image.open(
                foto_path
            ).convert("RGB")

            img = resize_and_crop(
                img,
                photo_width,
                photo_height
            )

            row = idx // PHOTOS_PER_ROW
            col = idx % PHOTOS_PER_ROW

            x = (
                MARGIN +
                col *
                (photo_width + SPACING)
            )

            y = (
                MARGIN +
                row *
                (photo_height + SPACING)
            )

            folha.paste(img, (x, y))

            img.close()

        except Exception as erro:

            print(
                f"Erro em {foto_path}: {erro}"
            )

    output_file = os.path.join(
        output_dir,
        f"pagina_{page_number + 1}.jpg"
    )

    folha.save(
        output_file,
        "JPEG",
        quality=JPEG_QUALITY,
        dpi=(300, 300)
    )

    print(
        f"Página {page_number + 1} criada."
    )

print("\nConcluído com sucesso!")

