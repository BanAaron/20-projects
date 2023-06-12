from pathlib import Path
from requests import get


def get_extension(image_url: str) -> str | None:
    valid_extensions: list[str] = [".png", "jpeg", ".jpg", ".gif", ".svg"]
    for extension in valid_extensions:
        if extension in image_url:
            return extension


def download_image(image_url: str, location: str) -> ():
    file_type: str = get_extension(image_url)
    if file_type is None:
        raise ValueError("Invalid file type.")

    file_path: Path = Path(location + file_type)

    try:
        image_content: bytes = get(image_url).content
        with open(file_path, "wb") as save_file:
            save_file.write(image_content)
    except Exception as e:
        print(f"{e}")


if __name__ == '__main__':
    download_image("https://hips.hearstapps.com/hmg-prod/images/funny-dog-captions-1563456605.jpg?crop=0.748xw:1.00xh"
                   ";0.0897xw,0&resize=768:*", "images/test")
