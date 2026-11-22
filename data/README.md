# Data provenance and acquisition

The five simulated extracellular recording files `simulation_1.mat`–`simulation_5.mat` were supplied through the Neural Engineering Laboratory, Iran University of Science and Technology (IUST), for the original 2019 academic project. The project author has confirmed permission to publish the materials. The upstream simulator, licensing terms for third-party reuse, and the biological interpretation of reference annotation code `0` are not established by the MAT files alone.

The raw MAT files are **not committed to the repository**. They may be supplied as a separate Release asset. Extract `simulation_1.mat` to `simulation_5.mat` into `MyDrive/Computational Neuroscience/` before running the notebook on Colab, or modify `DATA_DIR_OVERRIDE` to point to their containing directory. Compare each file with `SHA256SUMS.txt` before analysis.

A working interpretation of `samplingInterval=0.0416666667` is milliseconds, corresponding to ~24 kHz for 2,880,000 samples per recording (120 s). This physical-unit interpretation remains dependent on the original simulation documentation.
