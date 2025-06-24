#!/usr/bin/env python3
# filepath: make_gxdb/extract_exon_locs.py

import gzip
import sys

def parse_gff_for_exons(gff_file):
    """
    Extract exon locations from a GFF file and print them to stdout
    
    Args:
        gff_file: Path to the input GFF file
    """
    # Determine if input is gzipped
    open_func = gzip.open if gff_file.endswith('.gz') else open
    mode = 'rt' if gff_file.endswith('.gz') else 'r'
    
    with open_func(gff_file, mode) as infile:
        # Process each line
        for line in infile:
            # Skip comment lines
            if line.startswith('#'):
                continue
                
            fields = line.strip().split('\t')
            if len(fields) < 9:
                continue
                
            seq_id, source, feature_type, start, end = fields[0:5]
            
            # Extract only exon features
            if feature_type.lower() == 'exon':
                print(f"{seq_id}\t{start}\t{end}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <gff_file>\n")
        sys.exit(1)
    
    gff_file = sys.argv[1]
    parse_gff_for_exons(gff_file)