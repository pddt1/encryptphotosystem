import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import *

def power(a, d, n):
  ans = 1
  while d != 0:
    if d % 2 == 1:
      ans = ((ans % n) * (a % n)) % n
    a = ((a % n) * (a % n)) % n
    d >>= 1
  return ans


# Encryption
def encrypt(image, e, n):
  row, col = image.shape[0], image.shape[1]
  encrypted = np.zeros([image.shape[0], image.shape[1], 3])
  encrypted_image = image.copy()

  for i in range(0, row):
    for j in range(0, col):
      r, g, b = image[i,j]
      C_R = power(r, e, n)
      C_G = power(g, e, n)
      C_B = power(b, e, n)

      encrypted[i][j] = [C_R, C_G, C_B]

      C_R = C_R % 256
      C_G = C_G % 256
      C_B = C_B % 256
      encrypted_image[i,j] = [C_R, C_G, C_B]
  return encrypted_image, encrypted


# Decryption
def decrypt( encrypted, d, n):
  row, col =  len(encrypted),len(encrypted[0])
  image = np.zeros([row, col, 3],dtype=np.uint8)

  for i in range(0, row):
    for j in range(0, col):
      r, g, b = encrypted[i][j]
      M_R = power(r, d, n)
      M_G = power(g, d, n)
      M_B = power(b, d, n)
      image[i,j] = [M_R, M_G, M_B]
  return image


