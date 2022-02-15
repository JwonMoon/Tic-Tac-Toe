BOARD_SIZE = 3
# players
P1 = 0
P2 = 1
P_NONE = 2
# markers
P1_M = 'O'
P2_M = 'X'
NONE_M = '_'

def getPlayerName(expr):
    if expr == P1 or expr == 'O':
        return 'P1'
    elif expr == P2 or expr == 'X':
        return 'P2'
    elif expr == P_NONE or expr == '_':
        return 'NONE'
    else:
        print("getPlayerName(expr): expr 인자를 잘못 입력하였습니다.", expr)
        return -1

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
    winner = P_NONE
    # 가로 검사
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if BOARD[i][j] == NONE_M:
                break
            elif j == BOARD_SIZE-1:
                winner = BOARD[i][j]
                print("[1] winner:", winner)
                return winner
            elif BOARD[i][j] != BOARD[i][j+1]:
                break

    # 세로 검사
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if BOARD[j][i] == NONE_M:
                break
            elif j == BOARD_SIZE-1:
                    winner = BOARD[j][i]
                    print("[2] winner:", winner)
                    return winner
            elif BOARD[j][i] != BOARD[j+1][i]:
                break
                
    # ↘ 대각선 검사
    for i in range(BOARD_SIZE):
            if BOARD[i][i] == NONE_M:
                break
            elif i == BOARD_SIZE - 1:
                winner = BOARD[i][i]
                print("[3] winner:", winner)
                return winner
            elif BOARD[i][i] != BOARD[i+1][i+1]:
                break

    # ↙ 대각선 검사
    for i in range(BOARD_SIZE):
        if BOARD[i][BOARD_SIZE-i-1] == NONE_M:
            break
        elif i == BOARD_SIZE - 1:
            winner = BOARD[i][BOARD_SIZE-i-1]
            print("[3] winner:", winner)
            return winner
        elif BOARD[i][BOARD_SIZE-i-1] != BOARD[i+1][BOARD_SIZE-i-2]:
            break
    return winner


def inputRowCol(player):
    print("[{} 차례입니다.] (게임종료: 0,0 입력)".format(getPlayerName(player)))
    row = int(input("행 번호: "))
    col = int(input("열 번호: "))
    if(row > BOARD_SIZE or col > BOARD_SIZE or row*col < 0): # 인덱스 범위 검사
        print("번호를 잘못 입력하였습니다.\n")
        return -1, -1
    elif isEmpty(BOARD, row, col) == False: # 마커 중복 검사
        print("빈칸이 아닙니다.\n")
        return -1, -1
    else:
        return row, col

def isEmpty(BOARD, row, col):
    return (BOARD[row-1][col-1] == NONE_M)


def putMarker(player, row, col):
    global BOARD    
    BOARD[row-1][col-1] = getPlayerMark(player)
    return True

if __name__ == "__main__":
    BOARD = initBoard()
    player = P1
    
    while(True):
        print("")
        printBoard(BOARD)
        print("")
        winner = isGameDone(BOARD)  # 승패검사
        if(winner == P_NONE):
            while(True):
                row, col = inputRowCol(player) # 숫자입력 예외 처리
                if(row == 0 and col == 0):
                    print("게임을 종료합니다.\n")
                    exit()
                elif(row != -1 and col != -1):
                    putMarker(player, row, col) # 마커 입력
                    player = (player + 1) % 2   # player 변경
                    break
        else:
            print("@ {} @가 이겼습니다!".format(getPlayerName(winner)))
            break