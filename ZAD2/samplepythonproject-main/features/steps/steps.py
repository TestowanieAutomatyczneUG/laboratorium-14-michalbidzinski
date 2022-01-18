from behave import *
from src.FizzBuzz import FizzBuzz
use_step_matcher("parse")


@given('FizzBuzz feature')
def step_impl(context):
    context.FizzBuzz = FizzBuzz()


@when(u'I pass the {num:d}')
def step_impl(context, num):
    context.result = context.FizzBuzz.game(num)
@when(u'I pass the {invalid_data}')
def step_impl(context, invalid_data):
    context.result = context.FizzBuzz.game(invalid_data)

@then('The result is Fizz')
def step_impl(context):
    assert context.result == "Fizz"


@then('The result is FizzBuzz')
def step_impl(context):
    assert context.result == "FizzBuzz"


@then('The result is Buzz')
def step_impl(context):
    assert context.result == "Buzz"


@then('The result is {output:d}')
def step_impl(context, output):
    assert context.result == output
@then('The result is {err}')
def step_impl(context, err):
    assert context.result == err
