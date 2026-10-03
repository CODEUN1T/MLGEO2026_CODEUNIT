"""Smoke test: check that the course environment runs before doing real work."""
import platform

import numpy as np
import pandas as pd
import xarray as xr

# A calculation with a known answer: a line rising 2.5 mm/yr must give slope 2.5.
t = np.arange(0.0, 10.0, 0.1)
slope = np.polyfit(t, 2.5 * t + 1.0, 1)[0]
assert abs(slope - 2.5) < 1e-9, f"expected slope 2.5, got {slope}"

print(f"Python {platform.python_version()} on {platform.system()} {platform.machine()}")
print(f"numpy {np.__version__}, pandas {pd.__version__}, xarray {xr.__version__}")
print("smoke test passed")