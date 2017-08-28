## osuex

Command line interface and python module for linux users to peacefully extract osu files
Works out of the box for PlayOnLinux users (See below)


### Installation

```
pip install osuex
```

Or install from source by cloning the repository and running as root

```
python setup.py install
```

### Command Line

```
Usage: osuex [OPTIONS]

  Tool to search BOARD for TEXT in the title or OP's post.

Options:
  -o, --osufilesdir TEXT   Directory with osu files for extraction
  -b, --beatmapsdir TEXT   Board to search
  -t, --skinsdir    TEXT   Directory to extract skins to
  --help             Show this message and exit.
```
If using PlayOnLinux, navigate to directory containing osz and osk files and run

```
osuex
```