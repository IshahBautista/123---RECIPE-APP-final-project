from config import json_path, recipes_data

class OriginFilter:
    def __init__(self):
        #Create a dictionary to store origins as keys and their corresponding indices as values
        self.origin_dict = {}
        self.initTable()

    def initTable(self):
        #Make origins as the keys and indices of the json file as the values
        for index in range(len(recipes_data)):  #Iterate through the file and add elements to the table
            origin = recipes_data[index]["origin"]
            if origin not in self.origin_dict:
                self.origin_dict[origin] = []
            self.origin_dict[origin].append(index)

    def filter(self, filterList):
        finalIndexList = []
        for filterItem in filterList:
            finalIndexList.append(self.origin_dict.get(filterItem, []))  #Get the indices list from dict

        obtainedNamesList = []

        for typeList in finalIndexList:
            for item in typeList:
                obtainedNamesList.append(recipes_data[item]["preprocessedname"])

        return obtainedNamesList
