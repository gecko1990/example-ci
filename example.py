def add(a, b):
    return a + b

#esto deberia ser un comentario
#esto para cerrar el issue
def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
