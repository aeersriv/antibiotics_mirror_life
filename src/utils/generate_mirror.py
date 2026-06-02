#
# Pedroni et al. (c) 2025
# Creative Commons Attribution 4.0 International
#
# Aërium Srīvus (c) 2025
# GNU General Public License v 3 (GPLv3)
#
# The original script was refactored such that it can be
# used as module, not as a script as the original author once
# intended.
#
# This allows it to be used as an import for further processing
# such as in Jupyter notebooks or other scripts.

from typing_extensions import Self

from src.utils.logger import Logger


class MirrorTarget:
    """Mirror the structure of target."""

    def __init__(self: Self, log_: Logger) -> None:
        self.log_: Logger = log_


    def invert_pdb(self: Self, pdbid: str, path: str) -> None:
        """Read a PDB file, and manually invert the sign of
        each x, y, and z coordinates in HETATM and ATOM lines.

        Args:
            pdbid (str): file path of native target.
            path (str): output where to save the mirror target.
        """

        self.log_.info(f"Inverting the structure of {pdbid} ...")
        mirror_pdb = f"{path}/L-{pdbid.split('/')[-1]}"
        with (
                open(pdbid, "r", encoding="utf-8") as d_pdb,
                open(mirror_pdb, "w", encoding="utf-8") as l_pdb
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

        self.log_.info(f"Saved mirror of {pdbid} as {mirror_pdb}.")
