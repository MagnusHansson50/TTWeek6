Feature: Ta bort en vän


  Scenario: Ta bort en existerande vän
    Given vännen "Lisa" finns i listan
    When jag klickar på "Ta bort" bredvid hennes namn
    Then ska "Lisa" inte längre visas i listan