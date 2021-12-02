class Submarine(object):
    def __init__(self) -> None:
        self.depth = 0
        self.horizontal = 0

    def forward(self, units):
        self.horizontal += int(units)

    def down(self, units):
        self.depth += int(units)

    def up(self, units):
        self.depth -= int(units)

    def command(self,direction,units): 
        if direction == "forward":
            self.forward(units)

        elif direction == "up":
            self.up(units)

        elif direction == "down":
            self.down(units)

        else:
            print("Not a valid direction")

    def get_sum(self):
        return self.depth * self.horizontal

class SubmarineComplex(Submarine):
    def __init__(self) -> None:
        super().__init__()
        self.aim = 0

    def forward(self, units):
        units = int(units)
        self.horizontal += units
        self.depth += (self.aim * units)
        

    def down(self, units):
        units = int(units)
        self.aim += units

    def up(self, units):
        units = int(units)
        self.aim -= units