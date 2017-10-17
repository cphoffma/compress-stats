# compress-stats

Small application takes a file or directory and compresses. It won't actually write out any of the compressed files but will display a metric for a "how much will my data compress".

It will compress in various block sizes. The new intel Skylake processors support QAT offloading and thus gzip-qat is planned for the future.

usage: compress.py [-h] [-d DIRECTORY] [-a ALGO] [-s SIZE] [--version]

optional arguments:
  -h, --help    show this help message and exit
  -d DIRECTORY  Directory to start scan
  -a ALGO       Compression algorithm to use [lz4|gzip9]
  -s SIZE       Record/block size to compress upon (bytes)
  --version     show program's version number and exit

