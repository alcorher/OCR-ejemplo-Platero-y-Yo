# Actividad 1.4 - OCR

Script de reconocimiento óptico de caracteres (OCR) aplicado a una imagen de
*Platero y yo*. El programa prepara la imagen para mejorar la lectura del
texto y utiliza Tesseract para extraerlo.

## Requisitos

- Python 3.14 o superior.
- Tesseract OCR instalado en Windows.
- El paquete de idioma español de Tesseract, recomendado para reconocer
  correctamente las tildes y la letra `ñ`.

El script espera encontrar el ejecutable de Tesseract en:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

Si Tesseract está instalado en otra ubicación, hay que modificar
`pytesseract.pytesseract.tesseract_cmd` en `main.py`.

## Instalación

### Con uv

Este proyecto incluye `pyproject.toml` y `uv.lock`, por lo que se puede
instalar con [uv](https://docs.astral.sh/uv/):

```powershell
uv sync
```

### Con pip

También se pueden instalar las dependencias directamente:

```powershell
pip install -e .
```

Las dependencias principales son:

- OpenCV: lectura y transformación de imágenes.
- Matplotlib: visualización de las etapas del procesamiento.
- Pillow: conversión de la imagen para Tesseract.
- Pytesseract: conexión entre Python y Tesseract OCR.

## Uso

Coloca la imagen de entrada con el nombre `imagen.jpg` en la raíz del
proyecto y ejecuta:

```powershell
uv run python main.py
```

O, si las dependencias ya están instaladas en el entorno activo:

```powershell
python main.py
```

El programa:

1. Carga `imagen.jpg`.
2. Recorta aproximadamente la zona inferior de la imagen, donde se encuentra
   el texto.
3. Convierte el recorte a escala de grises.
4. Lo amplía tres veces.
5. Mejora el contraste mediante CLAHE.
6. Aplica enfoque con una máscara de desenfoque (*Unsharp Mask*).
7. Realiza una binarización mediante el método de Otsu.
8. Muestra una figura con la imagen original y cada etapa del procesamiento.
9. Envía la imagen binarizada a Tesseract y muestra el texto extraído.
10. Muestra una segunda versión del texto eliminando líneas vacías y espacios
    al principio y al final.

## Ajustes

El recorte está definido mediante porcentajes del tamaño de la imagen en
`main.py`. Para procesar imágenes con una composición diferente, ajusta las
variables `fila1`, `fila2`, `columna1` y `columna2`.

Para utilizar el modelo de idioma español, instala `spa.traineddata` en la
carpeta `tessdata` de Tesseract y cambia la llamada OCR a:

```python
texto = pytesseract.image_to_string(pil_image, lang="spa")
```

## Estructura

```text
.
├── imagen.jpg      # Imagen de entrada
├── main.py         # Procesamiento de imagen y extracción OCR
├── pyproject.toml  # Metadatos y dependencias del proyecto
├── uv.lock         # Versiones bloqueadas para uv
└── README.md       # Documentación
```

## Notas

- La ejecución abre una ventana de Matplotlib; debe cerrarse para continuar
  cuando el entorno lo requiera.
- La calidad del resultado depende de la resolución, el contraste y la
  orientación de la imagen.
- El programa imprime el resultado en la consola y no genera un archivo de
  texto automáticamente.