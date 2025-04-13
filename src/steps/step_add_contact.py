from behave import given, when, then
from playwright.sync_api import expect
from pages.friend_page import FriendPage

@given(u'att användaren är på Ny vän sidan')
def step_given_contact_page(context):
    context.friend_page = FriendPage(context.page)
    context.friend_page.goto_add_friend()
    #context.page.goto(context.base_url)
    #context.page.click('text="Ny vän"')

@when(u'användaren fyller i namn "{name}" och e-post "{email}"')
def step_when_fill_in_new_contact(context, name, email):
    name = "" if name == "__EMPTY__" else name
    email = "" if email == "__EMPTY__" else email
    context.friend_page.fill_name(name)
    context.friend_page.fill_email(email)
    #context.page.wait_for_selector('label:text("Namn") + input')
    #context.page.fill('label:text("Namn") + input', "Lisa")
    #context.page.wait_for_selector('label:text("E-post") + input')
    #context.page.fill('label:text("E-post") + input', "lisa@example.com")

@when(u'klickar på "Spara"')
def step_when_click_save(context):
    context.friend_page.click_save()
    #context.page.get_by_role("button", name="Spara").click(timeout=100)

@then('ska "{name}" med e-post "{email}" visas i vänlistan')
def step_then_new_contact_is_shown_in_friend_list(context, name, email):
    name_field, email_field = context.friend_page.friend_is_listed(name, email)
    expect(name_field).to_be_visible()
    expect(email_field).to_be_visible()
    #context.page.click('text="Vänlista"')
    #expect(context.page.get_by_text("Lisa", exact=True)).to_be_visible()
    #expect(context.page.get_by_text("lisa@example.com", exact=True)).to_be_visible()

@then(u'ska inte spara knappen vara klickbar')
def step_then_save_button_is_disabled(context):
    spara_button = context.friend_page.is_save_disabled()
    expect(spara_button).to_be_disabled()