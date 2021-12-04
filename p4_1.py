from typing import List, Tuple

def parse_input(s: str) -> Tuple[List[int], List[List[List[int]]]]:
    l = s.replace("\n\n","\n|\n")
    blocks = l.split("|")
    moves = [int(m) for m in blocks[0].strip().split(',')]
    boards = [b.strip().split('\n') for b in blocks[1:]]
    boards = [[[int(s) for s in x.split()] for x in b] for b in boards]
    return (moves, boards)

def column(c: int, board: List[List[int]]) -> List[int]:
  return [row[c] for row in board]

def check(row: int, col: int, board: List[List[int]]) -> int:
  colnotempty = [i for i in column(col, board) if i > 0]
  rownotempty = [i for i in board[row] if i > 0]
  return not rownotempty or not colnotempty

def score(move: int, board: List[List[int]]) -> int:
  b = [i for row in board for i in row if i >= 0]
  return sum(b) * move

def mark(move, boards):
  for board in boards:
    for r in range(len(board)):
      for c in range(len(board[0])):
        if board[r][c] == move:
          board[r][c] = -1
          if check(r, c, board):
            return score(move, board)
  return 0

def do(data: str) -> int:
  (moves, boards) = parse_input(data)
  bingo = 0
  for m in moves:
    bingo = mark(m, boards)
    if bingo:
      return bingo
