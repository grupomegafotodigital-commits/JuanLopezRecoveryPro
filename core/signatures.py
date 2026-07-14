"""
Firmas binarias de formatos conocidos.
Cada firma representa el inicio (header) de un archivo.
"""


FILE_SIGNATURES = {

    "jpg": [
        bytes.fromhex("FFD8FFE0"),
        bytes.fromhex("FFD8FFE1"),
        bytes.fromhex("FFD8FFE8"),
    ],

    "png": [
        bytes.fromhex("89504E470D0A1A0A"),
    ],

    "gif": [
        b"GIF87a",
        b"GIF89a",
    ],

    "bmp": [
        bytes.fromhex("424D"),
    ],

    "tiff": [
        bytes.fromhex("49492A00"),
        bytes.fromhex("4D4D002A"),
    ],

    "pdf": [
        b"%PDF",
    ],

    "zip": [
        bytes.fromhex("504B0304"),
    ],

    "mp4": [
        b"ftyp",
    ],

    "cr2": [
        bytes.fromhex("49492A00100000004352"),
    ],

    "nef": [
        bytes.fromhex("4D4D002A"),
    ],

    "arw": [
        bytes.fromhex("49492A00"),
    ],
}