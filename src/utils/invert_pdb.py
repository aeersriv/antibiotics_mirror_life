# Pedroni et al. (c) 2025
# Creative Commons Attribution 4.0 International
#
# ÆĒR ŚRĪV (c) 2025
# GNU General Public License v 3 (GPLv3)
#

""" The original script was refactored such that it can be
used as module, not as a script as the original author once
intended.

This allows it to be used as an import for further processing
such as in Jupyter notebooks or other scripts.
"""

def invert_pdb_coordinates(d_pdb_file):
    """
    1. Reads a PDB file pdb_file: str, inverts the signs of the
    x, y, z coordinates in HETATM and ATOM lines.
    2. Writes a new PDB file with inverted coordinates named with
    prefix L- and .pdb file extension
    """

    l_pdb_file = f"L-{d_pdb_file[1:]}"
    with (
            open(d_pdb_file, "r", encoding="utf-8") as d_pdb,
            open(l_pdb_file, "w", encoding="utf-8") as l_pdb
        ):
        for line in d_pdb:
            if line.startswith("HETATM") or line.startswith("ATOM"):
                # invert the signs to transpose the coordinates of
                # the given peptide structure to "mirror form."
                x = -1.0 * float(line[30:38])
                y = -1.0 * float(line[38:46])
                z = -1.0 * float(line[46:54])
                newline = f"{line[:30]}{x:8.3f}{y:8.3f}{z:8.3f}{line[54:]}"
                # line containing coordinates with inverted signs
                l_pdb.write(newline)
            else:
                l_pdb.write(line)
