class Pokemon:
    def __init__(self,new_name,new_weight,new_height,new_food,new_cp):
        self.__name=new_name
        self.__weight=new_weight
        self.__height=new_height
        self.__food=new_food
        self.__cp=new_cp
    def eat(self):
        print(f'The pokemon is eating {self.__food}.')
    def make_noice(self):
        print('The pokemon wow wow wow!')
    def get_name(self):
        return self

class Pikachu(Pokemon):
    def
