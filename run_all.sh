#!/bin/bash
python process_pdfs_batch.py 0 5 &
python process_pdfs_batch.py 5 10 &
python process_pdfs_batch.py 10 15 &
python process_pdfs_batch.py 15 20 &
python process_pdfs_batch.py 20 25 &
python process_pdfs_batch.py 25 30 &
python process_pdfs_batch.py 30 35 &
python process_pdfs_batch.py 35 40 &
python process_pdfs_batch.py 40 45 &
python process_pdfs_batch.py 45 50 &
python process_pdfs_batch.py 50 55 &
python process_pdfs_batch.py 55 60 &
python process_pdfs_batch.py 60 65 &
python process_pdfs_batch.py 65 70 &
python process_pdfs_batch.py 70 75 &
python process_pdfs_batch.py 75 80 &
python process_pdfs_batch.py 80 85 &
python process_pdfs_batch.py 85 90 &
python process_pdfs_batch.py 90 95 &
python process_pdfs_batch.py 95 100 &
python process_pdfs_batch.py 100 105 &
python process_pdfs_batch.py 105 110 &
python process_pdfs_batch.py 110 115 &
python process_pdfs_batch.py 115 120 &
python process_pdfs_batch.py 120 125 &
python process_pdfs_batch.py 125 128 &
wait
print 'All done'
