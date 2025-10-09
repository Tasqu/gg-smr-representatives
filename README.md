# gg-smr-representatives

Representative period selection for the GG-SMR project.

Let's see if we can do some representative period selection for the
[North European Backbone Model](https://github.com/vttresearch/north_european_model)
using [TSAM](https://github.com/FZJ-IEK3-VSA/tsam).


## Key contents

1. `aggregation-testing.ipynb` tests TSAM capabilities in preparation for eventually generating representatives.
2. `multihyper.py` contains parallelized functions for speeding up some calculations.
3. `ne-model-hypertuning.ipynb` tests hypertuning of NE-model representaive period selection.
4. `representative-period-processing.ipynb` creates representative periods for the NE-model.


## Setup

The included scripts require three major components:
1. [TSAM](https://github.com/FZJ-IEK3-VSA/tsam) for the time series aggregation.
2. [North European Backbone Model](https://github.com/vttresearch/north_european_model) for the data to be clustered.
3. [GAMS transfer](https://www.gams.com/latest/docs/API_PY_GETTING_STARTED.html) python API.

Please refer to their respective installation instructions for how to set each component up.
Note that the NE-model runs in its own python environment, which we don't need.
For the included scripts, I recommend using the `tsam_env` from the [TSAM](https://github.com/FZJ-IEK3-VSA/tsam) installation instructions as a basis,
and adding `GAMS transfer` into that environment.
The [`ipykernel` package](https://pypi.org/project/ipykernel/) also needs to be installed in that enviroment to run the included Jupyter notebooks.


## Use

The scripts for processing the representative periods are written as Jupyter notebooks.
For the representative period aggregation proper, refer to the `representative-period-processing.ipynb`.
`aggregation-testing.ipynb` is a simpler example I used when initially testing TSAM and its suitability for this purpose.
Meanwhile, `ne-model-hypertuning.ipynb` is a script I wrote for examining the representative period selection hypertuning to see what kind of solutions TSAM recommends should be used as the periods.


## Licence

Copyright (c) 2025 Topi Rasku and VTT Technical Research Centre of Finland Ltd.

All rights reserved (for now).


## Acknowledgements

As per the citation request in the [TSAM](https://github.com/FZJ-IEK3-VSA/tsam) repository:

>Maximilian Hoffmann, Leander Kotzur, Detlef Stolten, "The Pareto-optimal temporal aggregation of energy system models", Applied Energy, Volume 315, 2022, 119029, ISSN 306-2619, https://doi.org/10.1016/j.apenergy.2022.119029.

They also have other papers around the same topic, which you might find of interest.