from yt_dlp import YoutubeDL

url = input("URL: ")

with YoutubeDL({}) as ydl:
    info = ydl.extract_info(url, download=False)

    for f in info["formats"]:
        altura = f.get("height")
        ext = f.get("ext")
        if altura:
            print(f"ID: {f['format_id']} | {altura}p | {ext}")