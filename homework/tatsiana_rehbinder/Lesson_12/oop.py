class Flower:
    def __init__(self, name, color, stem_length, price, life_time):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.life_time = life_time

    def __repr__(self):
        return f"{self.color} {self.name} ({self.stem_length}, {self.price}, {self.life_time}g)"


class Rose(Flower):
    def __init__(self, color, stem_length, price, life_time):
        super().__init__("rose", color, stem_length, price, life_time)


class Tulip(Flower):
    def __init__(self, color, stem_length, price, life_time):
        super().__init__("tulip", color, stem_length, price, life_time)


class Lily(Flower):
    def __init__(self, color, stem_length, price, life_time):
        super().__init__("lily", color, stem_length, price, life_time)


class Bouquet:
    def __init__(self, flowers=None):
        self.flowers = flowers if flowers else []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_price(self):
        return sum(f.price for f in self.flowers)

    def get_wilt_time(self):
        if not self.flowers:
            return 0
        return sum(f.life_time for f in self.flowers) / len(self.flowers)

    def sort_by(self, parameter):
        if parameter == "price":
            self.flowers.sort(key=lambda f: f.price)
        elif parameter == "life":
            self.flowers.sort(key=lambda f: f.life_time)
        elif parameter == "color":
            self.flowers.sort(key=lambda f: f.color)
        elif parameter == "stem":
            self.flowers.sort(key=lambda f: f.stem_length)

    def search_by_life(self, min_life):
        return [f for f in self.flowers if f.life_time >= min_life]
