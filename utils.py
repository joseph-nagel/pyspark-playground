'''Some utilities.'''

from pathlib import Path
from warnings import warn
from requests import get


def download_textfile(url, save_path):
    '''Download and save text file.'''

    save_path = Path(save_path)

    if save_path.exists():
        warn(f'{save_path} exists already, download skipped')

    else:
        # download text file
        response = get(url)

        # create save dir
        save_dir = save_path.parent

        if not save_dir.exists():
            save_dir.mkdir(parents=True, exist_ok=True)

        # save text file
        with open(save_path, mode='wb') as f:
            f.write(response.content)

