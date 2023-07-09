import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
MP3_AUDIO = []
OTHER = []
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []

DOC_DOCUMENT = []
DOCX_DOCUMENT = []
TXT_DOCUMENT = []
PDF_DOCUMENT = []
XLSX_DOCUMENT = []
PPTX_DOCUMENT = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

REGISTER_EXTENSION = {
    "JPEG": JPEG_IMAGES,
    "JPG": JPG_IMAGES,
    "PNG": PNG_IMAGES,
    "SVG": SVG_IMAGES,
    "OGG": OGG_AUDIO,
    "WAV": WAV_AUDIO,
    "AMR": AMR_AUDIO,
    "MP3": MP3_AUDIO,
    "ZIP": ZIP_ARCHIVES,
    "GZ": GZ_ARCHIVES,
    "TAR": TAR_ARCHIVES,
    "DOC": DOC_DOCUMENT,
    "DOCX": DOCX_DOCUMENT,
    "TXT": TXT_DOCUMENT,
    "PDF": PDF_DOCUMENT,
    "XLSX": XLSX_DOCUMENT,
    "PPTX": PPTX_DOCUMENT,
    "AVI": AVI_VIDEO,
    "MP4": MP4_VIDEO,
    "MOV": MOV_VIDEO,
    "MKV": MKV_VIDEO,
}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return (
        Path(filename).suffix[1:].upper()
    )  # перетворюємо розширення файлу на назву папки jpg -> JPG


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # Якщо це папка то додаємо її до списку FOLDERS і переходимо до наступного елемента папки
        if item.is_dir():
            # перевіряємо, щоб папка не була тією в яку ми складаємо вже файли
            if item.name not in (
                "archives",
                "video",
                "audio",
                "documents",
                "images",
                "other",
            ):
                FOLDERS.append(item)
                # скануємо вкладену папку
                scan(item)  # рекурсія
            continue  # переходимо до наступного елементу в сканованій папці

        #  Робота з файлом
        ext = get_extension(item.name)  # беремо розширення файлу
        fullname = folder / item.name  # беремо шлях до файлу
        if not ext:  # якщо файл немає розширення то додаєм до невідомих
            OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSION.add(ext)
                container.append(fullname)
            except KeyError:
                # Якщо ми не зареєстрували розширення у REGISTER_EXTENSION, то додаємо до невідомих
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == "__main__":
    folder_to_scan = sys.argv[1]
    print(f"Start in folder {folder_to_scan}")
    scan(Path(folder_to_scan))
    print(f"Images jpeg: {JPEG_IMAGES}")
    print(f"Images png: {PNG_IMAGES}")
    print(f"Images jpg: {JPG_IMAGES}")
    print(f"Images svg: {SVG_IMAGES}")
    print(f"Audio mp3: {MP3_AUDIO}")
    print(f"Audio ogg: {OGG_AUDIO}")
    print(f"Audio wav: {WAV_AUDIO}")
    print(f"Audio amr: {AMR_AUDIO}")
    print(f"Video avi: {AVI_VIDEO}")
    print(f"Video mp4: {MP4_VIDEO}")
    print(f"Video mov: {MOV_VIDEO}")
    print(f"Video mkv: {MKV_VIDEO}")
    print(f"Archives zip: {ZIP_ARCHIVES}")
    print(f"Archives gz: {GZ_ARCHIVES}")
    print(f"Archives tar: {TAR_ARCHIVES}")
    print(f"Documents doc: {DOC_DOCUMENT}")
    print(f"Documents docx: {DOCX_DOCUMENT}")
    print(f"Documents txt: {TXT_DOCUMENT}")
    print(f"Documents pdf: {PDF_DOCUMENT}")
    print(f"Documents xlsx: {XLSX_DOCUMENT}")
    print(f"Documents pptx: {PPTX_DOCUMENT}")

    print(f"Types of files in folder: {EXTENSION}")
    print(f"Unknown files of types: {UNKNOWN}")
    print(f"Other: {OTHER}")

    print(FOLDERS)
