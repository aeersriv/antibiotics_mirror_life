#
# Aërium Srīvus (c) 2025
# GNU General Public License v 3 (GPLv3)
#

from subprocess import run


def ligand_prep(
        ligand: str,
        name: str,
        path: str
    ) -> str | None:
    """Prepare the structure of ligand.

    Args:
        ligand (Mol): rdkit.Chem.rdchem.Mol instance of ligand.
        path (str): output path where to save the prepared
        ligand.
    """
    pH: float = 7.0
    PDBQT_name: str = f"{name}.pdbqt"
    SDF_name: str = f"{name}.sdf"

    scrub: list[str] = [
            "scrub.py",
            ligand,
            "-o",
            f"{path}/{SDF_name}",
            "--ph", str(pH),
            "--skip_tautomer",
            "--skip_acidbase"
        ]
    print(
        f"Scrubing {name} with {' '.join(scrub)}"
    )
    proc = run(scrub)
    if proc.returncode == 1:
        return None

    input_mk = f"{path}/{SDF_name}"
    output_mk = f"{path}/{PDBQT_name}"
    mkprepligand: list[str] = [
            "mk_prepare_ligand.py",
            "-i", input_mk,
            "-o", output_mk
        ]
    print(
        f"Preparing {name} with {' '.join(mkprepligand)}"
    )
    proc = run(mkprepligand)

    return name
