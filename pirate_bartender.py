import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

#If preference in ingredients is true
#select ingreient randomly
#add ingredient to list



#Takes in a list of questions and stores preferences in dict preferences
def askquestion (questionlist):
    preferences = {}
    for question in questionlist:
        print(questionlist[question])
        preference = input()
        if preference == "yes" or preference == "y":
            preferences[question] = True
        elif preference == "no" or preference =="n":
            preferences[question] = False
        else: 
            preference = input("Please answer yes or no")
    return preferences

def makeDrink (preferenceList):
    drink = []
    for ingredient in preferenceList:
        if preferenceList[ingredient] == True:
            drink.append(random.choice(ingredients[ingredient]))
    return drink

#main
if __name__ == '__main__':
    userPreferences = askquestion(questions)
    drink = makeDrink(userPreferences)
    print ("here's your drink! It has a: ")
    print (*drink, sep = ", ")
    #print ("here's your drink! It has a {} and {}.".format(*drink))