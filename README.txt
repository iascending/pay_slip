Myob-Exercise
=============

Generate employee's pay slip information with name, pay period, gross income, income tax, net income and super.

Installation
------------

- Using pip:

    download and uzip myob-exercise.zip

    $ pip install virtualenv
    $ cd myob-exercise (the folder contains downloaded source files)
    $ virtualenv -p python3 . (or virtualenv .)
    $ source bin/activate
    $ pip install -r requirements.txt

Usage
-----

Myob-Exercise --- Generate Employee Payslip Information. Shown here is an example
of how to use it. Feel free to modify input.csv file to get more results.

    $ cd myob-exercise
    $ source bin/activate
    $ cd src
    $ python myob-exercise.py
