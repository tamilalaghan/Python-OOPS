#Execute One

class Hotel :
    
    def __init__ (self, name, numOfDay, roomType, price):
        self.name = name
        self.numberOfDay = numOfDay
        self.roomType = roomType
        self.price = price

    def booking_quote(self):
        if hasattr(self,"promo") :
            print(f"You have a promo, the quote price is {(self.price - self.promo) * self.numberOfDay}")  
        else:
            print(f"No promo for the day, the regular quote price is {self.price * self.numberOfDay}")
        return
        
    def set_promo(self,promo):
        self.promo = promo

classic = Hotel("Classic",5,"KingSuite",250)
classic.booking_quote()
classic.set_promo(35)
classic.booking_quote()