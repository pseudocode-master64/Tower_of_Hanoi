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
            """Move one ring from one position to another"""

            if len(self.pole[move_from]) == 0:
                ring = self.pole[move_from][0]
            else:
                ring = self.pole[move_from][-1]

            # Exceptions
            if len(self.pole[move_to])!= 0 and ring > self.pole[move_to][-1]:
                print('The ring you asked to move is BIGGER than the last ring on the destination pole, try again')
            else:    
                self.pole[move_from].pop()
                self.pole[move_to].append(ring)

    def autoplay(self, biggest_ring: int, source: str, destination: str, auxilary: str) -> None:
        """Automatically solve the puzzle + print out each step taken to solve the puzzle"""
        
        if biggest_ring == self.pole[source][-1]: # if the biggest ring is the last ring on the source pole
            self.move_ring(source, destination)
            self.display()
        else:
            index = self.pole[source].index(biggest_ring) # .index(a) returns the index of a within a list
            top_ring: int = self.pole[source][index + 1] # top_ring = The ring on top of biggest_ring
            
            self.autoplay(top_ring, source, auxilary, destination) # destination is changed to auxilary pole
            self.move_ring(source, destination)
            self.display()
            self.autoplay(top_ring, auxilary, destination, source) # auxilary pole is changed to source pole



    def execute(self) -> str:
        """Initiate the game"""

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
