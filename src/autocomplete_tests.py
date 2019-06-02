from hamcrest import assert_that, equal_to
from client import create_client


"""
Tests for autocomplete.
More needed, and could be broken up into files by functionality.
"""


def test_ten_results_returned(delete_previous_db_record):
    """
    I'm assuming the fictional gateway schema only
    returns ten results and has an API endpoint called getResults
    which accepts a search string
    """
    request = create_client().gateway.getResults(
        search="some string").response()

    # Assert sucessful request
    assert_that(request.result.status, equal_to('200'))

    """
    I'm assuming the json object uses a list to contain
    the results
    """
    assert_that(len(request.result.results, equal_to(10)))
