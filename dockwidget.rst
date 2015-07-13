DockWidget
==========
A DockWidget provides a widget which is able to be docked inside the main window, or placed in its own separate window. The widget is useful for holding widgets where it would be useful to separate them from the main interface.
===========
Constructor
===========
The widget is constructed via::

  dockwidget = QDockWidget()

=======
Methods
=======
Adding the child widget is done using::

  dockwidget.setWidget(widget)

The palette can be set to floating programmatically via::

  dockwidget.setFloating(float)

The floating status of the DockWidget can also be retrieved with::

  dockwidget.floating()

A number of customisations can be made to the DockWidget with the method::

  dockwidget.setFeatures(features)

The features list can include the following::

* ``QDockWidget.DockWidgetClosable`` - allow the DockWidget to be closed.
* ``QDockWidget.DockWidgetMovable`` - allow the DockWidget to be moved.
* ``QDockWidget.DockWidgetFloatable`` - allow the DockWidget to be floated.
* ``QDockWidget.DockWidgetVerticalTitleBar`` - set the title bar vertically.
* ``QDockWidget.DockWidgetNoDockWidgetFeatures`` - turn off all features.

An arbitary widget can be set for use in the DockWidget title bar. This could be a container containing several widgets, or a single widget. They are set via::

  dockwidget.setTitleBarWidget(widget)

=======
Example
=======
Below is an example of an DockWidget:

.. literalinclude:: _examples/dockwidget.py

Download: :download:`DockWidget <_examples/dockwidget.py>`
