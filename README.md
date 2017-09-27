# python-compress

Small application takes a file or directory and compresses. It won't actually write out any of the compressed files but will display a metric for a "how much will my data compress".

It will compress in various block sizes. It currently only supports lz4. The new intel Skylake processors support QAT offloading and thus gzip-qat is planned for the future.

Usage:

python compress.py <file|dir>
