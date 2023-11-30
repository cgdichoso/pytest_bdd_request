from pytest_bdd import scenario, given, when, then
from pytest_bdd.parsers import cfparse


@scenario('../features/simple_cucumber.feature',
          'This is a simple scenario')
def test_runner():
    pass


@given(cfparse('the "{url}" parameter specified'), target_fixture='')
def given_method(sb, url):
    sb.get(url)


@when(cfparse('the action is performed'), target_fixture='')
def when_method():
    pass


@then('the expected result is displayed', target_fixture='')
def then_method():
    pass
