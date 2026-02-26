import sys
from PIL import Image, ImageOps


# Verificar cantidad de argumentos
if len(sys.argv) != 3:
    sys.exit("Too few or too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

# Extensiones válidas
valid = [".jpg", ".jpeg", ".png"]

# Verificar extensión del input
if not input_file.lower().endswith(tuple(valid)):
    sys.exit("Invalid input")

# Verificar extensión del output
if not output_file.lower().endswith(tuple(valid)):
    sys.exit("Invalid output")

# Verificar que tengan la misma extensión
if input_file.split(".")[-1].lower() != output_file.split(".")[-1].lower():
    sys.exit("Input and output have different extensions")

try:
    # Abrir imagen principal
    image = Image.open(input_file)

    # Abrir camisa
    shirt = Image.open("shirt.png")

    # Ajustar tamaño
    image = ImageOps.fit(image, shirt.size)

    # Pegar camisa encima
    image.paste(shirt, shirt)

    # Guardar resultado
    image.save(output_file)

except FileNotFoundError:
    sys.exit("Input does not exist")