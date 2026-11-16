import cv2
from matplotlib import pyplot as plt
import pytesseract
from PIL import Image


img = cv2.imread('imagen.jpg')
alto, ancho = img.shape[:2]

#Recorte 
fila1 = int(alto * 0.52)
fila2 = int(alto * 0.95)
columna1 = int(ancho * 0.04)
columna2 = int(ancho * 0.96)
recorte = img[fila1:fila2, columna1:columna2]

#escala de grises
gray = cv2.cvtColor(recorte, cv2.COLOR_BGR2GRAY)

# Reescalado x3
resized = cv2.resize(gray, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

# Mejora contraste
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
contrast = clahe.apply(resized)

# Enfoque con Unsharp Mask
gaussian = cv2.GaussianBlur(contrast, (5, 5), 10.0)
unsharp = cv2.addWeighted(contrast, 1.5, gaussian, -0.5, 0)

# Binarización Otsu
_, binary = cv2.threshold(unsharp, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)



fig, axes = plt.subplots(2, 3, figsize=(15, 8))
# Fila 1: Original
axes[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  #sin esto se veía con el fondo azul por el formato de la imagen que necesita matplotlib
axes[0, 0].set_title("1. Imagen Original")
axes[0, 0].axis("off")
# Recorte
axes[0, 1].imshow(cv2.cvtColor(recorte, cv2.COLOR_BGR2RGB))
axes[0, 1].set_title("2. Recorte (ROI)")
axes[0, 1].axis("off")
# Escala de Grises
axes[0, 2].imshow(gray, cmap='gray')
axes[0, 2].set_title("3. Escala de Grises")
axes[0, 2].axis("off")
# Fila 2: Contraste CLAHE
axes[1, 0].imshow(contrast, cmap='gray')
axes[1, 0].set_title("4-5. Escalado x3 + CLAHE")
axes[1, 0].axis("off")
# Enfocado Unsharp Mask
axes[1, 1].imshow(unsharp, cmap='gray')
axes[1, 1].set_title("6. Enfocado (Unsharp Mask)")
axes[1, 1].axis("off")
# Binarización Otsu
axes[1, 2].imshow(binary, cmap='gray')
axes[1, 2].set_title("7. Binarización (Otsu)")
axes[1, 2].axis("off")
plt.tight_layout()
plt.show()

# Aquí si instalamos el lenguaje español y lo usamos tendremos menos fallos en letras con acentos y ñ.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pil_image = Image.fromarray(binary)
texto = pytesseract.image_to_string(pil_image)

print("Texto extraído de la imagen:")
print(texto)


# Limpiar texto
lineas_limpias = [linea.strip() for linea in texto.splitlines() if linea.strip()]
texto_formateado = "\n".join(lineas_limpias)

print("Texto formateado:")
print(texto_formateado)

