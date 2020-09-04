# test_point_on_line_function
@pytest.mark.parametrize("point1, point2, expected", [
	((1, 1), (2, 2), (3, 3)),
	((1, 0), (1, 2), (1, 3)),
	((-1, 0), (0, 1), (1, 2)),
])
def test_point_on_point(point1, point2, expected):
	from test_point_on_line_function import point_on_line
	answer = point_on_line(point1, point2, expected)
	assert answer == expected
