from moviepy.editor import VideoFileClip
import os

def convert_all_videos_in_directory():
    # Obtener la ruta del directorio del script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Crear la carpeta "Convert" si no existe
    convert_dir = os.path.join(script_dir, "Convert")
    if not os.path.exists(convert_dir):
        os.makedirs(convert_dir)
    
    # Procesar cada archivo de video en el directorio del script
    for filename in os.listdir(script_dir):
        # Filtrar solo los archivos de video (aquí puedes añadir más extensiones si es necesario)
        if filename.endswith((".mp4", ".avi", ".mov", ".mkv")):
            # Ruta completa del video de entrada
            input_path = os.path.join(script_dir, filename)
            
            # Generar el nombre del archivo de salida
            filename_without_ext = os.path.splitext(filename)[0]
            output_filename = f"{filename_without_ext}Con.mp4"
            output_path = os.path.join(convert_dir, output_filename)
            
            # Cargar el video
            video = VideoFileClip(input_path)
            
            # Quitar el audio
            video = video.without_audio()
            
            # Guardar el video en formato MP4 en la carpeta "Convert"
            video.write_videofile(output_path, codec='libx264')

# Ejecutar la función para convertir todos los videos en la carpeta del script
convert_all_videos_in_directory()
