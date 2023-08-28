import gdown

class DownloadTxtFile:
    def __init__(self):
        self.txt_file_url = 'https://drive.google.com/file/d/11348ecXmcTVhi66Fv4PmvDPYNNX1-aSb/view?usp=drive_link'
        self.txt_output_file = 'data/url_data.txt'
        self.txt_fileId = self.getFileID()
     
    def getFileID(self):
        try:
            if "drive.google.com" in self.txt_file_url:
                file_id = self.txt_file_url.split("/")[-2]
                return file_id
        except:
             return print('No Internet Connection or Something went wrong')
    
    def downloadFile(self):
            download_link= f'https://drive.google.com/uc?id={self.txt_fileId}'
            return gdown.download(download_link, self.txt_output_file, quiet=False)

class DownloadCSVFile(DownloadTxtFile):
    def __init__(self):
        super().__init__()
        self.csv_file_Id = self.getCsvFileId()

    def getCsvFileId(self):
        self.downloadFile()
        path = self.txt_output_file
        with open(path,'r') as txtFile:
             fileId = txtFile.read()
        return fileId

    def downloadCSVFile(self):
            download_link= f'https://drive.google.com/uc?id={self.getCsvFileId()}'
            return gdown.download(download_link, 'data/new_data.csv', quiet=False)

     


