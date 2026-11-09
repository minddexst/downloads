import sys
from yt_dlp import YoutubeDL
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def progress_hook(d):
    if d['status'] == 'downloading':
        p = d.get('_percent_str', '0.0%').strip()
        speed = d.get('_speed_str', 'N/A').strip()
        eta = d.get('_eta_str', 'N/A').strip()
        sys.stdout.write(f"\r[Téléchargement] Avancement : {p} | Vitesse : {speed} | ETA : {eta}   ")
        sys.stdout.flush()
    elif d['status'] == 'finished':
        console.print("\n\n[white] Téléchargement terminé ! Finalisation du fichier...[/white]")

def main():
    url = Prompt.ask("[bold white]Colle l'URL de la vidéo[/bold white]")
    if "tiktok.com" in url:
        console.print("[bold white] Lien TikTok détecté ![/bold white]\n")
    elif "instagram.com" in url:
        console.print("[bold white] Lien Instagram / Reel détecté ![/bold white]\n")
    elif "youtube.com" in url or "youtu.be" in url:
        console.print("[bold white] Lien YouTube détecté ![/bold white]\n")
    elif "twitter.com" in url or "x.com" in url:
        console.print("[bold white] Lien Twitter / X détecté ![/bold white]\n")
    else:
        console.print("[bold white] Lien multimédia détecté ![/bold white]\n")
    console.print("[bold white]Select download format:[/bold white]")
    console.print("[bold white]1 — Video only[/bold white]")
    console.print("[bold white]2 — Audio only (MP3)[/bold white]")
    console.print("[bold white]3 — Video + Audio (Both combined)[/bold white]")
    choix = Prompt.ask(
        "[bold white]Enter your choice[/bold white]",
        choices=["1", "2", "3"],
        default="3"
    )
    
    ydl_opts = {
        'progress_hooks': [progress_hook],
        'outtmpl': 'downloads/%(uploader)s_%(id)s.%(ext)s',
    }
    
    if choix == '1':
        ydl_opts.update({
            'format': 'bestvideo',
        })
        console.print("\n[white]Video mode selected...[/white]\n")
    elif choix == '2':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
        console.print("\n[white]Audio mode selected (MP3)...[/white]\n")
    else:
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'noplaylist': False,
        })
        console.print("\n[white]Combined mode selected (Video + Audio)...[/white]\n")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        console.print("\n[bold white]Everything is good! File saved successfully.[/bold white]")
    except Exception as e:
        console.print(f"\n[bold white]An error occurred : {e}[/bold white]")

if __name__ == "__main__":
    main()