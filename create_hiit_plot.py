import sys
import random

colors = ['yafcolor5', 'yafcolor2', 'yafcolor3']

for x in open(sys.argv[1]):
	f = [int(y) for y in x.split()]
	r = [0.2*random.random() for y in range(6)]
	r[0] = r[2] = r[4] = 0

	print '\\addplot+[no markers, yafcolor5, opacity=0.5] coordinates {(%f, %f) (%f, %f) (%f, %f)};' % (3 * f[1] + r[0], f[2] + r[1], 3 * f[1] + 1 + r[2], f[3] + r[3], 3 * f[1] + 2 + r[4], f[4] + r[5])
