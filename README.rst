=======
CurlyTx
=======
Enigma2 (Dreambox) plugin that lets you view the contents of remote
plain text files, e.g. HTTP.

Multiple URLs can be configured and navigated.



Open issues
===========
- move mode to re-order pages
- how to show clock in lcd?


License
=======
The plugin is subject to the GPLv3 or later.



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


Building
========
First upgrade the version number in ``CONTROL/control``.

Then simply run ::

    ./build.sh

You will need the ``ipkg-build`` script from
 http://reichholf.net/files/dreambox/tools/ipkg-build

Also see http://dream.reichholf.net/wiki/Howto:IPK_Pakete_erstellen
