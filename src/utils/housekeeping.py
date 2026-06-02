from os import mkdir
from os.path import isdir

from importlib.metadata import version
from src.utils.logger import Logger


def log_pkg_ver(pkgimports: list[str], log_: Logger) -> None:
    for pkg_ in pkgimports:
        log_.info(f"Import {pkg_} v {version(pkg_)}")


def check_dir(path_arr: list[str], log_: Logger) -> list[str]:
    missing_path: list[str] = []
    for dir_ in path_arr:
        if isdir(dir_):
            log_.info(
                f"Skipping: {dir_}, path exists ..."
            )
            continue
        log_.info(
            f"{dir_} is missing, include to the list ..."
        )
        missing_path.append(dir_)

    return missing_path


def fix_dir(path_arr: list[str], log_: Logger) -> None:

    missing_path: list[str] = check_dir(path_arr, log_)
    if not missing_path:
        return None

    created_dir: list[str] = []
    for dir_ in missing_path:
        try:
            log_.info(f"Trying to create dir: {dir_}")
            mkdir(dir_)
        except OSError as err_:
            log_.crit(
                err_, f"Cannot create DIR: {dir_}"
            )
        else:
            created_dir.append(dir_)

    failed_dir: list[str] = list(
            set(missing_path)^set(created_dir)
        )
    if failed_dir:
        log_.info(
            f"Unable to create the ff. DIR: {failed_dir}."
        )

