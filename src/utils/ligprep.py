#
# Aërium Srīvus (c) 2025
# GNU General Public License v 3 (GPLv3)
#

from subprocess import run

from src.utils.logger import Logger
from typing_extensions import Self


class LigPrep:
    """Ligand Preparation Tool."""

    def __init__(self: Self, log_: Logger) -> None:
        self.log_: Logger = log_


    def ligand_prep_invidual(
            self: Self,
            lig_path: str,
            name: str,
            path: str,
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
        self.log_.info(f"Scrubing {name} with {' '.join(scrub_cmd)}")
        _scrub_cmd_ = run(scrub_cmd)

        if _scrub_cmd_.returncode == 0:
            self.log_.info(f"Failed to run MolScrub on {name}")
            return None

        mkprepligand_cmd: list[str] = [
                "mk_prepare_ligand.py",
                "-i", f"{path}/scrub/{name}-scrub.sdf",
                "-o", f"{path}/{name}-prepped.pdbqt"
            ]
        self.log_.info(
            "Running mk_prepapre_ligand.py on "
            f"{name} with {' '.join(mkprepligand_cmd)}"
        )
        _mkprepligand_cmd_ = run(mkprepligand_cmd)

        if _mkprepligand_cmd_.returncode == 0:
            return None

        return name

    def ligand_prep_batch(
            self: Self,
            smi_file: str,
            out_file: str,
            path: str
        ) -> None:
        """Batch preparation of ligand.

        Args:
            smi_path (str): Path of smiles for preparation.
            out_path (str): Path for saving of prepared ligands.
        """
        scrub: str = f"{path}/scrubbed"
        prepd: str = f"{path}/prepped"

        pH: float = 7.4
        scrub_out: str = f"{smi_file}-scrubbed.sdf"

        scrub_cmd: list[str] = [
                "scrub.py",
                f"{path}/{smi_file}",
                "-o",
                f"{scrub}/{scrub_out}",
                f"--ph {pH}",
                "--skip_tautomer"
            ]
        self.log_.info(
            f"Batch scrubing {smi_file} with {' '.join(scrub_cmd)}"
        )
        _scrub_cmd_ = run(scrub_cmd)

        if _scrub_cmd_.returncode == 0:
            self.log_.info(
                f"Failed to run batch scrubbing of {smi_file}"
            )
            raise SystemExit

        mkprepligand_cmd: list[str] = [
                "mk_prepare_ligand.py",
                "-i", f"{scrub}/{scrub_out}",
                f"--multimol_outdir {prepd}"
            ]
        self.log_.info(
            f"Batch mk_prepapre_ligand.py on {scrub}"
            f"/{scrub_out} with {' '.join(mkprepligand_cmd)}"
        )
        _mkprepligand_cmd_ = run(mkprepligand_cmd)

        if _mkprepligand_cmd_.returncode == 0:
            raise SystemExit
