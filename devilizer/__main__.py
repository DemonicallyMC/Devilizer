import random

from devilizer.visualizer.visualize import visualize
from devilizer.sorting.bubble_sort import bubble_sort

lst = random.sample(range(1, 20), 19)
visualize(lst, bubble_sort)
