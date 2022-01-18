from behave import *
from src.ISBN import ISBN


@given('ISBN validate function')
def step_imp(context):
    context.validate = ISBN.validate


@when('the inputed number is  {num}')
def step_imp(context, num):
    context.result = context.validate(num)


@then('the output is {result}')
def step_imp(context, result):
    assert str(context.result) == result
