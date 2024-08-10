import sys
import os

# Configura la ruta base relativa al directorio actual
base_path = os.path.dirname(os.path.abspath(__file__))
myapp_path = os.path.join(base_path, 'docker', 'myapp')

# Agrega la ruta al sys.path
sys.path.insert(0, myapp_path)
