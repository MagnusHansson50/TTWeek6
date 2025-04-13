Feature: Lägga till en ny vän

  Scenario Outline: Användaren lägger till en vän med korrekt information
    Given att användaren är på Ny vän sidan
    When användaren fyller i namn "<name>" och e-post "<email>"
    And klickar på "Spara"
    Then ska "<name>" med e-post "<email>" visas i vänlistan
    Examples:
    |name   | email             |
    | Lisa  | lisa@example.com  |


  Scenario Outline: Användaren försöker lägga till en vän utan att fylla i alla fält
    Given att användaren är på Ny vän sidan
    When användaren fyller i namn "<name>" och e-post "<email>"
    Then ska inte spara knappen vara klickbar
    Examples:
    |name       | email             |
    | __EMPTY__ | hej@example.com   |
    | hej       | __EMPTY__         |
