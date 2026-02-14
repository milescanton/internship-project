from behave import given, when, then


@when('Click on Settings')
def click_on_settings(context):
    context.app.index_page.click_on_settings()