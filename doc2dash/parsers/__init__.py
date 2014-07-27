from __future__ import absolute_import, division, print_function

from . import pydoctor, sphinx, intersphinx


DOCTYPES = [
    intersphinx.InterSphinxParser,
    sphinx.SphinxParser,
    pydoctor.PyDoctorParser,
]


def get_doctype(path):
    """
    Gets the apropriate doctype for *path*.
    """
    for dt in DOCTYPES:
        if dt.detect(path):
            return dt
    else:
        return None
