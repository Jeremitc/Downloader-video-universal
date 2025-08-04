import sys
import os
import yt_dlp

def download_video(url):
    """
    Downloads a video from the given URL using yt-dlp.
    """
    # Create a 'downloads' directory if it doesn't exist
    download_folder = 'downloads'
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # yt-dlp options
    # -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best': Download best quality MP4 video and audio, fallback to best quality overall.
    # -o: Output template for the filename.
    # --merge-output-format mp4: Merge video and audio into an MP4 container.
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'quiet': False, # Set to False to see yt-dlp output
        'no_warnings': True,
        'ignoreerrors': True,
    }

    try:
        print(f"[*] Iniciando descarga desde: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n[+] Descarga completada con éxito.")
        print(f"[*] El video se ha guardado en la carpeta '{download_folder}'.")

    except Exception as e:
        print(f"\n[-] Ocurrió un error durante la descarga.")
        print(f"[-] Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    # Prompt the user for the video URL
    video_url = input("Por favor, introduce la URL del video y presiona Enter: ")

    # Check if the URL is empty
    if not video_url.strip():
        print("[-] No se ha introducido ninguna URL. Saliendo.")
        sys.exit(1)

    # Start the download
    download_video(video_url.strip())
