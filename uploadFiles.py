import dropbox
import os

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
                
        

def main():
    accessToken = "4-TL-JmilSwAAAAAAAAAAaC_F2fy7ew8xlWC4I3d21RbRY7pSj9KwnDoYn9mVn7A"
    transferData = TransferData(accessToken)
    file_from = input("Enter file path to transfer: ")
    file_to = input("Enter the file name you wanted created: ")
    transferData.upload_files(file_from, file_to)
    print("Files have been moved.")

main()