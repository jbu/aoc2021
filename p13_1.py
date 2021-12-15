import numpy as np
from functools import partial, reduce

def print_dots(coords, title=''):
  mx = np.amax(coords, axis=1)
  mn = np.amin(coords, axis=1)
  print(f"--- {title}")
  print("  ", end='')
  for x in range(mn[0], mx[0]+1):
    print(f"{x:2}", end='')
  print()
  for y in range(mn[1], mx[1]+1):
    print(f"{y:2} ", end='')
    for x in range(mn[0], mx[0]+1):
      is_coord = any(np.equal(coords.T,[x, y, 1]).all(1))
      p = '#' if is_coord else '.'
      print(f"{p:2}", end='')
    print()

def split_horizontal(coords:np.array, y: int) -> tuple[np.array, np.array]:
  stays = coords[:, coords[1,:] < y]
  folds = coords[:, coords[1,:] >= y]
  return (stays, folds)

def split_vertical(coords:np.array, x: int) -> tuple[np.array, np.array]:
  stays = coords[:, coords[0,:] < x]
  folds = coords[:, coords[0,:] >= x]
  return (stays, folds)

# Could go further with factoring out the transformation matrices and split.

def fold_up(y: int, coords:np.array) -> np.array:
  fold_along_x = np.array([[1, 0, 0],[0,-1, 0], [0, 0, 1]])
  translate_y = lambda yy: np.array([[1, 0, 0],[0, 1, yy], [0, 0, 1]])
  stays, folds = split_horizontal(coords, y)
  folds2 = translate_y(-y) @ folds
  folds2 = fold_along_x @ folds2
  folds2 = translate_y(y) @ folds2
  return np.hstack((folds2, stays))

def fold_left(x: int, coords:np.array) -> np.array:
  fold_along_y = np.array([[-1, 0, 0],[0,1, 0], [0, 0, 1]])
  translate_x = lambda xx: np.array([[1, 0, xx],[0, 1, 0], [0, 0, 1]])
  stays, folds = split_vertical(coords, x)
  folds2 = translate_x(-x) @ folds
  folds2 = fold_along_y @ folds2
  folds2 = translate_x(x) @ folds2
  return np.hstack((folds2, stays))

def do(data: str) -> int:
  """
  >>> do('''6,10
  ... 0,14
  ... 9,10
  ... 0,3
  ... 10,4
  ... 4,11
  ... 6,0
  ... 6,12
  ... 4,1
  ... 0,13
  ... 10,12
  ... 3,4
  ... 3,0
  ... 8,4
  ... 1,10
  ... 2,14
  ... 8,10
  ... 9,0
  ... 
  ... fold along y=7
  ... fold along x=5''')
  17 
  """
  instructions = []
  coord_l = []
  for line in data.splitlines():
    if line.startswith("fold"):
      i = line.split('=')
      match i:
        case ['fold along y', x]: instructions.append(partial(fold_up, int(x)))
        case ['fold along x', y]: instructions.append(partial(fold_left, int(y)))
    elif line != '':
      coord_l.append(tuple([int(x) for x in line.split(',')] + [1]))
  coords = np.array(coord_l).T

  transformed_coords = reduce(lambda c, i: i(c), instructions, coords)
  print_dots(transformed_coords)
  return np.unique(transformed_coords, axis=1).shape[1]


if __name__ == "__main__":
  import doctest
  doctest.testmod()