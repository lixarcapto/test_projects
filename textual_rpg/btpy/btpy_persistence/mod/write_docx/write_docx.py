



import os, docx


def write_docx(route:str, text:str)->None:
    """
    Funcion que almacena en un archivo 
    docx el texto
    enviado.
    """
    format = ".docx"
    if(format in route):
        route.replace(format, "")
    document = docx.Document()
    paragraph = document.add_paragraph(text)
    # Set paragraph style (optional)
    paragraph.style = "Normal"
    # Add additional formatting or elements as needed
    document.save(route + ".docx")