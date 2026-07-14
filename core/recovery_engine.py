from core.signatures import FILE_SIGNATURES


class RecoveryEngine:

    def __init__(self):
        self.found_files = []

    def scan_sector(self, sector_data, sector_number):

        for file_type, signatures in FILE_SIGNATURES.items():

            for signature in signatures:

                if sector_data.startswith(signature):

                    self.found_files.append({
                        "type": file_type,
                        "sector": sector_number
                    })

                    return True

        return False

    def get_results(self):
        return self.found_files