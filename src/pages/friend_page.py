from playwright.sync_api import Page

class FriendPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_add_friend(self):
        self.page.goto("https://forverkliga.se/JavaScript/my-contacts/#/add")

    def fill_name(self, name):
        self.page.wait_for_selector('label:text("Namn") + input')
        self.page.fill('label:text("Namn") + input', name)

    def fill_email(self, email):
        self.page.wait_for_selector('label:text("E-post") + input')
        self.page.fill('label:text("E-post") + input', email)

    def click_save(self):
        self.page.get_by_role("button", name="Spara").click()

    def goto_friend_list(self):
        self.page.goto("https://forverkliga.se/JavaScript/my-contacts/#/friends")

    def friend_is_listed(self, name, email):
        self.page.goto("https://forverkliga.se/JavaScript/my-contacts/#/friends")
        return (self.page.get_by_text(name, exact=True)), (self.page.get_by_text(email, exact=True))

    def is_save_disabled(self):
        return self.page.get_by_role("button", name="Spara")

    def delete_friend(self, name, email):
        self.page.goto("https://forverkliga.se/JavaScript/my-contacts/#/friends")
        # Hitta raden som innehåller både namn och e-post
        contact_row = self.page.locator(".friend").filter(has_text=f"{name} {email}")
        # Klicka på knappen "Ta bort" i den raden
        contact_row.get_by_role("button", name="Ta bort").click()

    def search_friend(self, query):
        self.page.get_by_placeholder("Sök").fill(query)

    def friend_name_visible(self, name):
        return (self.page.get_by_text(name, exact=True)).is_visible()