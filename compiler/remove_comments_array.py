

from btpy_lib.btpy.src.btpy.Btpy import Btpy
import re

def remove_comments_array(array):
    for i in range(len(array)):
        array[i] = __remove_comments(array[i])
    return array

def __remove_comments_old(text):
    r = text
    while("/*" in r):
        r = Btpy.remove_between(r,
            "/*", "*/")
    while("//" in r):
        if(Btpy.has_between(r,
                "//", " ")):
            r = Btpy.remove_between(r,
                "//", " ")
        if(Btpy.has_between(r,
            "//", "\n")):
            r = Btpy.remove_between(r,
                "//", "\n")
    return r

def __remove_comments(codigo):
  """
  Elimina los comentarios de una cadena de código JavaScript.

  Args:
    codigo: La cadena de código JavaScript como entrada.

  Returns:
    Una nueva cadena con los comentarios eliminados.
  """

  # Expresiones regulares para comentarios de una línea y multilínea
  patron_comentario_linea = r"//.*"
  patron_comentario_multiline = r"/\*.*?\*/"

  # Eliminar comentarios de una línea
  codigo = re.sub(patron_comentario_linea, "", codigo, flags=re.MULTILINE)

  # Eliminar comentarios de múltiples líneas
  codigo = re.sub(patron_comentario_multiline, "", codigo, flags=re.DOTALL)

  return codigo