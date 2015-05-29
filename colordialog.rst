ColorDialog
===========
The ColorDialog widget provides a colour chooser positioned within a dialog. This allows the user to select a range of colours from a palette or by entering colour values.

.. note::

  By default, the ColorDialog used is Qt's own native widget. It is also possible to use the platform native dialog instead, however this may behave differently.

===========
Constructor
===========
To construct the ColorDialog, use the call::

  colordialog = QColorDialog(parent)

The *parent* argument supplied indicates the widget (i.e. window) which owns the ColorDialog.

=======
Methods
=======
Display of the ColorDialog is done using the call::

  colordialog.open()

To obtain the colour information from the dialog use::

  colordialog.selectedColor()

The current colour displayed on the dialog can also be retrieved via::

  colordialog.currentColor()

Alternatively, it can be set programatically with::

  colordialog.setCurrentColor(color)

The *color* parameter should be set to an appropriate :doc:`color` object.

Options configuring the ColorDialog can be set using::

  colordialog.setOption(option, setting)

The *setting* parameter should be set to a Boolean value indicating whether the option is enabled or not. The *option* value can be set to any of the following:

* ``QColorDialog::ShowAlphaChannel``
* ``QColorDialog::NoButtons``
* ``QColorDialog::DontUseNativeDialog``

Using the ``QColorDialog::ShowAlphaChannel`` value allows the user to select the colour transparency. If ``QColorDialog::NoButtons`` is used, the dialog will show no buttons at the bottom. The ``QColorDialog::DontUseNativeDialog`` attempts to use the native platform dialog if possible.

The options in use can be retrieved from the ColorDialog by calling::

  colordialog.options()
