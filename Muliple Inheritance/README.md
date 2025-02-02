Execute One

```py
class PlantKingdom:
    def __init__(self):
        #The use of Super is essential
        super().__init__()
        self.species_kingdom = "Plant Kindom"

class Hydrophyte:
    def __init__(self):
        #The use of Super is essential
        super().__init__()
        self.habitat = "Aquatic or Water living"


class Lily(PlantKingdom,Hydrophyte):
    def __init__(self):
        super().__init__()
    
    def printprops(self):
        print(f"Kingdom : {self.species_kingdom}")
        print(f"Habitat : {self.habitat}")
        return

lil = Lily()
lil.printprops()
```

Outcome
![alt text](image.png)