# 123 - RECIPE APP final project
**README FILE**
Lets try to follow some coding conventions to keep our code readable and easy to make changes to because we're collaborating
1. Let's have different UI screens be different files, in each file we can include the backend and the frontend,
    we could also separate the ui files from the backend files.
2. Make sure your variable names are descriptive (don't use 1 letter variables or abbreviations).
       _example:_
      ** DONT:** a, b, c, SOP, totPri
      ** DO:** someValue1, some_Value2, SumOfPrices, totalPrice
4. If the logic in this part is complicated, try to add comments that can make it understandable.
5. Try to follow the Open/Close Principle as much as posible to make our code easy to expand and change
       _basically:_
       - Make a class for every major item that can have multiple variations (ingredients, recipes, filters, etc.)
       - When making class variables, make them private so we don't accidentally make unecessary value changes
           _example:_
           class Recipe:
               def __init__(self, something):
                   self.__something = something
                   ^^^^^^^^^^^^^^^^ make the item private
               def getSomething():
                   return self.__something
                   ^^^^^^^^^^^^^^^^^^^^^^^ as seen here, we make a method to return the item instead of returning the item directly.
