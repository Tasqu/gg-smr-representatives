# gg-smr-representatives

Representative period selection for the GG-SMR project.

Let's see if we can do some representative period selection for the
[North European Backbone Model](https://github.com/vttresearch/north_european_model)
using [TSAM](https://github.com/FZJ-IEK3-VSA/tsam).


## Key contents

1. `aggregation-testing.ipynb` tests TSAM capabilities in preparation for eventually generating representatives.


## Setup

The included scripts require three major components:
1. [TSAM](https://github.com/FZJ-IEK3-VSA/tsam) for the time series aggregation.
2. [North European Backbone Model](https://github.com/vttresearch/north_european_model) for the data to be clustered.
3. [GAMS transfer](https://www.gams.com/latest/docs/API_PY_GETTING_STARTED.html) python API.

Please refer to their respective installation instructions for how to set each component up.
Note that the NE-model runs in its own python environment, which we don't need.
For the included scripts, I recommend using the `tsam_env` as a basis,
while installing `GAMS transfer ` into that environment.


## Licence

All rights reserved (for now).


## Acknowledgements

As per the request in the [TSAM](https://github.com/FZJ-IEK3-VSA/tsam) repository:

>Maximilian Hoffmann, Leander Kotzur, Detlef Stolten, "The Pareto-optimal temporal aggregation of energy system models", Applied Energy, Volume 315, 2022, 119029, ISSN 306-2619, https://doi.org/10.1016/j.apenergy.2022.119029.

They also have other papers around the same topic, which you might find of interest.