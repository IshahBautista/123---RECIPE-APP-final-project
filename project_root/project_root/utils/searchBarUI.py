import flet as ft 
from flet import *
from config import json_path, recipes_data

class Trie:
    class TrieNode:
        def __init__(self):
            self.child = [None] * 26
            self.word_end = False
            self.word = None  # Store the complete word at the end node
    
    def insert_key(root, key):
        currentnode = root

        # Iterate across the length of the string
        for currentkey in key:
            # Check if the letter is already in the tree
            index = ord(currentkey) - ord('a')
            if currentnode.child[index] is None: 
                new_node = Trie.TrieNode() #if does not exist yet, make new node
                # Keep the reference for the newly created node
                currentnode.child[index] = new_node

            currentnode = currentnode.child[index]

        currentnode.word_end = True #indicate it is end of the word (lowest child of the tree)
        currentnode.word = key  #store the complete word

    def search_key(root, key):
        currentnode = root

        for currentkey in key:
            index = ord(currentkey) - ord('a')
            if currentnode.child[index] is None:
                return False

            currentnode = currentnode.child[index]

        return currentnode.word_end #true if word exists and marks ending

    #returns all the preprocessed words from a given node
    def search_prefix(root, prefix):
        curr = root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.child[index] is None:
                return []  # No words found with this prefix
            curr = curr.child[index]
        
        # Collect all words starting from the current node
        results = []
        Trie.collect_words(curr, results)
        return results
    
    def collect_words(node, results):
        if node.word_end:
            results.append(node.word)
        for child in node.child:
            if child:
                Trie.collect_words(child, results)

#HELPER METHODS ______________________________________________________
#for pre processing the words to lowercase and remove the space
def pre_process(key):
    if key is None:
        return ""
    return ''.join(char for char in key.lower() if char.isalpha())

#for getting the specific recipe based on the obtained name
def search_recipe(name):
    for recipe in recipes_data:
            if recipe["preprocessedname"] == name:
                return recipe

#class that returns the search results based on some prefix input in the search bar
class SearchResults:
    def __init__(self):
        self.__preProcessedNameList = [recipe['preprocessedname'] for recipe in recipes_data]
        self.__root = Trie.TrieNode() #create the node here
        self.__searchKey = None #currently empty but will be replaced later
        self.storeRecipesinTrie()

    def setSearchKey(self, key):
        self.__searchKey = key

    def storeRecipesinTrie(self):
        self.__preProcessedNameList = [recipe['preprocessedname'] for recipe in recipes_data]
        for preProcessedName in self.__preProcessedNameList:
            Trie.insert_key(self.__root, preProcessedName) #add the word's letters into the trie

    def getResultsfromPrefix(self):
        preProcessedPrefix = pre_process(self.__searchKey)
        print(f"Prefix: {preProcessedPrefix}")
        resultsList = Trie.search_prefix(self.__root, preProcessedPrefix)
        
        NameList = []
        for result in resultsList:
            foundRecipe = search_recipe(result)
            if foundRecipe is not None and result == foundRecipe['preprocessedname']:
                NameList.append(foundRecipe)
        return NameList

    def findRecipes(self):
        return self.getResultsfromPrefix()

#This class is the search bar itself
#It is connected to the display class and is dependent on it
class CustomSearchBar(ft.UserControl):
    def __init__(self, recipeList, display, filterList):
        super().__init__()
        self.anchor = None  
        self.recipeListReturn = []
        self.filterList = filterList
        self.__recipeList = recipeList #this is the mutable object 
        self.__display = display

    def printRecipeList(self):
            for specificRecipe in self.recipeListReturn:
                print(f"Name: {specificRecipe['name']}")
    
    def build(self):
        searchresults = SearchResults() #an object that is used to find search results

        def handle_change(e: ControlEvent):
            searchresults.setSearchKey(e.data)
            print(f"handle_change e.data: {e.data}")
            self.recipeListReturn = searchresults.findRecipes() #find the recipes based on input text
            self.__recipeList["value"] = self.recipeListReturn #update the mutable object's contents
            self.__display.updateRecipeCards(self.__recipeList) #update the recipe card in the passed display
            self.printRecipeList()

        self.anchor = ft.SearchBar(
            view_elevation=4,
            divider_color=ft.colors.AMBER,
            bar_hint_text="Search Recipes...",
            view_hint_text="Choose a Recipe...",
            on_change=handle_change,
            bar_leading=ft.IconButton(icon="search"),
            controls=[],
            width=400,
        )

        return self.anchor

