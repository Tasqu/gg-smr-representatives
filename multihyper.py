## multihyper.py
# For whatever reason, multiprocessing doesn't seem to work in Jupyter notebooks.
# Thus, we have to implement these functions outside and impor them.

import tsam.hyperparametertuning as hype  # Optimize representatives.
import multiprocessing  # Parallelize hypertuning across years to save time?
from itertools import zip_longest  # Zip arguments for multiprocessing.


# Define function for multiprocessing handing the hypertuning.
def run_hypertune(year_agg_tuple, reduction_factor):
    hyper = hype.HyperTunedAggregations(year_agg_tuple[1])
    result = hyper.identifyOptimalSegmentPeriodCombination(reduction_factor)
    return (year_agg_tuple[0], result)


# Run hypertuning in parallel.
def parallel_hypertuning(tsam_dict, reduction_factor, num_workers):
    num_workers = multiprocessing.cpu_count() - 1  # Leave one processor free.
    with multiprocessing.Pool(num_workers) as pool:
        results = pool.starmap(
            run_hypertune,
            zip_longest(
                tsam_dict.items(), [reduction_factor], fillvalue=reduction_factor
            ),
        )
    return results
