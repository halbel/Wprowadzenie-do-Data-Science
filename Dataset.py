import csv

class Dataset:
    def __init__(self):
        self.data = []
        self.labels = []

    def load(self,path,header=True):
        self.data = []
        self.labels = []
        
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=";")
            
            if header:
                self.labels = next(reader)  
            
            for row in reader:
                self.data.append(row)
    
    def print_labels(self):
        if self.labels:
            print("Column labels: ")
            for label in self.labels:
                print("-",label)
        else:
            print("Dataset dont have labels")
    
    def print_data(self, start = None, end = None):
        subset = self.data[start:end]
        for i, row in enumerate(subset, start=start or 0):
            print(f"{i}:{row}")

    def split(self,train,test,val):
        
        total = len(self.data)
        if train + test + val != 100:
            return ValueError("train + test + val must be 100") 
        
        train_end = int(total * train /100)
        test_end = train_end + int(total * test /100)

        train_data = self.data[:train_end]
        test_data = self.data[train_end:test_end]
        val_data = self.data[test_end:]

        return train_data, test_data, val_data
    
    def class_count(self,col_index):
        counts={}
        for row in self.data:
            key = row[col_index]
            counts[key] = counts.get(key,0)+1
        for k,v in counts.items():
            print((k,v))

    def print_class_data(self,class_unit,decision_column =-1):
        found = [w for w in self.data if w[decision_column] == class_unit]
        if found:
            for row in found:
                print(row)
        else:
            print(f"Not found data for class:{class_unit}")

    def save_do_csv(self, data_list, file_name):
        try:
            with open(file_name, mode='w', newline='', encoding='utf-8') as plik:
                writer = csv.writer(plik, delimiter=';')
                if self.labels:
                    writer.writerow(self.labels)
                writer.writerows(data_list)
            print(f"Data has been loaded to file {file_name}")
        except Exception as e:
            print(f"An error occured: {e}")

ds = Dataset()
ds.load("student-mat.csv", header=True)
ds.print_labels()
ds.print_data(0, 3)    
train, test, val = ds.split(35, 35, 30)
print(len(train), len(test), len(val))
ds.class_count(-1)
ds.print_class_data("13")
ds.save_do_csv(ds.data, "saved.csv")