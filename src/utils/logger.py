import logging
from pathlib import Path

from rich.logging import RichHandler


class Logger:
    """ Custom logger. """

    def __init__(self) -> None:
        logging.basicConfig(
            format="%(message)s",
            level=logging.INFO,
            datefmt="[%X]",
            handlers=[
                    RichHandler(
                        show_time=False,
                        show_path=False
                    )
                ]
        )

        self.log: logging.Logger = logging.getLogger("rich")

        BASE_PATH: Path = Path(".")
        file_log: logging.FileHandler = logging.FileHandler(
                filename=f"{BASE_PATH}/simtex.log"
            )

        file_log.setLevel(logging.INFO)
        file_log.setFormatter(
            logging.Formatter("%(levelname)s %(message)s")
        )
        self.log.addHandler(file_log)


    def crit(self, msg_: str) -> None:
        """Critical errors.

        Args:
            msg_ -- message to be logged.
        """

        self.log.critical("%s", msg_)

    def err(self, msg_: str) -> None:
        """Minor but tolerable errors.

        Args:
            msg_ -- message to be logged.
        """

        self.log.error("%s", msg_)

    def info(self, msg_: str) -> None:
        """Likely important information.

        Args:
            msg_ -- message to be logged.
        """

        self.log.info("%s", msg_)
