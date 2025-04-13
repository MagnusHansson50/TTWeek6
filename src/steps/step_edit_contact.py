from behave import given, when, then
from playwright.sync_api import expect
from pages.friend_page import FriendPage

@given(u'vännen "Lisa" med e-post "lisa@example.com" finns')
def step_impl(context):
    context.friend_page = FriendPage(context.page)
    context.friend_page.goto_add_friend()

    context.friend_page.fill_name("Lisa")
    context.friend_page.fill_email("lisa@example.com")

    context.friend_page.click_save()

    name_field, email_field = context.friend_page.friend_is_listed("Lisa", "lisa@example.com")
    expect(name_field).to_be_visible()
    expect(email_field).to_be_visible()

@when(u'jag ändrar hennes e-post till "lisa@nytt.se"')
def step_impl(context):
    context.friend_page.goto_friend_list()
    context.page.get_by_role("main").locator("div").filter(has_text="Lisa lisa@example.com Ändra").locator("a").click()
    form = context.page.locator("section.form")
    form.locator("input").nth(1).fill("lisa@nytt.se")


@then(u'ska "Lisa" ha e-post "lisa@nytt.se" i listan')
def step_impl(context):
    name_field, email_field = context.friend_page.friend_is_listed("Lisa", "lisa@nytt.se")
    expect(name_field).to_be_visible()
    expect(email_field).to_be_visible()
