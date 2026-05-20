---
title: "Announcing SeismoFK: Open-source FK Array Analysis for Infrasound and Seismic Data"
date: 2026-05-20
permalink: /posts/2026/05/seismofk-release/
image: /images/seismofk-spectrogram.jpg
header:
  og_image: "/images/seismofk-spectrogram.jpg"
tags:
  - SeismoFK
  - infrasound
  - array processing
  - FK analysis
  - open source
  - software
  - Python
  - PyQt5
  - IMS
  - CTBTO
---

Today I'm releasing **[SeismoFK](https://github.com/islam-hamama/SeismoFK)** — an open-source desktop application for **frequency–wavenumber (FK) array analysis** of infrasound and seismic array data.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20301796.svg)](https://doi.org/10.5281/zenodo.20301796)

If you read my [earlier post on the Artemis II Orion capsule re-entry detection](/posts/2026/04/orion-reentry-infrasound/), this is the tool that produced that analysis — beamforming, back-azimuth, slowness, and the multi-panel result figure all came out of SeismoFK.

## What SeismoFK does

SeismoFK is a PyQt5 desktop application that runs sliding-window FK array analysis on infrasound or seismic array data and reports, for each time window:

- **Semblance** (0–1 coherence measure)
- **Fisher ratio**
- **FK power**
- **Back-azimuth**
- **Apparent (trace) velocity / slowness**

It also forms a **delay-and-sum beam** steered to the dominant detected direction, compares the measured back-azimuth against an expected source direction, and archives classified events in a local SQLite database.

## Features

- Load **MiniSEED** waveforms from infrasound or seismic arrays
- Automatic station inventory loading from **FDSN StationXML**; auto-discovers all inventories in `XML/` or `XML_IM/`
- **XML Creator / Editor** to define custom array stations interactively
- `convert_ims.py` CLI to split a single CTBTO/IRIS `all_IMS_sts.xml` into per-station files
- Interactive **waveform viewer** with band-pass preview and time picking
- **Spectrogram window** for time–frequency inspection of every array element (new in this release)
- Sliding-window FK analysis with user-tunable bandpass, window length, overlap, and semblance threshold
- Local **event database** with classification, notes, filter, CSV export
- Auto-saved per-event result figure + CSV table

## Screenshots

![SeismoFK main analysis window](/images/seismofk-main-window.png)
*The main analysis window — inventory selection, FK parameters, waveform preview, and the bottom tools row.*

![SeismoFK spectrogram window](/images/seismofk-spectrogram.jpg)
*Spectrogram window — PSD for every channel of the array, with in-window controls to retune the bandpass and recompute on the fly.*

![FK analysis result for the Artemis II re-entry](/images/Output_Artemis-II-Reentry-Final.png)
*FK analysis result for the Artemis II Orion capsule re-entry detection — produced by SeismoFK from raw I57US waveforms.*

## Get it

- **Repository:** [github.com/islam-hamama/SeismoFK](https://github.com/islam-hamama/SeismoFK)
- **DOI:** [10.5281/zenodo.20301796](https://doi.org/10.5281/zenodo.20301796)
- **License:** MIT
- **Install:** `pip install -r requirements.txt` then `python Infra_Analysis.py`
- **Docs:** see the in-repo [README](https://github.com/islam-hamama/SeismoFK/blob/main/README.md) and the step-by-step [USAGE.md](https://github.com/islam-hamama/SeismoFK/blob/main/USAGE.md)

Station XML data is **not** bundled — IMS infrasound metadata is subject to CTBTO/IRIS distribution policies. The README documents how to supply your own (via `convert_ims.py` or the built-in XML Creator).

## Citation

If you use SeismoFK in your research, please cite it. GitHub auto-renders `CITATION.cff` as a *"Cite this repository"* button, or you can cite directly:

> Hamama, I. (2024–2025). *SeismoFK: Open-source FK array analysis for infrasound and seismic data.* Zenodo. [https://doi.org/10.5281/zenodo.20301796](https://doi.org/10.5281/zenodo.20301796)

## Acknowledgements

The array-processing methodology in SeismoFK is adapted in part from work by **Jelle Assink** (KNMI) — see the [ROSES 2021 array-processing material](https://github.com/roseseismo/roses2021/blob/main/unit08/array_processing.py).

---

*Feedback, bug reports, and feature requests are welcome — please open an issue on the [GitHub repo](https://github.com/islam-hamama/SeismoFK/issues) or reach out: [islam.hamama@nriag.sci.eg](mailto:islam.hamama@nriag.sci.eg).*
