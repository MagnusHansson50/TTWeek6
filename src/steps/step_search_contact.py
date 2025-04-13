from behave import given, when, then
from playwright.sync_api import expect
from pages.friend_page import FriendPage

@when(u'jag söker efter "lisa"')
def step_impl(context):
    context.friend_page.search_friend("lisa")


@then(u'ska "Lisa" visas i sökresultatet')
def step_impl(context):
    assert context.friend_page.friend_name_visible("Lisa")


@when(u'jag söker efter "EXAMPLE.COM"')
def step_impl(context):
    context.friend_page.search_friend("EXAMPLE.COM")
