__author__ = 'NamelessOne'

from string import Template
import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')


def render_from_string(template_string, mapping):
    """template_string is a template string. mapping is a dictionary containing
    values to be substituted into the template.

    $xx in the template will be replaced with the value of xx from the mapping dictionary.

    Returns a response suitable for the return value of
    a WSGI procedure."""

    template = Template(template_string)
    result = template.safe_substitute(mapping)

    return [result.encode()]


def render(templatename, mapping):
    """templatename is the name of a template file to be found
    in the TEMPLATE_DIR directory. mapping is a dictionary containing
    values to be substituted into the template.

    $xx in the template will be replaced with the value of xx from the mapping dictionary.

    Returns a response suitable for the return value of
    a WSGI procedure."""

    tpath = os.path.join(TEMPLATE_DIR, templatename)
    if not os.path.exists(tpath):
        print("Can't find template at:", tpath)
        return [b"Error processing template"]

    # read the template from the given file
    h = open(tpath, 'r')
    template = h.read()
    h.close()

    return render_from_string(template, mapping)