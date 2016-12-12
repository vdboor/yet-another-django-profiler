yet-another-django-profiler Changelog
=====================================

1.1.0 (2016-12-12)
------------------
* Added support for Django 1.10 (including the new ``MIDDLEWARE`` setting)
* Dropped support for Django 1.5 and 1.6
* Fixed profiling of management commands with arguments in Django 1.8+
* Redirect stderr of the profiled command to be the same as the ``profile``
  command's stderr

1.0.3 (2016-02-08)
------------------
* Fixed profiling of Django admin pages (by removing profiling parameters
  before executing the view)
* Convert the PYTHONPATH to absolute paths for the subprocess used to run
  gprof2dot when generating call graphs (fixes problems loading setting files,
  etc.)
* Correctly profile views which return a StreamingHttpResponse (up through
  creation of the response, not including iteration over the content)

1.0.2 (2015-12-08)
------------------
* Support for Django 1.9

1.0.1 (2015-08-15)
------------------
* Add URL and command line parameter for yappi clock type

1.0.0 (2015-07-17)
------------------
* Support for Django 1.8
* Support for Python 3 and PyPy
* Option to use Yappi instead of cProfile as the profiler
* Internationalization (English and Japanese for now, other languages welcome)

0.3.0 (2015-02-23)
------------------
* Added "profile" management command for profiling other management commands
* Attempt to resolve absolute paths of Python modules to fully-qualified module
  names for more readable results, and added 2 new settings to customize this
* Upgraded gprof2dot.py (still bundled despite a recent version now being
  available on PyPI because it is slightly modified to use the new module name
  derivation code)
* Work around bug in Python >= 2.7.4 that doesn't recognize "file" as a valid
  sorting option (even though every other initial substring of "filename" is)

0.2.0 (2015-02-12)
------------------
Don't require particular Django versions (so pip won't try to auto-adjust it).

0.1.0 (2014-02-27)
------------------
Initial release
