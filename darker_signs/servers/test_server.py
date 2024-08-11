from ..utils import download_file


class TestServer:
    def __init__(self, root_path, mail):
        self.root_path = root_path
        self.mail = mail

    def http(self):
        while True:
            print("Test Server Web\nWelcome, this is a test server")
            print("1) Informations\n2) Files\n3) Who we are\n0) Exit")
            selection = input("Make a selection ")
            if selection not in ["1", "2", "3", "0"]:
                continue
            match selection:
                case "1":
                    print(
                        "Informations\nThis is a very good company doing very good things!"
                    )
                case "2":
                    print("Files")
                    self.__http_files()
                case "3":
                    print(
                        "Who we are\nAs said, this is a very good company doing very good things"
                    )
                case "0":
                    break

    def ssh(self):
        print("ssh")

    def ftp(self):
        print("ftp")

    def __http_files(self):
        while True:
            print("1) 8m.enc\n2) 9m.enc\n0) Go back")
            file_number = input("Make a selection ")
            if file_number not in ["1", "2", "0"]:
                continue
            match file_number:
                case "1":
                    download_file(f"{self.root_path}/8m.enc", "ABCDENC")
                    break
                case "2":
                    download_file(f"{self.root_path}/9m.enc", "ABCDENC")
                    break
                case "0":
                    break
        return
