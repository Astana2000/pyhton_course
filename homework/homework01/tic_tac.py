class TicTacGame:
    def __init__(self):
        self.board = {1: [".", ".", "."],
                      2: [".", ".", "."],
                      3: [".", ".", "."]}
        self.players = {"1": "x", "2": "o"}
        self.players_help = {True: "1", False: "2"}
        self.row = 0
        self.column = 0
        self.winner = -1

    def show_board(self):
        for i in range(1, 4):
            print(self.board[i])

    def get_input(self):
        try:
            self.row = int(input("Введите номер строки: "))
            self.column = int(input("Введите номер столбца: "))
            self.validate_input(self.row, self.column)
        except ValueError:
            print("Введите число от 1 до 3!")
            self.get_input()

    def validate_input(self, row, column):
        if 0 < row < 4 and 0 < column < 4:
            if self.board[row][column - 1] != ".":
                print("Эта клетка уже занята")
                self.get_input()
        else:
            print("Введите корректное значение строки и столбца от 1 до 3")
            self.get_input()

    def start_game(self):
        self.board = {1: [".", ".", "."],
                      2: [".", ".", "."],
                      3: [".", ".", "."]}
        print("Игра началась!")
        player = True
        while self.check_winner() is False:
            print("Ход игрока под номером", self.players_help[player])
            self.get_input()
            self.board[self.row][self.column - 1] = self.players[self.players_help[player]]
            self.show_board()
            player = not player
        print("Выиграл игрок под номером ", self.winner)

    def check_winner(self):
        for i in range(1, 4):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != '.':
                # проверка по строкам
                return self.check_who_is_winner(i, 0)
            if self.board[1][i - 1] == self.board[2][i - 1] == self.board[3][i - 1] and self.board[1][i - 1] != '.':
                # проверка по столбцам
                return self.check_who_is_winner(1, i - 1)
        # проверка по диагоналям
        if self.board[1][0] == self.board[2][1] == self.board[3][2] and self.board[1][0] != '.':
            return self.check_who_is_winner(1, 0)
        if self.board[1][2] == self.board[2][1] == self.board[3][0] and self.board[1][2] != '.':
            return self.check_who_is_winner(1, 2)
        return False

    def check_who_is_winner(self, row, column):
        if self.board[row][column] == 'x':
            self.winner = 1
        else:
            self.winner = 2
        return True


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
