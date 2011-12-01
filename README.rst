*******
CurlyTx
*******
Enigma2 (Dreambox) plugin that lets you view the contents of remote
*plain text* files, e.g. HTTP URLs.

Multiple URLs can be configured and navigated.

.. contents::
   :depth: 2


========
Features
========
- Load any remote plain text files, e.g. via HTTP
- Unlimited number of remote URLs/pages
- Reload pages
- Show HTTP headers
- Configurable page titles
- Configurable text size
- Configurable default page
- Import complete page list from Atom feed
- Visible in the main menu or the extension menu (configurable)
- Configurable menu title
- Help screen for main window and settings window


=====
Usage
=====

First run
=========
After installing CurlyTx and restarting Enigma2, open the main menu.
The first entry will be "CurlyTx" - activate it.

You will see the main window with the message
"Go and add a page in the settings".
Do just that end press the red button to access the settings window.

Now we'll add the first URL:

- Press the yellow button ("New"); the "page edit" window will show up
- Enter the page URL, e.g. http://ip.cweiske.de
- If you wish, enter a page title, e.g. "My IP"
- Set the text size if you want. 20 is a good default value.
- Press the green button ("OK"), and you are back on the settings window.
- The page you have just created is in the configuration list now.


If you made a mistake and want to change it, select the page with the
up/down buttons and press "OK" - the page edit window will open.

Press the green button and the settings will be saved.
You're back on the main window now and the URL you just configured will be loaded.


Adding many pages
=================
You can use the settings window to add new pages, but this gets tedious if you
want to add many pages.
It's better to use the Atom feed import in this case.


=================
Modifying CurlyTx
=================


Translation
===========
Beginning a new translation
---------------------------
Replace ``$lang_code`` with your two-letter language code::

    $ cd po
    $ cp messages.po $lang_code.po
    ... edit $lang_code.po now
    $ ./compile.sh


Editing an existing translation
-------------------------------
Simply run ::

    $ cd po
    $ ./update.sh

This will update the translation template ``messages.pot`` from the source code
and will merge the changes into the single translation files.


Testing a translation
---------------------
Link your compiled translation file into ::

    src/locale/$lang_code/LC_MESSAGES/CurlyTx.mo

Enigma2 will pick it up automatically.


Building
========
First upgrade the version number in ``CONTROL/control``.

Then simply run ::

    ./build.sh

You will need the ``ipkg-build`` script from
 http://reichholf.net/files/dreambox/tools/ipkg-build

Also see http://dream.reichholf.net/wiki/Howto:IPK_Pakete_erstellen


Open issues
===========
- move mode to re-order pages
- how to show clock in lcd?


=======
License
=======
The plugin is subject to the GPLv3 or later.
