The openEHR Information Model package.

This is the original set of interfaces and classes that started OSHIP.  I originally wanted to keep as close
to the openEHR documents as posssible.

However, as we proceeded I found more and more that we were duplicating functionality that was already
present in the Grok/Zope3 framework.  This was a huge waste of time and effort.

I will leave this code in this branch for anyone that wants to continue a more pure Python implementation.
For the main version and the one I will be working on I will use as much of the framework as posssible and 
still consume and deliver openEHR archtype enabled data.

2009-01-27

Tim Cook


