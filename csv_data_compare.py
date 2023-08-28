import pandas

class CSVCompare:
    def __init__(self):
        self.main_file = 'data/data.csv'
        self.new_file = 'data/new_data.csv'
        self.checkColumn = 'id'

    def read_csv(self, csv_path, encoding ='utf-8'):
        return pandas.read_csv(csv_path, encoding = encoding)
    
    def newItems(self):
        main_csv_data = self.read_csv(self.main_file, encoding='utf-8')
        new_csv_data = self.read_csv(self.new_file, encoding='utf-8')
        new_rows = new_csv_data[~new_csv_data[self.checkColumn].isin(main_csv_data[self.checkColumn])]
        newItemsList = []
        for index, row in new_rows.iterrows():
            newItemsList.append(str(row[self.checkColumn]) + '.jpg')
        return newItemsList, new_rows

    
    def compareAndUpdateCSV(self):
        newitems = self.newItems()
        main_csv_data = self.read_csv(self.main_file, encoding='utf-8')
        if not newitems[1].empty:
            update_data = pandas.concat([main_csv_data, newitems[1]], ignore_index=True)
            update_data.to_csv(self.main_file, index=False)
            return 'New Data Updated'
        else:
            return 'Nothing for Update'

    