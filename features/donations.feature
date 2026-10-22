Feature: Charity donation tracking
  As a charity volunteer
  I want to record donations and calculate the total
  So that the charity can keep a simple record of funds received

  Scenario: Record a valid donation
    Given the donation tracker is empty
    When a donor records a donation of 25
    Then the donation should be recorded successfully
    And the donation count should be 1

  Scenario: Reject a negative donation
    Given the donation tracker is empty
    When a donor records a donation of -10
    Then the system should reject the donation
    And the donation count should be 0

  Scenario: Calculate the total of recorded donations
    Given the donation tracker is empty
    And a donation of 25 has been recorded
    And a donation of 10.50 has been recorded
    When the total donations are requested
    Then the total donations should be 35.50
