
import pytest
import maze

@pytest.mark.parametrize('archivo, meta',
    [
        ( 'maze1.txt', (0,5) ),
        ( 'maze2.txt', (8,13)),
        ( 'maze3.txt', (2,1) ),
        ( 'maze4.txt', (0,0)),
        ( 'maze5.txt', (0,10) )
    ]
)
def test_maze_solution(archivo,meta):
    m = maze.Maze(archivo)
    m.solve()
    assert m.solution[1][-1] == meta, "solution test failed"
