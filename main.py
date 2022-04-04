from vulners_module import *
from render_vulners_bulletin import *


def generate_bulletin(cve):
    data = render_bulletin(get_bulletins(cve))
    f = open("{}.html".format(cve), "wb")
    f.write(data.encode())
    f.close()