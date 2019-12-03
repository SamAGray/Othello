import numpy as np
import types
from abc import ABC, abstractmethod 

# Possible directions to move on the board
DIRECTIONS = [[0, 1], [1, 1], [1, 0], [1, -1],\
     [0, -1], [-1, -1], [-1, 0], [-1, 1]]

BOARD_SIZE = 8


class Player(ABC):
    @abstractmethod
    def get_move(self, board: np.ndarray,options) -> np.array:
        pass

class ManualPlayer(Player):
    def __init__(self,name: str):
        super().__init__()
        self.name =  name


    def get_move(self,board,options):
        x = 0
        y = 0
        goodInput = False
        while(not goodInput):
            self.print_board(board,options)
            res = input( \
                "{}, where would you like to move (x ==> [0,7], y ==> [0,7])?: ".format(self.name))
            print(res)

            try:
                x = int(res[0])
                y = int(res[2])
                res = [x,y]
                if (type(res) is str and x < BOARD_SIZE and y < BOARD_SIZE and len(res)==3, res in options):
                    goodInput = True
                else:
                    print("Bad move 1")
            except:
                print("Bad move 2")

        return res

    @staticmethod
    def print_board(board,options):

        print("   ",end="")
        for cols in range(len(board)):
            print(str(cols),end= " ")
        print()
        print("   ",end="")
        print("-"*15)

        for rows in range(len(board)):
            print(str(rows),end =" | ")
            for cols in range(len(board)):
                if([rows,cols] in np.array(options).tolist()):
                    print("X", end=" ")
                else:
                    print(str(board[rows,cols]),end=" ")
            print()


class Othello(object):
    def __init__(self,player1: Player = ManualPlayer("P1"),\
        player2: Player = ManualPlayer("P2")):
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

        self.players = []
        self.players.append(player1)
        self.players.append(player2)
        self.turn = 1
        self.count = 0
    
    def get_valid_moves(self):
        """
        Gets the moves possible by the current player
        
        returns an array of all the possible moves
        """
        validMoves = []

        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                print("{} {}".format(x,y))
                pos = np.array([x,y])
                if self.board[pos[0],pos[1]] == 0:
                    if(self.update_board(pos,_testing=True)):
                        validMoves.append(pos)

        return validMoves

    def in_board(self,pos : np.ndarray) -> bool:
        """
        Determines whether this position is on the board
        """
        if 0 > pos[0]  or pos[0] >= BOARD_SIZE:
            return False
        if 0 > pos[1]  or pos[1] >= BOARD_SIZE:
            return False

        return True

    def update_direction(self, move : np.ndarray, direction: np.ndarray):
        """
        Helper Method for update_board
        Updates the board in a specific direction:
        """
        pos = move.copy()
        pos += direction 
        while(self.in_board(pos)):
            if self.board[pos[0],pos[1]] == self.turn:
                pos -= direction
                while((pos != move).any()):
                    print("Here77")
                    self.board[pos[0], pos[1]] = self.turn
                    self.count += 1
                    pos -= direction
                break

            elif self.board[pos[0],pos[1]] == 0:
                break
            else:
                pos += direction
            print(pos)

    def update_board(self,move, _testing : bool = True ) -> bool :
        """
        Used to update the board with a player's move
        
        move: array representing the player's move

        returns False if move was invalid
        returns True if the move is valid

        """

        temp = self.board.copy()
        self.count = 0

        for direction in DIRECTIONS:
            self.update_direction(move,direction)

        if self.count == 0:
            self.board = temp
            return False
        else:
            if _testing:
                self.board = temp
                return True
    
    def gameCount(self):
        p1Count = 0
        p2Count = 0

        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if self.board[x,y] == 1:
                    p1Count += 1
                elif self.board[x,y] == 2:
                    p2Count += 1

        return([p1Count,p2Count])

    
    def run(self):
        """
        Runs the Othello Game
        """
        noMove = 0
        while(noMove < 2):
            print("Here")
            options = self.get_valid_moves()
            print(options)
            if len(options) > 0:
                res = False
                while(not res):
                    move = self.players[self.turn-1].get_move(self.board.copy(),options.copy())
                    res = self.update_board()
            else:
                noMove += 1

            self.turn = (self.turn * 2 ) % 3  # 1 --> 2  2 --> 1
        return self.gameCount()



if __name__ == "__main__":
    game = Othello()
    print(game.run())
