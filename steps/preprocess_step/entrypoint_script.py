import sys
print('hello from hub container v5')
print('hub arguments:', sys.argv)
f = open("/tmp/output.txt", "a")
f.write("Finished successfully")
f.close()
f = open("/data/mydata.txt", "a")
f.write("1:2:3")
f.close()

print('bye from hub container')