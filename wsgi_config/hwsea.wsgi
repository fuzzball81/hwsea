activate_this = '/home/<user>/virtualenvs/flask/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/home/<user>/devel/hwsea')


from main import app as application
