# Infinity Works Individual Project.

Week 1, Week 2, Week 3, Week 4, Week 5, and Week 6 Projects.

* Overview can be seen within `mini-project-generation.pdf`.

Addition of an Individual attempt of a client PoC for ETL pipeline.

All are pushed under: `git commit -m "Individual Project"`

## Instructions.

All files functional for being run can be found within the `/src` folders.

This is usually found by looking in the nested weekly folders e.g. `w1_project/src`.

Depending upon system enter the following into a relevant shell/integrated terminal:

* Mac:  `python3 main.py`
* Windows: `py main.py`

### Folder Structures.

Below is the folders used within the project and what type of files they hold.

#### /src.

Includes the main source code and functionality for the applicaiton: `main.py`.

Includes the functions which are usually included in external folders, as well as relevant unit-testing files.

    e.g.` main_functions.py` & `test_main_functions.py`.

#### /notes.

includes files and documentation relevant for the weekly projects i.e. weekly pseudo code.

    e.g.`miniproject1-pseudo.txt`.

## Testing.

Testing is universal so follows the same format of unit-testing throughout all iterations.

To test use the below format in the relevant shell/integrated terminals of the filenames designated in their weekly sections below.

* Mac: `python3 {filename}.py` e.g. `python3 test_main_functions.py`
* Windows: `py {filename}.py` e.g. `py test_main_functions.py`

### Week 1 testing files.

`test_main_functions.py`

* functions being tested: `main_functions.py`

## Imports.

Breakdown of imports used for each weekly iteration of the individual project.

### Week 1 Imports.

`import unittest`

`import os`

## Change Log.

Breakdown of changes made to this repository, includes dates and days these changes were made.

### Week 1.

01/09/2023 - Friday: 

* Set up folder structure for Week 1 Project. Folders Inc: `notes` for documentation, and `src` including programing files.
* Created files for handling code within `src` folder.
  * `main.py` for main functionality of applicaiton.
  * `main_functions.py` to externally handle functions.
  * `test_main_functions.py` for testing functions from `main_functions.py`.
* Added `miniproject1-pseudo.txt` to `notes` folder to give overview of week1 project.
* Completed all designated criteria from the pseudo code in `miniproject1-pseudo.txt`.
* Added comments as descriptions, and `TODO's` for further improvement.
* imports of unittest & os were included for unit-testing and terminal clearing functionality.
