



from ..out_deps import os, docx

"""
    Funcion que almacena en un archivo docx el texto
    enviado.
"""
# not return
def create_docx(route:str, text:str)->None:
    format = ".docx"
    if(format in route):
        route.replace(format, "")
    document = docx.Document()
    paragraph = document.add_paragraph(text)
    # Set paragraph style (optional)
    paragraph.style = "Normal"
    # Add additional formatting or elements as needed
    document.save(route + ".docx")