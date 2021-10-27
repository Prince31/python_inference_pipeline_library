import csv

class Utility:

    def load_csv(self, file_name):
        '''
        Loads a csv file

        Argument:
        file_name (str): Name of csv file to load

        Return:
        row[0] (str)
        '''
        with open(file_name) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                return row[0]
