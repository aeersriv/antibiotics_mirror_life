#
# Aërium Srīvus (c) 2025
# GNU General Public License v 3 (GPLv3)
#

from subprocess import run


def ligand_prep(
        ligand: str,
        cid: str,
        path: str
    ) -> str | None:
    """Prepare the structure of ligand.

    Args:
        ligand (Mol): rdkit.Chem.rdchem.Mol instance of ligand.
        path (str): output path where to save the prepared
        ligand.
    """

    pH: float = 7.4

    scrub_cmd: list[str] = [
            "scrub.py",
            ligand,
            "-o",
            f"{path}/{cid}-scrub.sdf",
            "--ph", str(pH),
            "--skip_tautomer",
            "--skip_acidbase"
        ]
    print(
        f"Scrubing {cid} with {' '.join(scrub_cmd)}"
    )
    _scrub_cmd_ = run(scrub_cmd)

    if _scrub_cmd_.returncode == 1:
        return None

    mkprepligand_cmd: list[str] = [
            "mk_prepare_ligand.py",
            "-i", f"{path}/{cid}-scrub.sdf",
            "-o", f"{path}/{cid}-prepped.pdbqt"
        ]
    print(
        f"Preparing {cid} with {' '.join(mkprepligand_cmd)}"
    )
    _mkprepligand_cmd_ = run(mkprepligand_cmd)

    if _mkprepligand_cmd_.returncode == 1:
        return None

    return cid
