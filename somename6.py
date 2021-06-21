import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = '8-ajywlUQckAAAAAAAAAAXXfL94_4GtDLvAsTs8d_4-qX01rUa7-3EKNqYQGSI3l'
    transferData = TransferData(access_token)

    file_from = input("enter file path")
    file_to =   input("upload path")

    transferData.upload_file(file_from, file_to)
    print("Files have moved.")

main()