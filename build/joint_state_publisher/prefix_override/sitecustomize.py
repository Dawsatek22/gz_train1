import sys
if sys.prefix == '/home/d22/pipbot':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/d22/gz_projects/gz_ws/install/joint_state_publisher'
