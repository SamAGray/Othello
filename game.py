import numpy as np


# Possible directions to move on the board
DIRECTIONS = [[0, 1], [1, 1], [1, 0], [1, -1],\
     [0, -1], [-1, -1], [-1, 0], [-1, 1]]

BOARD_SIZE = 8

class Othello(object):
    def __init__(self,player1 = ManualPlayer(),player2 = manualPlayer()):
        """
        Othello Game

        Runs a game of Othello

        player1: player1 type
        player2: player2 type

        self.board: An 8,8 grid (0 is no player), 1 p1, 2 p2
        self.turn: The current player
        self.count: The number of tokens turned in the last move
        """

        self.board = np.zeros((BOARD_SIZE,BOARD_SIZE)\
            ,dtype=np.int8)
        self.board[3,3] = '2'
        self.board[4,4] = '2'
        self.board[3,4] = '1'
        self.board[4,3] = '1' 

        self.p1 = player1
        self.p2 = player2
        self.turn = 1
        self.count = 0
    
    def getValidMoves(self):
        """
        Gets the moves possible by the current player
        
        returns an array of all the possible moves
        """
        validMoves = []:

        for i in range(8):
            for y in range(8):
                pos = [x,y]
                if self.board[pos] = 0:
                    if(update_board(pos),__testing=True):
                        validMoves.append(pos)

        return validMoves

    def in_board(pos):
        """
        Determines whether this position is on the board
        """
        if 0 > pos[0]  or pos[0] < BOARD_SIZE
            return False
        if 0 > pos[1]  or pos[1] < BOARD_SIZE
            return False

        return True

    def update_direction(self, move, direction):
        """
        Helper Method for update_board
        Updates the board in a specific direction:
        """
        pos = move
        pos += direction 
        while(in_board(pos))
            if board[pos] == self.turn:
                pos -= direction
                while(pos != move):
                    board[pos] = self.turn
                    self.count += 1
            if board[pos] == 0
                break

    def update_board(self,move, __testing = True):
        """
        Used to update the board with a player's move
        
        move: array representing the player's move

        returns False if move was invalid
        returns True if the move is valid

        """

        temp = self.board.copy()
        self.count = 0

        for direction in DIRECTIONS
            self.update_direction(move,direction)

        if count == 0:
            self.board = temp
            return False
        else:
            if __testing:
            self.board = temp
            return True

def print_board(self):
    print '\n'.join(' '.join(str(cell) for cell in row) for row in self.board)
