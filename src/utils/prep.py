#
# ÆĒR ŚRĪV (c) 2025
# GNU General Public License v 3 (GPLv3)
#

from rdkit import Chem
from rdkit.Chem.rdchem import Mol
from rdkit.Chem import AllChem


def ligand_prep(ligand: Mol, path: str):
    """Prepare the structure of ligand.

    Args:
        ligand (Mol): rdkit.Chem.rdchem.Mol instance of ligand.
        path (str): output path where to save the prepared
        ligand.
    """

    mol = Chem.AddHs(ligand)
    _ = AllChem.EmbedMolecule(mol)
    AllChem.MMFFOptimizeMolecule(mol) # optimize molecule with MMFF94
    Chem.MolToMolFile(mol, f"{path}.mol")
