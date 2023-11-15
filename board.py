class TicTacToeBoard:
    num_rows = 3
    num_cols = 3
    length_to_win = 3

    def __init__(self):
        self.x_set = set()
        self.o_set = set()
        self.x_turn = True
        self.spaces = []
        for row_num in range(TicTacToeBoard.num_rows):
            for col_num in range(TicTacToeBoard.num_cols):
                self.spaces.append((row_num, col_num))

    def play_x(self, space):
        if not self.x_turn:
            raise ValueError("Tried to play X on O turn")

        self.check_valid_move(space)
        self.x_set.add(space)
        self.x_turn = False

    def play_o(self, space):
        if self.x_turn:
            raise ValueError("Tried to play O on X turn")

        self.check_valid_move(space)
        self.o_set.add(space)
        self.x_turn = True

    def check_valid_move(self, space):
        if space not in self.spaces:
            raise ValueError(f"{space} not a valid space")

        if space in self.x_set:
            raise ValueError(f"{space} already contains an X")

        if space in self.o_set:
            raise ValueError(f"{space} already contains an O")

    def check_x_win(self):
        return TicTacToeBoard.check_win(self.x_set)

    def check_o_win(self):
        return TicTacToeBoard.check_win(self.x_set)

    def is_draw(self):
        return all([
            not self.check_x_win(),
            not self.check_o_win(),
            len(self.x_set) + len(self.o_set) == len(self.spaces)
        ])

    @staticmethod
    def check_win(piece_set):
        return any([
            TicTacToeBoard.check_row_win(piece_set),
            TicTacToeBoard.check_col_win(piece_set),
            TicTacToeBoard.check_forward_diagonal_win(piece_set),
            TicTacToeBoard.check_back_diagonal_win(piece_set),
        ])

    @staticmethod
    def check_row_win(piece_set):
        row_nums = [row_num for row_num, _ in piece_set]
        for row_num in set(row_nums):
            if row_nums.count(row_num) >= TicTacToeBoard.length_to_win:
                return True

        return False

    @staticmethod
    def check_col_win(piece_set):
        row_nums = [col_num for _, col_num in piece_set]
        for row_num in set(row_nums):
            if row_nums.count(row_num) >= TicTacToeBoard.length_to_win:
                return True

        return False

    @staticmethod
    def check_forward_diagonal_win(piece_set):
        diagonal_num = [row_num - col_num for row_num, col_num in piece_set]
        for row_num in set(diagonal_num):
            if diagonal_num.count(row_num) >= TicTacToeBoard.length_to_win:
                return True

        return False

    @staticmethod
    def check_back_diagonal_win(piece_set):
        diagonal_num = [row_num + col_num for row_num, col_num in piece_set]
        for row_num in set(diagonal_num):
            if diagonal_num.count(row_num) >= TicTacToeBoard.length_to_win:
                return True

        return False
