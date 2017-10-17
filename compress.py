import argparse
import os
import lz4.block
import zlib
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
			
	                elif os.path.isdir(full):
	                        stack.append(full+"/")
	        if stack:
	                cwd = stack.pop()
	        else:
	                break
	return files

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', action='store', dest='directory', help='Directory to start scan')
	parser.add_argument('-a', action='store', dest='algo', default='lz4', help='Compression algorithm to use [lz4|gzip9]', type=str)
	parser.add_argument('-s', action='store', dest='size', default='1048576', help='Record/block size to compress upon (bytes)', type=int)
	parser.add_argument('--version', action='version', version='%(prog)s .1')
	results=parser.parse_args()

	files = traverse(results.directory)
	record_size = int(results.size)
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
				compressed_data = orig_size
				if results.algo == 'lz4':
					compressed_data = lz4.block.compress(buff)
				elif results.algo == 'gzip9':
					compressed_data = zlib.compress(buff,9)
				comp_size += len(compressed_data)
				buff = f.read(record_size)

	print "compression ratio:"+ str((float(orig_size) / float(comp_size)))

main()

