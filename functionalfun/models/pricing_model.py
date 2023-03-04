from functionalfun.models.car_model import Car


make_base_prices = {
    "coup": 100,
    "suv" : 199,
    "sedan": 125,
    "super": 220


}


factors = {
    "doors": 25, #Cost per door
    "make" : make_base_prices, #Different base prices for different makes
    "sport": 100 # additional price for sport mode

}


def price_(car: Car):
    print(car.__dict__)
    return None