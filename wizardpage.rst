WizardPage
==========
A WizardPage is the object holding the page content for display in the :doc:`wizard`.

===========
Constructor
===========
A WizardPage object can be constructed using::

  wizardpage = QWizardPage()

=======
Methods
=======
The title and subtitle can be set on a page using the calls::

  wizardpage.setTitle(title)
  wizardpage.setSubTitle(subtitle)

A page can be set to be the final page with::

  wizardpage.setFinalPage(final)

A commit page, which can be undone by clicking Back or Cancel can be set via::

  wizardpage.setCommitPage(commit)

To check whether a page has been completed call::

  wizardpage.isComplete()

Additional methods are available to check whether a page is either a commit or final page::

  wizardpage.isCommitPage()
  wizardpage.isFinalPage()

=======
Example
=======
The WizardPage example is a part of the Wizard widget example.
