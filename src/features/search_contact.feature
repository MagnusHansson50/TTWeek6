Feature: Söka efter en vän

  Scenario: Söka efter namn (case-insensitivt)
    Given vännen "Lisa" med e-post "lisa@example.com" finns
    When jag söker efter "lisa"
    Then ska "Lisa" visas i sökresultatet

  Scenario: Söka efter e-post (case-insensitivt)
    Given vännen "Lisa" med e-post "lisa@example.com" finns
    When jag söker efter "EXAMPLE.COM"
    Then ska "Lisa" visas i sökresultatet