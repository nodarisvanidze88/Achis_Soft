import gdown
import pandas

class DownloadCsvFile:
    def __init__(self, file_url, output_file):
        self.file_url = file_url
        self.output_file = output_file
        self.fileId = self.getFileID()
     
    def getFileID(self):
        try:
            if "drive.google.com" in self.file_url:
                file_id = self.file_url.split("/")[-2]
                return file_id
        except:
             return 'No Internet Connection or Something went wrong'
     
    def downloadFile(self):
            try:
                download_link= f'https://drive.google.com/uc?id={self.fileId}'
                print(gdown.download(download_link, self.output_file, quiet=False))
                return gdown.download(download_link, self.output_file, quiet=False)
            except:
                return 'No Internet Connection or Something went wrong'
    
    def convertCSVFile(self):
         r_file = pandas.read_csv(self.output_file)
         r_file.to_csv(self.output_file, index=False, encoding='utf-8')
         


        

url = 'https://drive.google.com/file/d/1gYfY1FBT3iKExEAYVCC0xk-wHdLpZRPd/view?usp=drive_link'
out_path = 'data/new_data.csv'      
func = DownloadCsvFile(url, out_path)
func.downloadFile()
func.convertCSVFile()