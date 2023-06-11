import sys

import qrcode
from sys import argv


class QrCode:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr_code(
        self, file_name: str, contents: str, fg: str = "black", bg: str = "white"
    ):
        try:
            self.qr.add_data(contents)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)
        except Exception as err:
            print(err)
            sys.exit()


if __name__ == "__main__":
    try:
        file: str = argv[1]
        content: str = argv[2]
    except IndexError:
        print("Invalid number of arguments provided.")
        sys.exit()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

    qr = QrCode(size=10, padding=2)
    qr.create_qr_code(f"{file}.png", content)
