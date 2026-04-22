#
# ÆĒR ŚRĪV (c) 2025
# GNU General Public License v 3 (GPLv3)
#


from rdkit import Chem
from rdkit.Chem import Mol, AllChem


def ligand_prep(ligand: Mol, name: str):
    mol = Chem.AddHs(ligand)
    _ = AllChem.EmbedMolecule(mol)
    AllChem.MMFFOptimizeMolecule(mol) # optimize molecule with MMFF94
    Chem.MolToMolFile(mol, f"{name}.mol")
