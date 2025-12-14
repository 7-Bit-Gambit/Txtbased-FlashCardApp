
Text Based Flashcard App
=====================

Text Based Flashcard App is an interactive, console-based flashcard application designed for students who want to create, study, and manage flashcard decks efficiently. It supports deck creation, learning sessions with randomization, progress tracking, and deck editing, all handled using simple CSV-files.

Features
--------
- Create flashcard decks with custom questions and answers
- Learn from a deck in random order
- Track proficiency levels
- Edit decks (add, remove, delete decks)
- Data validation
- CSV-based file storage
- Interactive CLI menu 

Intended Audience
-----------------
This application is built for students who want to study more efficiently using customizable digital flashcards.

Tech Stack
----------
- Python (Version 3.13)
- CSV (built-in library)
- No external libraries required

Installation
------------
1. Download or clone the repository.
2. Ensure all project files are present.
	?  main.py
	?  config.py
	?  create_deck.py
	?  delete_deck.py
	?  deck_selector.py
	?  learn_from_deck.py
	?  datahandlers.py
	?  check_knowledge_level.py

3. Run the main application:

   main.py

Configuration
-------------
The application:
- Stores decks in CSV files
- Validates user input
- Generates all required files automatically

Usage
-----
Main menu:

What would you like to do today?
1. Learn from a deck.
2. Create a deck.
3. Delete a deck.
4. Check your knowledge level.
(To terminate the app press enter)

Project Structure
-----------------
flashcard_app/
│
├── main.py
├── config.py
│
├── deck_helpers.py
├── card_helpers.py
│
├── create_deck.py
├── edit_deck.py
├── learn_from_deck.py
├── check_knowledge_level.py
│
└── decks/
    ├── example_deck.csv
License
-------
No formal license specified. Intended for academic use.



User Story
-------------------------------------------------------------------------
As a student, I want to have an application that allows me to create and manage flashcard decks so that I can study more efficiently.

This user story guided the overall design and implementation of the application. The following section explains how each requirement of the user story is fulfilled and where this functionality is implemented in the source code.

Creating Flashcard Decks
----------------------------------------
Requirement
As a student, I want to create my own flashcard decks and populate them with my own questions and answers.

Implementation
----------------------------------------
- Interactive menu option for deck creation
- User input for deck name, questions, and answers
- Input validation before saving
- Persistent storage using CSV files

Responsible Files
----------------------------------------
create_deck.py
datahandlers.py
config.py

2. Learning From a Deck
----------------------------------------
Requirement:
I want to select a deck, answer questions in random order, and have my progress tracked.


Implementation
----------------------------------------
- Deck selection from available CSV files
- Randomized order of flashcards
- Evaluation of user answers
- Proficiency tracking per card

Responsible Files
----------------------------------------
learn_from_deck.py
deck_selector.py
datahandlers.py

3. Proficiency Overview
----------------------------------------
Requirement:
I want to see how well I am doing so I know which decks to focus on.

Implementation:
----------------------------------------
- Proficiency values stored per flashcard
- Knowledge level calculation and display

Responsible Files:
----------------------------------------
check_knowledge_level.py
datahandlers.py

4. Editing and Deleting Decks
----------------------------------------
Requirement:
I want to edit and delete flashcard decks.


Implementation:
----------------------------------------
- Menu option to delete decks
- Safe removal of deck files
- Validation of selected decks

Responsible Files:
----------------------------------------
delete_deck.py
deck_selector.py
datahandlers.py

Conclusion
----------------------------------------
All user story requirements are fulfilled through modular Python files, interactive CLI input, CSV-based persistence, and clear separation of responsibilities.


Authors
-------
- Jules Andreas Kern
- Tim Freyvogel
- Ata Erduran


