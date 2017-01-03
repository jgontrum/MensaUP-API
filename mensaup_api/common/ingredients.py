# -*- coding: utf-8 -*-


class Ingredients(object):
    def __init__(self):
        self.ingredient_list = [
            "colouring", "preservative", "antioxidant", "flavour_enhancer", "sulfur", "blackened", "waxed", "phosphate", "sweetener",
            "aspartam", "lactoprotein", "egg_white", "quinine", "caffeine", "milk_powder", "whey_powder", "cocoa",
            "rennet", "alcohol", "gluten", "crustaceans", "eggs", "gelatin", "peanuts", "soy", "milk",
            "edible_nuts", "celeriac", "mustard", "sesame", "sulfite", "lupin", "molluscs", "chicken", "vegetarian",
            "pork", "beef", "fish", "lamb", "vegan", "vital"
        ]
        self.__ingredients = []
        self.__diets = []

    def get_ingredients(self):
        return self.__ingredients

    def get_diets(self):
        if self.is_vegan():
            self.__diets.append("vegan")
        if self.is_vegetarian():
            self.__diets.append("vegetarian")
        if "fish" in self.__ingredients:
            self.__diets.append("fish")
        if "lamb" in self.__ingredients:
            self.__diets.append("lamb")
        if "pork" in self.__ingredients:
            self.__diets.append("pork")
        if "beef" in self.__ingredients:
            self.__diets.append("beef")
        if "chicken" in self.__ingredients:
            self.__diets.append("chicken")
        return self.__diets

    def is_vegan(self):
        bad = ["lactoprotein", "egg_white", "milk_powder", "whey_powder", "rennet", "crustaceans", "eggs", "gelatin",
               "fish", "milk", "molluscs", "chicken", "pork", "beef", "fish", "lamb"]
        if "vegan" in self.__ingredients:
            return True
        for bad_ingredient in bad:
            if bad_ingredient in self.__ingredients:
                return False
        return True

    def is_vegetarian(self):
        bad = ["rennet", "crustaceans", "gelatin", "fish", "molluscs", "chicken", "pork", "beef", "fish", "lamb"]
        if self.is_vegan() or "vegetarian" in self.__ingredients:
            return True
        for bad_ingredient in bad:
            if bad_ingredient in self.__ingredients:
                return False
        return True

    def contains(self, kind):
        self.__ingredients.append(kind)

    def contains_chicken(self):
        self.contains("chicken")

    def contains_vegetarian(self):
        self.contains("vegetarian")

    def contains_pork(self):
        self.contains("pork")

    def contains_beef(self):
        self.contains("beef")

    def contains_fish(self):
        self.contains("fish")

    def contains_lamb(self):
        self.contains("lamb")

    def contains_vegan(self):
        self.contains("vegan")

    def contains_vital(self):
        self.contains("vital")