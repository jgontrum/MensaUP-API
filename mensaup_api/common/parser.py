import re
import urllib.request as ur

from bs4 import BeautifulSoup

from mensaup_api import options
from mensaup_api.common.ingredients import Ingredients


class MensaParser(object):
    ingredients_pattern = re.compile(r'\d{1,2}|[A-Z]{1,2}(?=\))')
    ingredients_lookup = options()['ingredientsMapping']

    def __init__(self, mensa: str):
        self.url = options()['mensas'][mensa]['url']
        self.name = options()['mensas'][mensa]['mensa']
        self.name = options()['mensas'][mensa]['mensa']

    @staticmethod
    def clean(text: str) -> str:
        """
        Remove stuff that could be in the text.
        """
        new = text.replace("\r", "")
        new = new.replace("\t", "")
        new = new.replace("\n", "")
        new = new.replace("- ", "-")
        new = new.replace(",", ", ")

        new = new.replace("  ", " ")
        new = new.replace("  ", " ")
        new = new.replace("  ", " ")

        return new

    def check_page(self) -> list:
        page = BeautifulSoup(ur.urlopen(self.url).read(), "html.parser")

        table = page.find("table", attrs={"class": "bill_of_fare"})

        if not table:
            return []

        titles = []
        ingredients = []
        texts = []
        for row in table.find_all('tr'):
            for cell in row.find_all('td'):
                if 'class' in cell.attrs:
                    for cell_class in cell['class']:
                        if cell_class == 'head':
                            titles.append(cell.text)
                        elif 'text' in cell_class:
                            texts.append(self.clean(cell.text))
                        elif 'label' in cell_class:
                            ingredients_store = Ingredients()
                            for i in re.findall(
                                    self.ingredients_pattern, cell.text):
                                if i in self.ingredients_lookup:
                                    ingredients_store.contains(
                                        self.ingredients_lookup[i])

                            for img in cell.find_all("img"):
                                image_url = img.attrs['src']
                                if "hahn" in image_url:
                                    ingredients_store.contains_chicken()
                                elif "mais.png" in image_url:
                                    ingredients_store.contains_vegetarian()
                                elif "sau" in image_url:
                                    ingredients_store.contains_pork()
                                elif "kuh" in image_url:
                                    ingredients_store.contains_beef()
                                elif "fisch" in image_url:
                                    ingredients_store.contains_fish()
                                elif "lamm" in image_url:
                                    ingredients_store.contains_lamb()
                                elif "mais2" in image_url:
                                    ingredients_store.contains_vegan()
                                elif "vital" in image_url:
                                    ingredients_store.contains_vital()

                            ingredients.append(ingredients_store)

        assert len(titles) == len(texts) == len(ingredients)

        list_of_offers = []
        for title, text, ingredient in zip(titles, texts, ingredients):
            if text:
                list_of_offers.append({
                    "category": title,
                    "text": text,
                    "ingredients": ingredient.get_ingredients(),
                    "diets": ingredient.get_diets(),
                })

        return list_of_offers
