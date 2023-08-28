from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from data_download import DownloadCSVFile
from csv_data_compare import CSVCompare
from images_operation import ImageCompareAndDownloadV2

class MyBoxLayout(BoxLayout):    
    def btnb(self):
        DownloadCSVFile().downloadCSVFile()
        ImageCompareAndDownloadV2().compareAndDownloadImagesNew()
        CSVCompare().compareAndUpdateCSV()
        

        print('all is done')

class MyApp(App): 
    def build(self):
        return MyBoxLayout()
    

if __name__ =="__main__":
    MyApp().run()