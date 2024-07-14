

rule spectrum_smoothing:
    input:
        "boardreflect_nonorm"
    output:
        "smoothed.nc"
    shell:

rule chl_value:
    input:
        "smoothed.nc"
    output:
        "sder.nc"
        "chl_value.nc"
    shell:

rule chl_map
    input
        "chl_value.nc"
    output
        "chl_map.fig"

# or just straight to
rule chl_value:
    input:
        "boardreflect_nonorm.nc",
    output:
        "chl_value.nc"
    shell:

rule chl_map
    input
        "chl_value.nc"
    output
        "chl_map.fig"

