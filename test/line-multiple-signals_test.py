from railwayroutegenerator import generator
from .helper import compare_route_lists


def test_line_multiple_signals():
    routes = generator.generate_from_planpro("line-test-multiple-signals.ppxml", output_format="python-objects")
    expected_routes = [("60ES1", "60AS1"), ("60AS1", "60BS1"), ("60BS1", "60ES2"),
                       ("60ES2", "60AS2"), ("60ES3", "60AS3")]
    compare_route_lists(routes, expected_routes)


if __name__ == '__main__':
    test_line_multiple_signals()
