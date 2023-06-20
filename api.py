import requests


class SuperHeroes:
    def __init__(self, url: str):
        self.url = url
        self.heroes = None

    def get_request(self):
        """ Отправить get запрос на ссылку и сохранить героев в self.heroes"""
        response = requests.get(self.url)
        self.heroes = response.json()

    def find_heroes(self, name):
        """Показать самую полезную информацию о герое (powerstats)
           И плюс загружать его фотографию в папку с героями"""
        for i in self.heroes:
            if name == hero["name"]:
                print(hero)


    def find_best_hero(self, heroes_list: list, power_state: str) -> str:
        """ heroes_list = ['Ant-Man', 'Spider-Man', 'Aquaman']
            power_state = 'intelligence'
            -> 'Ant-Man, intelligence = 80
        """
        pass


superheroes = SuperHeroes(url="https://cdn.jsdelivr.net/gh/akabab/"
                              "superhero-api@0.3.0/api/all.json")
superheroes.get_request()
superheroes.find_heroes(name="Ant-Man")
