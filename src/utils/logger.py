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


    def logger(self, exception_: str, msg_: str) -> None:
        """Log the proccesses using passed message and exception_ variable.

        Args:
            exception_ -- determines what type of log level to use
            msg_ -- message to be logged.
        """

        match exception_:
            case "E": # for major error
                self.log.critical("%s", msg_)
            case "e":
                self.log.error("%s", msg_)
            case "I": # to print information in the terminal
                self.log.info("%s", msg_)
