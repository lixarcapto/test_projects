



export function dowload_with_blop(contenido) {
    const blob = new Blob([contenido], 
        { type: 'text/plain' }); 
    // Ajusta el tipo MIME según el archivo
    const url = URL.createObjectURL(blob);
    const enlace = document.createElement('a');
    enlace.href = url;
    enlace.download = 'mi_archivo.txt';
    document.body.appendChild(enlace);
    enlace.click();
    document.body.removeChild(enlace);
    URL.revokeObjectURL(url); // Libera la URL cuando ya no sea necesaria
}