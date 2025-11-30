#
# Original by Patrick Kunzmann
# BSD 3 clause
# Modified by ÆĒR ŚRĪV (c) 2025
# GNU General Public License v3 (GPLv3)
#

import numpy as np
import biotite.structure as struc
import biotite.structure.io as strucio


def get_enantiomer(n, ca, c, cb):
    n = np.cross(ca - n, ca - c)
    sign = np.sign(np.dot(cb - ca, n))

    return sign


def analyze_chirality(array):
    array = array[struc.filter_amino_acids(array)]
    array = array[
            (
                array.atom_name == "CB"
            ) | (
                struc.filter_peptide_backbone(array)
            )
        ]
    ids, _ = struc.get_residues(array)
    enantiomers = np.zeros(len(ids), dtype=int)
    for i, id_ in enumerate(ids):
        coord = array.coord[array.res_id == id_]
        if len(coord) != 4:
            enantiomers[i] = 0
        else:
            enantiomers[i] = get_enantiomer(
                    coord[0], coord[1], coord[2], coord[3]
                )
    return enantiomers


def verify(pdb_file):
    stack = strucio.load_structure(pdb_file)
    array = stack[0]
    chirality = analyze_chirality(array)

    return (
        True
        if np.argmax(
            np.bincount(chirality)
        ) == -1
        else False
    )
