from core.disk import Disk
import wmi


class DiskScanner:

    def scan(self):

        c = wmi.WMI()

        disks = []

        for index, disk in enumerate(c.Win32_DiskDrive()):

            size = int(disk.Size) if disk.Size else 0

            sectors = 0

            try:
                sectors = size // 512
            except:
                pass

            disks.append(
    Disk(
        index=index,
        model=disk.Model,
        size=size,
        interface=disk.InterfaceType,
        serial=getattr(disk, "SerialNumber", ""),
        manufacturer=getattr(disk, "Manufacturer", ""),
        partitions=getattr(disk, "Partitions", 0),
        deviceid=disk.DeviceID,
        sectors=sectors,
    )
)

            })

        return disks