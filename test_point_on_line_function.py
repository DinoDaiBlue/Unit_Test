# test_point_on_line_function
import pytest


@pytest.mark.parametrize("point1, point2, input, expected", [
    ((1, 1), (2, 2), 3, 3),
    ((1, 0), (1, 2), 1, "NaN"),
    ((-1, 0), (0, 1), 1, 2),
    ((0, 1), (0, 2), 0, "NaN"),
    ((1, 0), (2, 0), 4, 4)
])
def test_point_on_line(point1, point2, input, expected):
    from point_on_line_function import point_on_line
    answer = point_on_line(point1, point2, input)
    assert answer == expected


@pytest.mark.parametrize("point1, point2, input, expected", [
    ((1, 1), (2, 2), (3, 3), "True"),
    ((1, 0), (1, 2), (2, 4), "False"),
    ((1, 0), (1, 2), (1, 3), "True"),
    ((0, 1), (0, 3), (0, 5), "True"),
    ((1, 0), (2, 0), (4, 0), "True"),
    ((0, 0), (1, 2), (2, 4), "True")
])
def test_point_on_line_tf(point1, point2, input, expected):
    from point_on_line_function import point_on_line_tf
    answer = point_on_line_tf(point1, point2, input)
    assert answer == expected
