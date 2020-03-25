#!/usr/bin/env python3

import dask
import os
import xarray as xr


indir='/g/data/ub4/era5/netcdf/surface/SLHF'
year=int(os.getenv('YEAR', '2002'))

ds = xr.open_mfdataset(
        f'{indir}/{year}/*.nc',
        combine='by_coords',
        chunks={           
            'time':93,
            'latitude':91,
            'longitude':180
            }
        )
# chunk sizes can be found using ncdump -hs <file> ; these chunks are transfered to the output file too

# Update chunking
#for v in ds:
#     if 'chunksizes' in ds[v].encoding:
#         ds[v] = ds[v].chunk(ds[v].encoding['chunksizes'])


slhf=ds.slhf

dailymean=slhf.resample(time='1D').mean('time')

dailymean.attrs = slhf.attrs
dailymean.attrs['long_name'] = "Daily mean surface latent heat flux"

ds=xr.Dataset({'dmlhf':dailymean})

ds.to_netcdf(f'outfile_{year}.nc', 
        encoding={
            'dmlhf':{
                'zlib':True,
                'chunksizes':dailymean.data.chunksize,
                'complevel':5,
                'shuffle':True
                }
            })
