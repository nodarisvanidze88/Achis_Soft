import os
import pickle
import gdown
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from csv_data_compare import CSVCompare

# Class gets all files from google drive path and compares with local images, if some images are missing in local new images will downloaded from google drive
class ImageCompareAndDownload:
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
        self.creds = None
        self.image_folder_path = 'data/images/'
        self.image_folder_id = '1j2yxZ972Jf1r5B-FQE06Up74UcL2Sm-1'

    # create token
    def loadOrCreateCreditionals(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)
    # create google service
    def createGoogleDriveApiService(self):
        self.loadOrCreateCreditionals()
        service = build('drive', 'v3', credentials=self.creds)
        return service
    
    # get local image list
    def getLocalImageList(self):
        return [file for file in os.listdir(self.image_folder_path) if os.path.isfile(os.path.join(self.image_folder_path, file))]
    
    # get google drive image list with id and name
    def getGoogleDriveImages(self):
        service = self.createGoogleDriveApiService()
        results = service.files().list(
            q=f"'{self.image_folder_id}' in parents",
            fields="files(id, name)").execute()
        drive_files = results.get('files', [])
        return drive_files
    
    # compare and download images
    def compareAndDownloadImages(self):
        imageList = self.getLocalImageList()
        googleImageList = self.getGoogleDriveImages()
        for imageItems in googleImageList:
            if imageItems['name'] not in imageList:
                download_url = f"https://drive.google.com/uc?id={imageItems['id']}"
                download_path = f"{self.image_folder_path}{imageItems['name']}"
                gdown.download(download_url, download_path)
            else:
                print(f"File {imageItems['name']} not found on Google Drive.")

# Second version of Class gets missing images depend on new data from csv and download only those images
class ImageCompareAndDownloadV2:
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
        self.creds = None
        self.image_folder_path = 'data/images/'
        self.image_folder_id = '1j2yxZ972Jf1r5B-FQE06Up74UcL2Sm-1'

    def loadOrCreateCreditionals(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

    def createGoogleDriveApiService(self):
        self.loadOrCreateCreditionals()
        service = build('drive', 'v3', credentials=self.creds)
        return service
    
    def getLocalImageList(self):
        return [file for file in os.listdir(self.image_folder_path) if os.path.isfile(os.path.join(self.image_folder_path, file))]
    
    def getGoogleDriveImages(self):
        service = self.createGoogleDriveApiService()
        results = service.files().list(
            q=f"'{self.image_folder_id}' in parents",
            fields="files(id, name)").execute()
        drive_files = results.get('files', [])
        return drive_files

    def compareAndDownloadImagesNew(self):
        missingImageList = CSVCompare().newItems()
        googleImageList = self.getGoogleDriveImages()
        print(missingImageList[0])
        for imageItems in googleImageList:
            if imageItems['name'] in missingImageList[0]:
                download_url = f"https://drive.google.com/uc?id={imageItems['id']}"
                download_path = f"{self.image_folder_path}{imageItems['name']}"
                gdown.download(download_url, download_path)


