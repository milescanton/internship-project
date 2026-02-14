from behave import given, when, then


@then('Add and verify test information')
def add_and_verify_info(context):

    project_data = {
        "name": "Miles Canton",
        "company": "Careerist",
        "role": "QA Engineer",
        "age": "27",
        "country": "United States",
        "project_name": "Task 2",
        "phone": "1234567890",
        "email": "cantonmiles.com"
    }

    context.app.add_project_page.add_info(project_data)
    context.app.add_project_page.verify_info(project_data)

@then('Verify Send an Application button is active')
def verify_submit_button(context):
    context.app.add_project_page.verify_submit_button()