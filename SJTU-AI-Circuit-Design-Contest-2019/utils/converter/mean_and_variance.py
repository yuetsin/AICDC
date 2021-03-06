#!/usr/bin/env python

import IR
import numpy as np
from PIL import Image

stuff_buf = IR.stuff

r_vs = []
g_vs = []
b_vs = []

for cat in stuff_buf:
    for img_entry in cat:
        print(img_entry)

        file_path = img_entry[0]
        assert(type(file_path) == str)

        im = Image.open(file_path)
        width, height = im.size

        for wi in range(width):
            for hi in range(height):
                v = im.getpixel((wi, hi))
                assert(len(v) == 3)

                r_vs.append(v[0] / 255.0)
                g_vs.append(v[1] / 255.0)
                b_vs.append(v[2] / 255.0)

r_mean = np.mean(r_vs)
print("Done with r_mean: %8f" % r_mean)

g_mean = np.mean(g_vs)
print("Done with g_mean: %8f" % g_mean)

b_mean = np.mean(b_vs)
print("Done with b_mean: %8f" % b_mean)

r_variance = np.var(r_vs)
print("Done with r_variance: %8f" % r_variance)

g_variance = np.var(g_vs)
print("Done with g_variance: %8f" % g_variance)

b_variance = np.var(b_vs)
print("Done with b_variance: %8f" % b_variance)

print("""
(つД`)ノ

===== MEAN ===== 
R: %.8f
G: %.8f
B: %.8f

=== VARIANCE ===
R: %.8f
G: %.8f
B: %.8f

EOF
""" % (r_mean, g_mean, b_mean, r_variance, g_variance, b_variance))
