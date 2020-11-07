import sys
print('hello from build container v5')
print('build arguments:', sys.argv)
f = open("/tmp/output.txt", "a")
f.write("Finished successfully2")
f.close()
f = open("/data/mydata.txt", "r")
print('read line:', f.readline())
print('bye from build container')