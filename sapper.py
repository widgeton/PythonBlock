import random as rnd


class Cell:
    def __init__(self, mine: bool, around_mines: int = 0):
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = False

    def __str__(self):
        if self.fl_open and not self.mine:
            return str(self.around_mines)
        if self.fl_open and self.mine:
            return "*"
        return "#"


class GamePole:
    def __init__(self, size: int, mines: int):
        self.size = size
        self.mines = mines
        self.pole = []
        self.init()

    def init(self):
        lst = [Cell(mine=True) if i < self.mines else Cell(mine=False) for i in range(self.size ** 2)]
        rnd.shuffle(lst)

        for i in range(self.size):
            start = i * self.size
            end = start + self.size
            self.pole.append(lst[start:end])

        for r_num, row in enumerate(self.pole):
            for c_num, cell in enumerate(row):
                around_mines = 0

                if self._has_up_mine(r_num, c_num):
                    around_mines += 1
                if self._has_down_mine(r_num, c_num):
                    around_mines += 1
                if self._has_right_mine(r_num, c_num):
                    around_mines += 1
                if self._has_left_mine(r_num, c_num):
                    around_mines += 1
                if self._has_up_left_mine(r_num, c_num):
                    around_mines += 1
                if self._has_up_right_mine(r_num, c_num):
                    around_mines += 1
                if self._has_down_left_mine(r_num, c_num):
                    around_mines += 1
                if self._has_down_right_mine(r_num, c_num):
                    around_mines += 1

                cell.around_mines = around_mines

    def _has_up_mine(self, row_idx: int, cell_idx: int) -> bool:
        return row_idx > 0 and \
            self.pole[row_idx - 1][cell_idx].mine

    def _has_down_mine(self, row_idx: int, cell_idx: int) -> bool:
        return row_idx < self.size - 1 and \
            self.pole[row_idx + 1][cell_idx].mine

    def _has_right_mine(self, row_idx: int, cell_idx: int) -> bool:
        return cell_idx < self.size - 1 and \
            self.pole[row_idx][cell_idx + 1].mine

    def _has_left_mine(self, row_idx: int, cell_idx: int) -> bool:
        return cell_idx > 0 and \
            self.pole[row_idx][cell_idx - 1].mine

    def _has_up_left_mine(self, row_idx: int, cell_idx: int) -> bool:
        return row_idx > 0 and \
            cell_idx > 0 and \
            self.pole[row_idx - 1][cell_idx - 1].mine

    def _has_up_right_mine(self, row_idx: int, cell_idx: int) -> bool:
        return row_idx > 0 and \
            cell_idx < self.size - 1 and \
            self.pole[row_idx - 1][cell_idx + 1].mine

    def _has_down_left_mine(self, row_idx: int, cell_idx: int) -> bool:
        return row_idx < self.size - 1 and \
            cell_idx > 0 and \
            self.pole[row_idx + 1][cell_idx - 1].mine

    def _has_down_right_mine(self, row_idx: int, cell_idx: int) -> bool:
        return row_idx < self.size - 1 and \
            cell_idx < self.size - 1 and \
            self.pole[row_idx + 1][cell_idx + 1].mine

    def show(self):
        for row in self.pole:
            print(*row)


if __name__ == '__main__':
    pole_game = GamePole(10, 12)
