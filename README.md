# Infinity Works Individual Project.

Week 1, Week 2, Week 3, Week 4, Week 5, and Week 6 Projects.

* Overview can be seen within `mini-project-generation.pdf`.

Addition of an Individual attempt of a client PoC for ETL pipeline.

All are pushed under: `git commit -m "Individual Project"`

## Instructions.

All files functional for being run can be found within the `/src` folders.

This is usually found by looking in the nested weekly folders e.g. `/w1_project/src`.

Depending upon system enter the following into a relevant shell/integrated terminal:

```
# Windows
$ py main.py

# MacOS/Unix
$ python3 main.py
```

### Prerequisites.

* Python 3 (Ideally 3.11).
* A clone of this repo.
* A suitable dev environment, such as `VSCode.`

### Folder Structure.

Below is the folders used within the project and what type of files they hold.

#### /src.

Includes the main source code and functionality for the applicaiton: `main.py`.

Includes the functions which are usually included in external folders, as well as relevant unit-testing files.

    e.g.`main_functions.py` & `test_main_functions.py`.

#### /notes.

includes files and documentation relevant for the weekly projects i.e. weekly pseudo code.

    e.g.`miniproject1-pseudo.txt`.

#### /data.

Includes files related to data/constants related to the functionality of the app.

    e.g.`application_data.py`.

## Testing.

Testing is universal so follows the same format of unit-testing throughout all iterations.

To test use the below format in the relevant shell/integrated terminals of the filenames designated in their weekly sections below.

```
# Windows
$ py {filename}.py (e.g. py test_main_functions.py)

# MacOS/Unix
$ python3 {filename}.py (e.g. python3 test_main_functions.py)
```

### Week 1 Testing Files.

`test_main_functions.py`

* functions being tested: `main_functions.py`

## Imports.

Breakdown of imports used for each weekly iteration of the individual project.

### Week 1 Imports.

```
import unittest
import sys
import os
```

## Change Log.

Breakdown of changes made to this repository, includes dates and days these changes were made.

### Week 1 - Change Log.


**01/09/2023 - Friday:**

* Set up folder structure for Week 1 Project.
  * Folders Inc: `notes` for documentation, and `src` including programing files.
* Created files for handling code within `src` folder.
  * `main.py` for main functionality of applicaiton.
  * `main_functions.py` to externally handle functions.
  * `test_main_functions.py` for testing functions from `main_functions.py`.
* Added `miniproject1-pseudo.txt` to `notes` folder to give overview of week1 project.
* Completed all designated criteria from the pseudo code in `miniproject1-pseudo.txt`.
* Implemented comments as descriptions, and `TODO's` for further improvement.
* imports of unittest & os were included for unit-testing and terminal clearing functionality.


**02/09/2023 - Saturday:**

* Cleaned sub-optimal code, and improved spacing in files for better readability.
* Implemented seperation of a main menu and product menu functionality.
* Implemented specific menu constants for each section.
  * `MAIN_MENU `& `PRODUCTS MENU`.
* Implemented specific title constants for each section.
  * `APP_TITLE` & `PRODUCT_TITLE`.
* Implemented new folder into the folder structure.
  * `data` folder was added to handle Title & Menu constants seperately from `main.py`.
  * `sys.path.append('../')` was added to deal with pathing to files in seperate folders.


### Week 2 - Change Log.


**02/09/2023 - Saturday:**

* Set up folder structure for Week 2 Project, Folders Inc:

  * `notes` for documentation,
  * `src` including programing files.
  * `data` for data/constant storage.
* Created files for handling code within `src` folder.

  * `main.py` for main functionality of applicaiton.
  * `main_functions.py` to externally handle functions.
  * `test_main_functions.py` for testing functions from `main_functions.py`.
* Added `mini-project-week-2.md` to `notes` folder to give overview of week2 project.
* Added `application_data.py` to `data` folder, contains data/constants needed for functionality.
* Added in comments to divide functions and unit-tests in files.
* Changed `main_functions.py` to `functions.py`.

  * `test_main_functions.py `also to `test_functions.py.`


### README - Change Log.


**01/09/2023 - Friday:**

* Created `README.md`, structed with Title & Sub-Sections:
  * `Instructions`, `Testing`, `Imports`, `Change Log`, and `MISC`.
* Added sub-section `Folder Structure` to `Instructions` sub-section.
  * Added sub-sections `/src`. & `/notes`. to `Folder Structure` sub-section.
* Added sub-section `Week 1 Testing Files` to `Testing` sub-section.
* Added sub-section `Week 1 Imports` to `Imports` sub-seciton.
* Added sub-section `Week 1 - Change Log` to  `Change Log` sub-section.


**02/09/2023 - Saturday:**

* Cleaned up sub-optimal elements within `README.md.`
* Added sub-section `Prerequisites` to `Instructions` sub-section.
* Added sub-section `/data` to `Folder Structure` sub-section.
* Added sub-section `Week 2 - Change Log` to `Change Log` sub-section.
* Added sub-section `README - Change Log `to `Change Log` sub-section.


## MISC

* `find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch`.
