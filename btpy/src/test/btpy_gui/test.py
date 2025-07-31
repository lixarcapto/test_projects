from PIL import Image
import os

def pegar_imagen(
    imagen_base: Image.Image,
    imagen_a_pegar: Image.Image,
    posicion: tuple[int, int]
) -> Image.Image:
    """
    Pega una imagen de PIL en otra imagen de PIL, manejando la transparencia
    automáticamente si la imagen a pegar tiene un canal alfa.

    Args:
        imagen_base (Image.Image): El objeto de imagen de Pillow que sirve como lienzo.
                                   Se modificará y se devolverá.
        imagen_a_pegar (Image.Image): El objeto de imagen de Pillow que se superpondrá.
        posicion (tuple[int, int]): La coordenada (x, y) de la esquina superior izquierda
                                    donde se pegará la imagen.

    Returns:
        Image.Image: La imagen base modificada con la nueva imagen pegada.
    """
    # Si la imagen a pegar no tiene un canal alfa, la convertimos a RGBA.
    # Esto asegura que podemos obtener una máscara de transparencia.
    if imagen_a_pegar.mode != 'RGBA':
        imagen_a_pegar = imagen_a_pegar.convert('RGBA')
    
    # Separamos los canales de la imagen a pegar para obtener el canal alfa (transparencia)
    _, _, _, a = imagen_a_pegar.split()

    try:
        # Pegamos la imagen en el lienzo, usando su propio canal alfa como máscara.
        # Esto previene que los píxeles transparentes de 'imagen_a_pegar'
        # sobrescriban los píxeles de 'imagen_base'.
        imagen_base.paste(imagen_a_pegar, posicion, mask=a)
        print(f"✅ Imagen pegada exitosamente en la posición {posicion}.")
    except ValueError as e:
        print(f"❌ Error al pegar la imagen: {e}. Verifique que las coordenadas y las dimensiones sean correctas.")
    
    return imagen_base

# --- Ejemplo de Uso ---
if __name__ == "__main__":
    from PIL import ImageDraw

    # Crear un lienzo de fondo de color
    lienzo = Image.new(
        'RGB', (400, 300), 
        color='lightblue')
    # Crear una "estampa" o "logo" con transparencia
    # El modo 'RGBA' y el color (0,0,0,0) crean un fondo completamente transparente
    PATH = "./res/solar.png"
    logo = Image.open(PATH).convert("RGB")
    # Guardar las imágenes de ejemplo
    lienzo.save("lienzo_original.png")
    logo.save("logo_transparente.png")
    
    # Usar la función para pegar el logo en el lienzo
    imagen_final = pegar_imagen(
        imagen_base=lienzo, 
        imagen_a_pegar=logo, 
        posicion=(150, 100)
    )
    
    # Guardar y mostrar el resultado final
    ruta_final = "imagen_final.png"
    imagen_final.save(ruta_final)
    print(f"Imagen final guardada en '{ruta_final}'")
    imagen_final.show(title="Imagen con estampa transparente")
    
    # --- Limpieza de archivos de ejemplo ---
    print("\n--- Limpiando archivos de ejemplo ---")
    if os.path.exists("lienzo_original.png"):
        os.remove("lienzo_original.png")
    if os.path.exists("logo_transparente.png"):
        os.remove("logo_transparente.png")
    if os.path.exists(ruta_final):
        os.remove(ruta_final)