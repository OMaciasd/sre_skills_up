import sys
import os

base_path = os.path.dirname(os.path.abspath(__file__))
myapp_path = os.path.join(base_path, 'docker', 'myapp')

sys.path.insert(0, myapp_path)
