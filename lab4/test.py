from app import Figure

def test_figure_type():
    fig = "square"
    square = Figure(fig, 2)
    assert square.get_figure_type == fig, "get_figure_type returned wrong value"

def test_figure_length():
    length = 5
    rect = Figure("rectangle", length)
    assert rect.get_figure_length == length, "get_figure_length returned wrong value"

def test_obj_invalid():
    # створюємо об'єкт з недозволеними параметрами
    import pytest
    with pytest.raises(AssertionError):
        Figure("circle", 1)
    with pytest.raises(AssertionError):
        Figure("square", 0)

def test_get_angles():
    triangle = Figure("triangle", 1)
    assert triangle.get_angles == 3, "Triangle should have 3 angles"

    square = Figure("square", 2)
    assert square.get_angles == 4, "Square should have 4 angles"
