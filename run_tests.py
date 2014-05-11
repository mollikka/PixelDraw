try:
    import coverage
    cov_mode = True
except ImportError:
    print "coverage.py not found"
    cov_mode = False

if cov_mode:
    cov = coverage.coverage()
    cov.start()

import unittest

if __name__ == "__main__":

    testsuite = unittest.TestLoader().discover("test")
    unittest.TextTestRunner().run(testsuite)


if cov_mode:
    cov.stop()
    cov.save()
    cov.html_report(directory='coverage', omit=['/usr/*','test/*','*/__init__.py'])

