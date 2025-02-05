# smindex
A tiny module for reading SuperMAG indices and substorm lists.

For the SuperMAG data visit https://supermag.jhuapl.edu/indices

If using any of these data products, please remember to cite the relevant SuperMAG papers and acknowledge SuperMAG (see here: https://supermag.jhuapl.edu/info/?page=rulesoftheroad)

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

(follow this link: https://supermag.jhuapl.edu/indices/?layers=SMR.LT,SMR,SMER.L,SMER.U,SMER.E,SME.MLAT,SME.MLT,SME.E,SME.UL&fidelity=low&start=2001-01-30T00%3A00%3A00.000Z&step=14400&tab=download)

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



## Downloading Substorm Lists

Substorm lists (by Frey et al., 2004 and 2006; Liou 2010; Newell and Gjerloev, 2011; Forsyth et al., 2015; Ohtani and Gjerloev, 2020) can be downloaded from the following page: https://supermag.jhuapl.edu/substorms/?tab=download

The ASCII file format is readable by this module. The files should be placed in `$SMINDEX_PATH/substorms`.

Once you have all of the data files, they can be combined using the following function:

```python
smindex.UpdateSubstorms()
```

## Reading Substorms

The best way to read the substorm lists is to use the `GetSubstorms` function:

```python
#get everything:
ss = smindex.GetSubstorms()

#get a single date (25th January 2005 in this case)
ss = smindex.GetSubstorms(Date=20050125)

#get a range of dates
ss = smindex.GetSubstorms(Date=[20050101,20050125])
```

## References

Frey, H. U., Mende, S. B., Angelopoulos, V., and Donovan, E. F. (2004), Substorm onset observations by IMAGE‐FUV, J. Geophys. Res., 109, A10304, doi:10.1029/2004JA010607.

Frey, H.U. and Mende, S.B., 2006, March. Substorm onsets as observed by IMAGE-FUV. In Proceedings of the 8th International Conference on Substorms (pp. 71-76). Calgary, Alberta, Canada: Univ. of Calgary.

Forsyth, C., Rae, I. J., Coxon, J. C., Freeman, M. P., Jackman, C. M., Gjerloev, J., and Fazakerley, A. N. ( 2015), A new technique for determining Substorm Onsets and Phases from Indices of the Electrojet (SOPHIE), J. Geophys. Res. Space Physics, 120, 10,592– 10,606, doi:10.1002/2015JA021343.

Gjerloev, J. W. (2012), The SuperMAG data processing technique, J. Geophys. Res., 117, A09213, doi:10.1029/2012JA017683.

 Gjerloev, J. W., R. A. Hoffman, S. Ohtani, J. Weygand, and R. Barnes,  Response of the Auroral Electrojet Indices to Abrupt Southward IMF  Turnings (2010), Annales Geophysicae, 28, 1167-1182.

Liou, K. (2010),  Polar Ultraviolet Imager observation of auroral breakup, J. Geophys. Res.,  115, A12219, doi:10.1029/2010JA015578.

Newell, P. T., and J. W. Gjerloev (2011), Evaluation of SuperMAG auroral electrojet indices as indicators of substorms and auroral power, J. Geophys. Res., 116, A12211, doi:10.1029/2011JA016779.

Newell, P. T., and J. W. Gjerloev (2011), Substorm and magnetosphere characteristic scales inferred from the SuperMAG auroral electrojet indices, J. Geophys. Res., 116, A12232, doi:10.1029/2011JA016936.

Newell, P. T. and J. W. Gjerloev (2012), SuperMAG-Based Partial Ring  Current Indices, J. Geophys. Res., 117, doi:10.1029/2012JA017586.

Ohtani, S., and J. Gjerloev, Is the Substorm Current Wedge an Ensemble of Wedgelets?: Revisit to Midlatitude Positive Bays, accepted, J. Geophys. Res, 2020.