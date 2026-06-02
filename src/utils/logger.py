import logging
from pathlib import Path
from typing import Self, Any

from rich.logging import RichHandler


class Logger:
    """ Custom logger. """

    def __init__(self: Self) -> None:
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


    def crit(self: Self, exception_: Any, msg_: str) -> None:
        """Critical errors.

        Args:
            exception_ -- stderr from raised exception.
            msg_ -- message to be logged.
        """

        self.log.critical("%s: %s", exception_, msg_)

    def err(self, exception_: Any, msg_: str) -> None:
        """Minor but tolerable errors.

        Args:
            exception_ -- stderr from raised exception.
            msg_ -- message to be logged.
        """

        self.log.error("%s: %s", exception_, msg_)

    def info(self, exception_: Any, msg_: str) -> None:
        """Likely important information.

        Args:
            exception_ -- stderr from raised exception.
            msg_ -- message to be logged.
        """

        self.log.info("%s: %s", exception_, msg_)
