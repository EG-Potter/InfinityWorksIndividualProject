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

    e.g.`main_functions.py`.

#### /notes.

includes files and documentation relevant for the weekly projects i.e. weekly pseudo code.

    e.g.`miniproject1-pseudo.txt`.

#### /app_data.

Includes files related to data/constants related to the functionality of the app (Menus, Titles, Collections etc).

    e.g.`app_data.py`.

#### /import_data.

Includes files which have data to be externally imported.

    e.g.`uk_registered_places.txt`.

#### /sub_menu.

Includes files which hold specific menu functionality, such as that for products or orders.

* Gives the ability for more localised/modular testing.

    e.g.`order_menu.py` and `product_menu.py`.

#### /unit_testing.

Includes files related to unit_testing, which is implemented through test-driven development.

    e.g.`test_main_functions.py`.

## Testing.

Testing is universal so follows the same format of unit-testing throughout all iterations.

To test use the below format in the relevant shell/integrated terminals of the filenames designated in their weekly sections below.

```
# Windows
$ py {filename}.py (e.g. py test_main_functions.py)

# MacOS/Unix
$ python3 {filename}.py (e.g. python3 test_main_functions.py)
```

### Week 1 - Testing Files.

`test_main_functions.py`

* functions being tested: `main_functions.py`

## Imports.

Breakdown of imports used for each weekly iteration of the individual project.

### Week 1 - Imports.

```
import unittest
import sys
import os
```

### Week 2 - Imports.

In addition to those from Week 1:

```
from ukpostcodeutils import validation
```

## Change Log.

Breakdown of changes made to the README.md, includes dates and days these changes were made.

### README - Change Log.

**01/09/2023 - Friday:**

* Created `README.md`, structed with Title & Sub-Sections:
  * `Instructions`, `Testing`, `Imports`, `Change Log`, and `MISC`.
* Added sub-section `Folder Structure` to `Instructions` sub-section.
  * Added sub-sections `/src`. & `/notes`. to `Folder Structure` sub-section.
* Added sub-section `Week 1 - Testing Files` to `Testing` sub-section.
* Added sub-section `Week 1 - Imports` to `Imports` sub-seciton.
* Added sub-section `Week 1 - Change Log` to  `Change Log` sub-section.

**02/09/2023 - Saturday:**

* Cleaned up sub-optimal elements within `README.md.`
* Added sub-section `Prerequisites` to `Instructions` sub-section.
* Added sub-section `/data` to `Folder Structure` sub-section.
* Added sub-section `Week 2 - Change Log` to `Change Log` sub-section.
* Added sub-section `README - Change Log `to `Change Log` sub-section.

**04/09/2023 - Monday:**

* Moved Change Logs for individual weekly projects into README.md files within each weeks folder.
* Added sub-sections `/import_data`, `/sub_menu`, `/unit_testing` to `Folder Structure` sub-section.
* Updated sub-section /data to /app_data in `Folder Structure` sub-section.
* Added sub-section `Week 2 - Imports` to `Imports` sub-seciton.
* Added additions to `MISC` sub-section.

## MISC

* `find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch`.
* `nameof(-)` - `from varname import varname, nameof`
* https://pypi.org/project/uk-postcode-utils/
  * https://github.com/mysociety/uk-postcode-utils
