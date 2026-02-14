from behave import given, when, then


@given('Open Reelly sign-in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when('Login to page using {email} and {password}')
def login(context, email, password):
    context.app.sign_in_page.login(email, password)