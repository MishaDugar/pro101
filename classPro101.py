import dropbox
import os
from dropbox.files import WriteMode
class Transferdata:
    def __init__(self,accesstoken) :
        self.accesstoken=accesstoken

    def uploadfiles(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        for rootfolder,folders,files in os.walk(filefrom):
            for filename in files:
                localpath=os.path.join(rootfolder,filename)
                relpath=os.path.relpath(localpath,filefrom)
                dropboxpath=os.path.join(fileto,relpath)
                with open(localpath,"rb")as f:
                    dbx.files_upload(f.read(),dropboxpath)
                    
                

       
def main():
    accesstoken="_RGtEFeoZ_0AAAAAAAAAAWghg1UCbKW_FhFgI8bi9uoA-xv7oygBt8YF7Lz8HX-9"
    transferdata=Transferdata(accesstoken)

    filefrom="folder1/"
    fileto="folder1/"

    transferdata.uploadfiles(filefrom,fileto)
    print("Transfer successfull")

main()
        