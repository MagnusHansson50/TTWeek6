from behave import given, when, then
from playwright.sync_api import expect
from pages.friend_page import FriendPage

@given(u'vännen "Lisa" finns i listan')
def step_impl(context):
    context.friend_page = FriendPage(context.page)
    context.friend_page.goto_add_friend()

    context.friend_page.fill_name("Lisa")
    context.friend_page.fill_email("lisa@example.com")

    context.friend_page.click_save()

    name_field, email_field = context.friend_page.friend_is_listed("Lisa", "lisa@example.com")
    expect(name_field).to_be_visible()
    expect(email_field).to_be_visible()


@when(u'jag klickar på "Ta bort" bredvid hennes namn')
def step_when_delete_contact(context):
    context.friend_page.delete_friend("Lisa", "lisa@example.com")


@then(u'ska "Lisa" inte längre visas i listan')
def step_impl(context):
    assert not context.friend_page.friend_name_visible("Lisa")
