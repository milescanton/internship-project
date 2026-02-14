from behave import given, when, then


@when('Click on Add a Project')
def click_on_add_a_project(context):
    context.app.settings_page.click_on_add_a_project()