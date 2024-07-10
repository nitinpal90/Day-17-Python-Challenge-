#!/usr/bin/env python
# coding: utf-8

# # Day-17 Python Challenge 

# # Matplotlib Library Part - 2

# In[1]:


import matplotlib.pyplot as plt


# # Image Formatting With Diffrent Colors

# In[12]:


#Importing libraries

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

iname = r'istockphoto-183412466-612x612.jpg'
plt.title("Birds Image")

#Opning imgae from PIL

image = Image.open(iname).convert('L')

# Mapping image to gray scale

plt.imshow(image, cmap = 'gray')
plt.show()


# In[13]:


#Importing libraries

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

iname = r'istockphoto-183412466-612x612.jpg'
plt.title("Birds Image")

#Opning imgae from PIL

image = Image.open(iname).convert('L')

# Mapping image to gray scale

plt.imshow(image, cmap = 'YlOrRd_r')
plt.show()


# In[18]:


#Importing libraries

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

iname = r'istockphoto-183412466-612x612.jpg'
plt.title("Birds Image")

#Opning imgae from PIL

image = Image.open(iname).convert('L')

# Mapping image to gray scale

plt.imshow(image, cmap = 'coolwarm')
plt.show()


# In[20]:


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

iname = r'istockphoto-183412466-612x612.jpg'
plt.title("Birds Image")

#Opning imgae from PIL

image = Image.open(iname).convert('L')

# Mapping image to gray scale

plt.imshow(image, cmap = 'nipy_spectral_r')
plt.show()


# In[29]:


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

iname = r'python.jpg'
plt.title("Guido van Rossum")

image = Image.open(iname).convert('L')

plt.imshow(image)
plt.show()


# In[33]:


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

iname = r'python.jpg'
plt.title("Guido van Rossum")

image = Image.open(iname).convert('L')

plt.imshow(image, cmap = 'YlOrBr_r')
plt.show()


# # Pie Chart

# In[44]:


import matplotlib.pyplot as pd

x = [10, 20, 30, 40, 50]
y = ['English', 'Hindi', 'Physics', 'Science', 'Maths']
plt.title("Class Subject")
plt.xlabel("Subject Distribution")
plt.pie(x, labels = y)
plt.show()

