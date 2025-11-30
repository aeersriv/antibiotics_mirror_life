import sys


def invert_pdb_coordinates(pdb_file):
    '''
    1. Reads a PDB file, inverts the signs of the x, y, z coordinates in HETATM and ATOM lines.
    2. Writes a new PDB file with inverted coordinates named with the same prefix and "_specular.pdb suffix".
    '''
    specular_pdb_file = f'{pdb_file[:-4]}pecular.pdb'
    with open(pdb_file, 'r') as infile, open(specular_pdb_file, 'w') as outfile:
        for line in infile:
            if line.startswith('HETATM') or line.startswith('ATOM'):
                x = float(line[30:38])
                x = -x
                y = float(line[38:46])
                y = -y
                z = float(line[46:54])
                z = -z
                newline = f'{line[:30]}{x:8.3f}{y:8.3f}{z:8.3f}{line[54:]}' # line containing coordinates with inverted signs
                outfile.write(newline)
            else:
                outfile.write(line) # Write other lines unchanged

            print(f'Specular PDB file saved as {specular_pdb_file}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 pdb_mirror.py <pdb_file.pdb>')
        sys.exit(1)
    pdb_file = sys.argv[1]
    invert_pdb_coordinates(pdb_file)
