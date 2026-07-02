Feature: Paper favorites data requirements
  As a researcher using the arxiv-papers-mobile app
  I want to mark and manage papers as favorites
  So that I can quickly revisit relevant research

  Background:
    Given I have access to the arXiv search API

  Scenario: A search result contains all fields needed to save a favorite
    When I fetch a paper from the search results for "deep learning"
    Then the paper has a unique identifier for storage
    And the paper has a non-empty title for display
    And the paper has at least one author for display
    And the paper has a published date for metadata

  Scenario: Multiple results all provide complete favorite data
    When I fetch 5 papers from the search results for "machine learning"
    Then every paper has a unique identifier
    And every paper has a non-empty title
    And all paper identifiers are distinct
