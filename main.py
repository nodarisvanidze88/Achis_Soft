from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from data_download import DownloadCsvFile
from csv_data_compare import CSVCompare

class MyBoxLayout(BoxLayout):    
    def btnb(self):
        url = 'https://drive.google.com/file/d/1gYfY1FBT3iKExEAYVCC0xk-wHdLpZRPd/view?usp=drive_link'
        out_path = 'data/new_data.csv'
        first_file='data/data.csv'
        second_file='data/new_data.csv'
        col = 'id' 
        func = DownloadCsvFile(url, out_path)
        func.downloadFile()
        func.convertCSVFile()
        create_function = CSVCompare(first_file, second_file, col)
        create_function.compareAndUpdateCSV()

class MyApp(App): 
    def build(self):
        return MyBoxLayout()
    

if __name__ =="__main__":
    MyApp().run()