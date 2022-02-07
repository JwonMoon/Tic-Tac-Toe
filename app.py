BOARD_SIZE = 3
# players
P1 = 0
P2 = 1
NONE = 2
# markers
P1_M = 'O'
P2_M = 'X'
NONE_M = '_'

def getPlayerName(player):
    if player == P1:
        return 'P1'
    elif player == P2:
        return 'P2'
    else:
        return 'NONE'

def getPlayerMark(player):
    if player == P1:
        return P1_M
    elif player == P2:
        return P2_M
    else:
        return NONE_M
        
def initBoard():
    board = []
    for i in range(BOARD_SIZE):
        none_row = []
        for j in range(BOARD_SIZE):
            none_row.append(NONE_M)
        board.append(none_row)
    return board


def printBoard(BOARD):
    # print index number of column
    for i in range(BOARD_SIZE):
        print("\t[{}]".format(i+1), end="")
    print("")
    # print index number of row & print board
    for i in range(BOARD_SIZE):
        print("[{}]".format(i+1), end="")
        for j in range(BOARD_SIZE):
            print("\t {}".format(BOARD[i][j]), end="")
        print("")


def isGameDone(BOARD):
    winner = NONE
    # 가로 검사
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE-1):
            if BOARD[i][j] != NONE_M and BOARD[i][j] != BOARD[i][j+1]:
                break
            elif j == BOARD_SIZE-1:
                winner = BOARD[i][j]

    # 세로 검사
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE-1):
            if BOARD[j][i] != NONE_M and BOARD[j][i] != BOARD[j+1][i]:
                break
            elif j == BOARD_SIZE-1:
                winner = BOARD[j][i]
                
    # ↘ 대각선 검사
    for i in range(BOARD_SIZE-1):
            if BOARD[i][i] != NONE_M and BOARD[i][i] != BOARD[i+1][i+1]:
                break
            elif i == BOARD_SIZE-1:
                winner = BOARD[i][i]
    # ↙ 대각선 검사
    for i in range(BOARD_SIZE-1, 0):
        if BOARD[i][i] != NONE_M and BOARD[i][i] != BOARD[i-1][i-1]:
            break
        elif i == 1:
            winner = BOARD[i][i]
    
    return winner


def putMarker(player):
    global BOARD
    print("{} 차례입니다.".format(getPlayerName(player)))
    row = int(input("행 번호: "))
    col = int(input("열 번호: "))
    if(row > BOARD_SIZE or col > BOARD_SIZE or row*col < 0):
        print("잘못 입력하였습니다.")
        return False
    BOARD[row-1][col-1] = getPlayerMark(player)
    printBoard(BOARD)
    print("")
    return True

if __name__ == "__main__":
    BOARD = initBoard()
    player = P1
    
    printBoard(BOARD)
    print("")
    while(True):
        winner = isGameDone(BOARD)
        if(winner == NONE):
            while(True):
                if(putMarker(player)):
                    player = (player + 1) % 2   # player 변경
                    break            
        else:
            print("<{}>가 이겼습니다!".format(getPlayerName(winner)))
            break

# 추가할 것
# 1) 승패조건 보완
# 2) 중복 마크 예외처리