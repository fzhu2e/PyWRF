#!/usr/bin/env bash

cd $RESULTS
rm -rf OSSE
cp -r OSSE_ec_multi_bak OSSE
rm -f $WRF/run_OSSE/wrfbdy*
rm -f $WRF/run_OSSE/wrfinput*
rm -f $WRF/run_OSSE/wrfvar*
cd -

exit 0
