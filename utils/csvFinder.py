import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
class CsvFinder:
    def __init__(self,csvPath):
        self.csvPath = csvPath
        self.csvData = self.read_data()



    def find_words(self,user_input):

        data = {}
        data_list = []
        for each_dict in self.csvData:
            #print(each_dict)
            freq = (each_dict['ความถี่'])
            freq_permit = ''.join(each_dict['ผู้รับอนุญาต\t\n'].strip())
            data[freq] = freq_permit #manage data csv to dict
        for k,v in data.items():
            if fuzz.ratio(v,user_input) >= 19:
                a = (fuzz.ratio(v,user_input), k, v)
                data_list.append(a)
        return data_list


    def find_freq(self,user_input):

        data = {}
        data_list = []
        found_data = []
        found_data_similar = []

        for each_dict in self.csvData:
            # print(each_dict)
            freq = (each_dict['ความถี่'])
            freq_permit = ''.join(each_dict['ผู้รับอนุญาต\t\n'].strip())
            data[freq] = freq_permit  #manage data csv to dict
        for k, v in data.items():
            if k == user_input: # found frequency
                 a = (k,v)
                 found_data.append((a))
                 return  found_data
            elif fuzz.ratio(k, user_input) >= 55:
                details = k,v   # k = 
                found_data_similar.append(details)
        return(found_data_similar)


    ''' 
    def math_value(self,val_to_match):

        for i,v in self.find_words():
            print(i,v)

    '''








    def read_data(self):  #read csv file
        with open(self.csvPath,encoding="utf-8") as file:
            csvdata = csv.DictReader(file, delimiter=',')
            csvdata = [i for i in csvdata]
            file.close()
            return csvdata












if __name__ == '__main__':
    csv = CsvFinder(csvPath='frq_table.csv')
    #print(csv.math_value("อากาศ"))
    #print(csv.find_words('อากาศ'))
    print(csv.find_freq('108.3'))



   # a =  csv.math_value('อ')
   # print(a)