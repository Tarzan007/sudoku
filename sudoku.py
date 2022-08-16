from enum import Enum
import numpy as np


class Sudoku:
    
    def __init__(self):
        self.board = []
        self.curAction = self.Action.ADD
        self.curSelect = None
        
        pass
    
    def onClick(self, table):
        pass
        
    
    def delete(self):
        pass
    
    def add(self, ):
        pass
    
    def undo(self):
        pass
    
    class Action(Enum):
        ADD = 1
        ERASE = 2
        NOTES = 3
        
     
    
    class Table:
        def __init__(self, tablePos):
            # Keep track of the position of the table in sudoku
            self.tablePos = tablePos
            # Keeping track of each block on the table row by row
            self.board = []
            # Filling each row with a block
            for i in range(len(9)):
                self.board.append(self.Block(i))
    
    
    class Block:
        def __init__(self, blockPos, locked, value):
            # Keep track if the block can be changed
            self.locked = locked
            # Keep track of the value in the clock
            self.value = value
            # Keeping track of the notes on the block 
            self.notes = [0 for x in range(len(9))]
            self.blockPos = blockPos
            
            
if __name__ == '__main__':
    pass