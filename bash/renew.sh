#!/usr/bin/env bash

cd $RESULTS
rm -rf OSSE
cp -r OSSE_bak OSSE
rm -f $WRF/run_OSSE/wrfbdy*
rm -f $WRF/run_OSSE/wrfinput*
rm -f $WRF/run_OSSE/wrfvar*
cp OSSE/wrf/2012102518/wrfvar* $WRF/run_OSSE/
cd -

exit 0
