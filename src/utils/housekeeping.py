from os import mkdir
from os.path import isdir

from importlib.metadata import version
from src.utils.logger import Logger


def log_pkg_ver(pkgimports: list[str], log_: Logger) -> None:
    for pkg_ in pkgimports:
        log_.info(f"Import {pkg_} v {version(pkg_)}")


def fix_dir(path_arr: list[str], log_: Logger) -> None:
    missing_path: list[str] = []
    for dir_ in path_arr:
        if not isdir(dir_):
            missing_path.append(dir_)
        log_.info(
            f"Skipping: {dir_}, path exists ..."
        )

    for dir_ in missing_path:
        try:
            mkdir(dir_)
            missing_path.remove(dir_)
        except OSError as err_:
            log_.crit(
                err_, f"Cannot create DIR: {dir_}"
            )

    if missing_path:
        log_.info(
            f"Unable to create the ff. DIR: {missing_path}."
        )
