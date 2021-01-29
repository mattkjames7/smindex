# smindex
A tiny module for reading SuperMAG indices and substorm lists.

For the SuperMAG data visit https://supermag.jhuapl.edu/indices

## Installation

Install this module using `pip3`:

```bash
pip3 install smindex --user
```

Or by cloning and building this repository:

```bash
git clone https://github.com/mattkjames7/smindex
cd smindex
python3 setup.py bdist_wheel
pip3 install dist/smindex-1.0.0-py3-none-any.whl --user
```

Then set up an environment variable which point to where you want to store the data in your `~/.bashrc` file:

```bash
export SMINDEX_PATH = /path/to/smindex/data/
```

## Downloading Indices

For best results, visit the indices page on the SuperMAG website and select the following indices to download:

SME U/L, SME, SME MLT, SME MLAT, SME LT, SMU LT, SML LT, SMR, SMR LT

The data format should be ASCII and ideally download full year files.

These data files should then be placed in the directory `$SMINDEX_PATH/download` where they can be processed.

They can be converted to a binary format which is quick to read:

```python
import smindex
smindex.ConvertData()
```

## Read Indices

Use the `smindex.GetIndices`function to read the converted index files:

```python 
#Read a single year file
data = smindex.GetData(2005)

#or a range of years
data = smindex.GetData([2005,2008])
```



