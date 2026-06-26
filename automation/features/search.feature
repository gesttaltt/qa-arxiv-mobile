Feature: arXiv paper search
  As a researcher using the arxiv-papers-mobile app
  I want to search for academic papers by keyword
  So that I can find relevant research quickly

  Background:
    Given I have access to the arXiv search API

  Scenario: Valid keyword returns results
    When I search for "machine learning"
    Then the response status is 200
    And the response contains at least 1 paper
    And each paper has a non-empty title

  Scenario: Empty query is handled gracefully
    When I search with an empty query
    Then the response status is 200 or 400

  Scenario Outline: Popular academic topics all return results
    When I search for "<keyword>"
    Then the response status is 200
    And the response contains at least 1 paper

    Examples:
      | keyword          |
      | quantum physics  |
      | neural networks  |
      | computer science |
