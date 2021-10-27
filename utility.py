import csv
import json

class Utility:

    def load_csv(self, file_name):
        '''
        Loads a csv file

        Parameters
        ----------
        file_name (str): Name of csv file to load

        Returns
        -------
        row[0] (str)
        '''
        with open(file_name) as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                result = row[0]
        return result
    
    def load_json(self, filename):
        '''
        Loads a json file

        Argument:
        file_name (str): Name of json file to load

        Return:
        key (str)
        '''   
        with open(filename) as f:
            data = json.load(f) 
        for key in data.keys():
            return key

if __name__ == '__main__':
    output = Utility().load_json("assets/sample.json")
    print(output)