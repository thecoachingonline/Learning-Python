import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so


import seaborn as sns
df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")

import matplotlib.pyplot as plt
plt.show()