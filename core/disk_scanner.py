import wmi


class DiskScanner:
    def scan(self):
        c = wmi.WMI()
        disks = []

        for index, disk in enumerate(c.Win32_DiskDrive()):

            size = 0

            if disk.Size:
                size = int(disk.Size)

            disks.append({
                "index": index,
                "model": disk.Model,
                "size": size,
                "interface": disk.InterfaceType,
                "serial": getattr(disk, "SerialNumber", ""),
            })

        return disks
        