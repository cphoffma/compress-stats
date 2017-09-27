import os
import lz4.block
import sys
def traverse(path):
	cwd = path
	stack = []
	files = []
	count=0
	while(True):
	        start = os.listdir(cwd)
	        for inside in start:
	                full = cwd+inside
			if os.path.islink(full):
				a=1
			elif os.path.isfile(full):
				files.append("" + full)
				count+=1
				if count % 10000 == 0:
					print full
					print "The count is:",count
			
	                elif os.path.isdir(full):
	                        stack.append(full+"/")
	        if stack:
	                cwd = stack.pop()
	        else:
	                break
	return files


print sys.argv[1]
files = traverse(sys.argv[1])
record_size = 1048576 #1MB
orig_size = 1
comp_size = 1
file_count = 0
#print files
print "# of inodes:",len(files)
for file in files:
	file_count+=1
	with open(file) as f:
		buff = f.read(record_size)	
		while (buff):
			orig_size += len(buff)
			compressed_data = lz4.block.compress(buff)
			comp_size += len(compressed_data)
			buff = f.read(record_size)
	if file_count % 10 == 0:
		print "compression ratio:"+ str((float(orig_size) / float(comp_size)))
print "compression ratio:"+ str((float(orig_size) / float(comp_size)))
print orig_size
print comp_size

