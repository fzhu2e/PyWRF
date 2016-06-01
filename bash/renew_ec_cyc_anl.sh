#!/usr/bin/env bash

cd $RESULTS
rm -rf OSSE
cp -r OSSE_ec_cyc_anl_bak OSSE
cp OSSE/real/2012102618/wrf* $WRF/run_OSSE
cd -

exit 0
