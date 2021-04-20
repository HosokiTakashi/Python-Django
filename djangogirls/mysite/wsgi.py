import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectname.settings")


application = Cling(get_wsgi_application())