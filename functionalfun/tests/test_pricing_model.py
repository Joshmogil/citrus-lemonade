from functionalfun.models import pricing_mode
from functionalfun.models import car_model

def test_price_():
    car =  car_model.Car(
        color="blue",
        make="suv",
        price=None,
        doors=20
        )

    
    assert pricing_mode.price_(car) == None