import pandas

class CSVCompare:
    def __init__(self, main_file, new_file,checkColumn):
        self.main_file = main_file
        self.new_file = new_file
        self.checkColumn = checkColumn

        

    def read_csv(self, csv_path, encoding ='utf-8'):
        return pandas.read_csv(csv_path, encoding = encoding)
    
    def compareAndUpdateCSV(self):
        main_csv_data = self.read_csv(self.main_file, encoding='utf-8')
        new_csv_data = self.read_csv(self.new_file, encoding='utf-8')
        new_rows = new_csv_data[~new_csv_data[self.checkColumn].isin(main_csv_data[self.checkColumn])]
        if not new_rows.empty:
            update_data = pandas.concat([main_csv_data, new_rows], ignore_index=True)
            update_data.to_csv(self.main_file, index=False)
            return 'New Data Updated'
        else:
            return 'Nothing for Update'
        
first_file='data/data.csv'
second_file='data/new_data.csv'
col = 'id'
create_function = CSVCompare(first_file,second_file,col)
print(create_function.compareAndUpdateCSV())