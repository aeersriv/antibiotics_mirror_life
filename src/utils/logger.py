import logging
from datetime import datetime
from os import mkdir, remove
from os.path import isdir, exists
from pathlib import Path
from typing import Self, Any

from rich.logging import RichHandler


class Logger:
    """ Custom logger. """

    def __init__(self: Self, log_file_: str) -> None:
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

        BASE_PATH: Path = Path("./logs/")
        log_filepath: Path = BASE_PATH / f"{log_file_}.log"

        if not isdir(BASE_PATH):
            self.info(
                f"Missing log dir {BASE_PATH}, creating ..."
            )
            try:
                mkdir(BASE_PATH)
            except OSError as os_err_:
                self.crit(os_err_, f"Cannot create {BASE_PATH}.")
                raise SystemExit from os_err_

        if exists(log_filepath):
            self.info(
                f"{log_filepath} already exists! Removing file ..."
            )
            remove(log_filepath)

        file_log: logging.FileHandler = logging.FileHandler(
                filename=log_filepath
            )

        file_log.setLevel(logging.INFO)
        file_log.setFormatter(
            logging.Formatter("%(levelname)s %(message)s")
        )
        self.log.addHandler(file_log)

        self.info(
            "Setup of logger complete, started "
            f"<{log_file_}> {str(datetime.now())}"
        )


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

    def info(self, msg_: str) -> None:
        """Likely important information.

        Args:
            msg_ -- message to be logged.
        """

        self.log.info("%s", msg_)
