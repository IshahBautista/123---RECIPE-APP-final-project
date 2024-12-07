from utils.filtersView import FilterType
from services.filters.originFilterBackend import OriginFilter
from services.filters.difficultyFilterBackend import DifficultyFilter
from services.filters.preptimeFilterBackend import PrepTimeFilter

class filterReceiver:
    def __init__(self, activefilterlist, recipeList, filteredlist, display):
        self.recipeList = recipeList #is mutable
        self.activefilterlist = activefilterlist #is mutable
        self.filteredlist = filteredlist
        self._display = display
        self.originfilter = OriginFilter()
        self.difficultyfilter = DifficultyFilter()
        self.prepTimeFilter = PrepTimeFilter()
        pass
    
    def printRecipeList(self):
        for specificrecipe in self.recipeList['value']:
            print(f"list: {specificrecipe['preprocessedname']}")

    def getPreProcessedList(self):
        preProcessedNameList = [item['preprocessedname'] for item in self.recipeList['value']]
        return preProcessedNameList

    #for pressing the chips
    def appendOrigin(self, chipname):
        self.activefilterlist["origin"].append(chipname)
        print(f"ACTIVE: {self.activefilterlist['origin']}")
        obtainedNameList = self.originfilter.filter(self.activefilterlist['origin'])
        self.filteredlist['originrecipes']  = obtainedNameList
        self._display.updateRecipeCards(self.recipeList)

    def appendDifficulty(self, chipname):
        self.activefilterlist["difficulty"].append(chipname)
        print(f"ACTIVE: {self.activefilterlist['difficulty']}")
        obtainedNameList = self.difficultyfilter.filter(self.activefilterlist['difficulty'])
        self.filteredlist['difficultyrecipes']  = obtainedNameList
        self._display.updateRecipeCards(self.recipeList)

    def appendActiveFilter(self, chipname:str, filterType:FilterType):
        if filterType.getfilterName() == "Origin":
            self.appendOrigin(chipname)

        elif filterType.getfilterName() == "Difficulty":
            self.appendDifficulty(chipname)

    def setPrepTimeFilter(self, value):
        if value == None: #if the filter has been changed to nothing
            return

        self.activefilterlist['preptime'] = value
        obtainedNameList = self.prepTimeFilter.filter(self.activefilterlist['preptime'])
        self.filteredlist['preptimerecipes'] = obtainedNameList
        print(f"LIST: {self.filteredlist['preptimerecipes']}")
        self._display.updateRecipeCards(self.recipeList)

    #for unpressing the chips
    def removeOrigin(self, chipname):
        self.activefilterlist["origin"].remove(chipname)
        obtainedNameList = self.originfilter.filter(self.activefilterlist['origin'])
        self.filteredlist['originrecipes']  = obtainedNameList
        self._display.updateRecipeCards(self.recipeList)

    def removeDifficulty(self, chipname):
        self.activefilterlist["difficulty"].remove(chipname)
        obtainedNameList = self.difficultyfilter.filter(self.activefilterlist['difficulty'])
        self.filteredlist['difficultyrecipes']  = obtainedNameList
        self._display.updateRecipeCards(self.recipeList)

    def removeActive(self, chipname:str, filterType:FilterType):
        if filterType.getfilterName() == "Origin":
            self.removeOrigin(chipname)

        elif filterType.getfilterName() == "Difficulty":
            self.removeDifficulty(chipname)
