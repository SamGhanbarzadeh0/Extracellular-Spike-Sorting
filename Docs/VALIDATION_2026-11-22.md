# Full-validation artifact audit — 22 November 2026

## Evidence inspected

- User-supplied Jupyter notebook: `01- Spike Sorting 2019 v3 - Final Figures and Validation.ipynb` — 7,499,501 bytes; SHA-256 `b1410903317aea8af311cdc76468eb63ece143f9775ac1abe034a7b219a433bb`.
- Run-stamped reference archive: `SpikeSorting_2019_v3_20261122T060055_422939Z_Results.zip` — 48,319,586 bytes; SHA-256 `57166309bf7c8c3a16032361cebb4a3af0ba3d1ac98da98ba89c6e31edd6822a`.
- Original earlier archive: `SpikeSorting_2019_v3_Results.zip` — compared against the new primary 45-row table.
- Five source `simulation_i.mat` files from the same Drive folder — each binary SHA-256 matched `RUN_COMPLETENESS_MANIFEST.json`.

## Completed and checked

1. The new archive is a valid ZIP and its byte hash matches the notebook's printed final SHA-256.
2. `FULL_VALIDATION_STATUS.json` explicitly reports `COMPLETE`, five recordings, nine methods, and ten seeds per method.
3. Each `simulation_i/COMPLETE.json` checkpoint is present and says `COMPLETE`; all six per-dataset checkpoint table row counts match its declared stages.
4. Global files contain 45 seed-stability rows (each `n_seeds=10`), 270 threshold/PCA rows, 70 method-parameter rows, 15 onset-alignment rows, 15 polarity rows, and 10 permutation-control rows. The declared row counts were independently computed from the CSVs.
5. All 45 primary comparison rows agree with the earlier results archive **in every scientific column**. The only differing field is the recorded wall-clock runtime `fit_s` across those 45 rows.
6. Every row in `END_TO_END_HELDOUT_MICRO_SUMMARY.csv` satisfies F1 = 2TP/(2TP+FP+FN) to machine tolerance.
7. The full archive records 92 figure outputs. Eight chosen PNG figures are available directly in the repository-ready kit.
8. The public notebook copy preserves all 26 executable cell sources and preserved inline stream/text/PNG output contents. Transient Colab account metadata has been deleted; outdated markdown about an earlier partial run has been updated.

## Important qualification

The complete reference run was performed in the Colab environment associated with the user and its artifacts are present, consistent and auditable. We have independently **inspected and cross-checked these outputs and source file hashes**; we have **not independently recomputed every expensive stage** in this audit environment. The earlier local scikit-learn 1.8.0 audit's 43/45 exact ARI matches and two HDBSCAN deviations remain informative as a cross-version sensitivity check, not a defect in this 1.6.1 archive.

Notebook `execution_count` is empty for some cells even when their preserved display output exists. The more robust provenance is the run-stamped completed archive with all per-recording checkpoints, not notebook cell counters.

## Scientific limits remain

- The MAT reference annotation semantics, particularly code `0`, are not independently proven by the MAT files.
- Original simulation metadata is required to fully validate the time unit, event-index convention and source generator.
- Two-code F1 of 0.973822 and all-code F1 of 0.713059 have different denominators and cannot be substituted.
- ARI values are matched-event conditional, whereas event-level F1 incorporates missed events.
- The 2019 academic project and 2026 Python validation must be dated separately; the implementation years of every later method are not independently established.

## Release gate

**Technical artifact readiness: PASS.** Valid completed reference archive, identifiable recorded environment, validated source hashes, consistent primary scientific outputs, and sanitized notebook copy.

**Scientific reporting scope: QUALIFIED PASS.** Publish the exact performance definitions and provenance limitations; do not advertise real-neuron isolation or external/generalization accuracy.

**GitHub deployment: NOT YET COMPLETED.** Repository creation, file commits, and GitHub Releases attachment still require a GitHub repository and release publishing action.
