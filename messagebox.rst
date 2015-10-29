MessageBox
==========
The MessageBox widget is a subclass of the :doc:`dialog` object. It is tailored for displaying short messages to the user such as information or errors, but can also be used to ask simple questions.

===========
Constructor
===========
The MessageBox widget is constructed using::

  messagebox = QMessageBox()

=======
Methods
=======
The text on the MessageBox can be set with::

  messagebox.setText(text)

If a more detailed description of the message is required, such as a portion of a log file, this can be displayed using::

  messagebox.setInformativeText(text)

Standard buttons are Qt provided buttons which can easily be added to the MessageBox without the user having to create each one manually. These can be set via::

  messagebox.setStandardButtons(buttons)

The standard buttons supported are:

* ``QMessageBox.Ok``
* ``QMessageBox.Open``
* ``QMessageBox.Save``
* ``QMessageBox.Cancel``
* ``QMessageBox.Close``
* ``QMessageBox.Discard``
* ``QMessageBox.Apply``
* ``QMessageBox.Reset``
* ``QMessageBox.RestoreDefaults``
* ``QMessageBox.Help``
* ``QMessageBox.SaveAll``
* ``QMessageBox.Yes``
* ``QMessageBox.YesToAll``
* ``QMessageBox.No``
* ``QMessageBox.NoToAll``
* ``QMessageBox.Abort``
* ``QMessageBox.Retry``
* ``QMessageBox.Ignore``

A user can add and remove extra buttons manually with::

  messagebox.addButton(button)
  messagebox.removeButton(button)

In both cases, the *button* object points to the button object (such as a :doc:`pushbutton`) to be added or removed.

Icons can be added to the MessageBox to further indicate the purpose of the content::

  messagebox.setIcon(icon)

The *icon* parameter should be set to:

* ``QMessageBox.NoIcon``
* ``QMessageBox.Question``
* ``QMessageBox.Information``
* ``QMessageBox.Warning``
* ``QMessageBox.Critical``

=======
Example
=======
Below is an example of a MessageBox:

.. literalinclude:: _examples/messagebox.py

Download: :download:`MessageBox <_examples/messagebox.py>`
