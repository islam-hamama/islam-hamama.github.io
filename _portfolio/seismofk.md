---
title: "SeismoFK — Open-source Infrasound Array Analysis"
excerpt: "Desktop application and batch processor for FK, Capon/MUSIC and PMCC array analysis of infrasound data, with detection uncertainty and station noise levels."
collection: portfolio
permalink: /portfolio/seismofk/
header:
  teaser: cards/seismofk.webp
  og_image: "/images/seismofk-v121-pmcc-families.png"
---

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20301795.svg)](https://doi.org/10.5281/zenodo.20301795)

**SeismoFK** is an open-source (MIT) application for infrasound and seismic **array analysis**. It measures the time delays of a signal across the sensors of an array to find where it comes from (**back-azimuth**) and how fast it crosses the array (**trace velocity**), then archives, plots and quantifies the result. It powers the analyses in several of my [blog posts](/year-archive/), including the [Artemis II Orion re-entry detection](/posts/2026/04/orion-reentry-infrasound/).

- **Source code:** [github.com/islam-hamama/SeismoFK](https://github.com/islam-hamama/SeismoFK)
- **Latest release:** [v1.2.1](https://github.com/islam-hamama/SeismoFK/releases/latest) — see the [release announcement](/posts/2026/09/seismofk-v1-2-1/)
- **Documentation:** [README](https://github.com/islam-hamama/SeismoFK/blob/main/README.md) and step-by-step [USAGE](https://github.com/islam-hamama/SeismoFK/blob/main/USAGE.md)

## What it does

| Capability | What you get |
|---|---|
| **FK beamforming** | Conventional FK with semblance, Fisher ratio and beam; **Capon (MVDR)** and **MUSIC** high-resolution slowness maps; theoretical array response |
| **PMCC detector** | Multi-band, triplet-consistency detection grouped into **families** (one per arrival), each with **95% confidence intervals** and a flag for merged sources |
| **Noise levels** | RMS level per sensor in **dB re 20 µPa**, L90 / L50 / L10 / Leq statistics, hour-of-day cycles and sensor-offset checks |
| **Long-term processing** | `seismofk-cli` runs any method over months or years of data with bounded memory, Parquet archives and figures |
| **Data safety** | Data-readiness checks, StationXML calibration-epoch resolution, unit tracking; IMS infrasound inventories included |
| **Desktop GUI** | Waveform explorer, spectrograms, StationXML editor and an event database |

## Screenshots

![SeismoFK main window](/images/seismofk-v121-main-window.png)
*Main window: data source and FK settings, the waveform explorer with the analysis window shaded, and the array methods.*

![PMCC detector with families](/images/seismofk-v121-pmcc-families.png)
*PMCC detector on a synthetic 120° / 340 m/s plane wave, with the detected family and its 95% interval.*

![Noise levels](/images/seismofk-v121-noise-levels.png)
*Noise levels in 1-minute windows with a simulated sensor gain error flagged.*

## Install

```bash
git clone https://github.com/islam-hamama/SeismoFK.git
cd SeismoFK
python -m venv .venv && source .venv/bin/activate
pip install -e ".[parquet]"
seismofk          # desktop application
seismofk-cli -h   # batch processing
```

## Citation

Please cite SeismoFK with this single reference, whatever version you use:

> Hamama, I. (2026). *SeismoFK* [Computer software]. Zenodo. [https://doi.org/10.5281/zenodo.20301795](https://doi.org/10.5281/zenodo.20301795)
