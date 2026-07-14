import ctypes
from ctypes import wintypes


GENERIC_READ = 0x80000000
FILE_SHARE_READ = 0x00000001
FILE_SHARE_WRITE = 0x00000002
OPEN_EXISTING = 3
INVALID_HANDLE_VALUE = wintypes.HANDLE(-1).value


class PhysicalDrive:

    def __init__(self, device_path):

        self.device_path = device_path

        self.handle = None

    def open(self):

        kernel32 = ctypes.windll.kernel32

        self.handle = kernel32.CreateFileW(
            self.device_path,
            GENERIC_READ,
            FILE_SHARE_READ | FILE_SHARE_WRITE,
            None,
            OPEN_EXISTING,
            0,
            None,
        )

        if self.handle == INVALID_HANDLE_VALUE:
            raise OSError(
                f"No fue posible abrir {self.device_path}"
            )

    def close(self):

        if self.handle:

            ctypes.windll.kernel32.CloseHandle(self.handle)

            self.handle = None
                def seek(self, offset):

        kernel32 = ctypes.windll.kernel32

        FILE_BEGIN = 0

        result = kernel32.SetFilePointerEx(
            self.handle,
            ctypes.c_longlong(offset),
            None,
            FILE_BEGIN
        )

        if result == 0:
            raise OSError("No fue posible mover el puntero del disco.")

    def read(self, size):

        kernel32 = ctypes.windll.kernel32

        buffer = ctypes.create_string_buffer(size)

        bytes_read = wintypes.DWORD()

        success = kernel32.ReadFile(
            self.handle,
            buffer,
            size,
            ctypes.byref(bytes_read),
            None
        )

        if not success:
            raise OSError("Error leyendo el dispositivo.")

        return buffer.raw[:bytes_read.value]

    def read_sector(self, sector=0):

        self.seek(sector * 512)

        return self.read(512)