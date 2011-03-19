Django Reusable App Boilerplate
===============================

If you work with Django every day you will want to build reusable apps. This repository should work as a boilerplate for reusable Django apps. 

**Features:**

* It is ready for test driven development (TDD). Add your first test to tests.py before you implement anything!
* It is ready to be distributed via PyPi

We are still far from being experts in producing reusable apps. This repository is more or less what we have learned from some inspiring blog posts and from looking at other awesome repositories out there. The whole process of submitting an app based on this boilerplate to PyPi has never been tested (but will be tested soon). Suggestions for enhancements are much appreciated!

How to use
==========

::

  git clone git://github.com/bitmazk/django-reusable-app-boilerplate yourappname
  cd yourappname
  ./bin/init.sh
  ./yourappname/tests/runtests.py

The ``init.sh`` a script will ask you for some variables like your desired app-name and other information like keywords, app URL, app author and author email. Your inputs will be used to rename some folders and replace module names and imports in the boilerplate files provided. It will also be used to prepare your ``setup.py`` for easy distribution of your app via PyPi.
