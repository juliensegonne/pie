import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


test="2023-06-25;08:30:00"
heure_obj = datetime.strptime(test, '%Y-%m-%d;%H:%M:%S')
print(heure_obj)