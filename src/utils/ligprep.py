#
# Aërium Srīvus (c) 2025
# GNU General Public License v 3 (GPLv3)
#

from subprocess import run

from src.utils.logger import Logger

def ligand_prep(
        lig_path: str,
        name: str,
        path: str,
        log_: Logger
    ) -> str | None:
    """_summary_

    Args:
        lig_path (str): Path of the ligand SDF.
        name (str): File name for the scrubbed and prepped ligand.
        path (str): Path where to save the ligand.
        logger (Logger): Logger file.

    Returns:
        str | None: A successful preparation will return the name of
            the ligand, whilst a failed will return None.
    """


    pH: float = 7.4

    scrub_cmd: list[str] = [
            "scrub.py",
            lig_path,
            "-o",
            f"{path}/scrub/{name}-scrub.sdf",
            "--ph", str(pH),
            "--skip_tautomer"
        ]
    log_.info(f"Scrubing {name} with {' '.join(scrub_cmd)}")
    _scrub_cmd_ = run(scrub_cmd)

    if _scrub_cmd_.returncode == 1:
        log_.info(f"Failed to run MolScrub on {name}")
        return None

    mkprepligand_cmd: list[str] = [
            "mk_prepare_ligand.py",
            "-i", f"{path}/scrub/{name}-scrub.sdf",
            "-o", f"{path}/{name}-prepped.pdbqt"
        ]
    log_.info(
        "Running mk_prepapre_ligand.py on "
        f"{name} with {' '.join(mkprepligand_cmd)}"
    )
    _mkprepligand_cmd_ = run(mkprepligand_cmd)

    if _mkprepligand_cmd_.returncode == 1:
        return None

    return name
