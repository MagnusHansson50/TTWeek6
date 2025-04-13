Feature: Ändra uppgifter för en vän

  Scenario: Ändra e-postadress för en existerande vän
    Given vännen "Lisa" med e-post "lisa@example.com" finns
    When jag ändrar hennes e-post till "lisa@nytt.se"
    And klickar på "Spara"
    Then ska "Lisa" ha e-post "lisa@nytt.se" i listan