class Tower: 
    
    def __init__(self) -> str:
        total_rings = int(input('How many rings are there? '))
        self.total_rings: int = total_rings
        self.pole: dict = {
            'A' : [],
            'B' : [],
            'C' : [],
            }

        self.original = [] # The desired position of rings

        for i in range(self.total_rings):
            self.pole['A'].insert(0,i+1) #insert(index to be inserted at, element)
            (self.original).insert(0,i+1)
        self.display()
            

    def display(self) -> None:
        print()
        print('A ', self.pole['A'])
        print('B ', self.pole['B'])
        print('C ', self.pole['C'])
        print()

    def move_ring(self, move_from, move_to) -> str:
            """move a ring from one position to another with an origin and a destination"""

            self.move_from = move_from
            self.move_to = move_to

            if len(self.pole[move_from]) == 0:
                ring = self.pole[move_from][0]
            else:
                ring = self.pole[self.move_from][-1]

            # Exceptions
            if len(self.pole[move_to])!= 0 and ring > self.pole[move_to][-1]:
                print('The ring you asked to move is BIGGER than the last ring on the destination pole, try again')
            else:    
                self.pole[move_from].pop()
                self.pole[move_to].append(ring)

    def autoplay(self, rings: int, source: str, destination: str, auxilary: str) -> None:
        self.rings = rings
        self.source = source
        self.destination = destination
        self.auxilary = auxilary

        if rings == 1:
            self.move_ring(source, destination)
            self.display()
        else:
            index = self.pole[source].index(rings)
            top_disk = self.pole[source][index + 1]
            
            self.autoplay(top_disk, source, auxilary, destination)
            self.move_ring(source, destination)
            self.display()
            self.autoplay(top_disk, auxilary, destination, source)



    def execute(self) -> str:
        """Initiate the game """
        if input("Do you want to help? (Y/N) ") == "Y":
                self.autoplay(self.total_rings,'A', 'C', 'B')
        else:
            pass
        while True:
            if self.original == self.pole['C']:
                print("\n"'Congratulations! You solved it!'"\n")
                break 
            else:
                Start.move_ring(str(input('From which pole? ')), str(input('To which pole? ')))
                self.display()
           
Start = Tower()
Start.execute()