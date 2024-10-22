<p align=center>
    <img src="img/Result.png">
</p>

<p align=center>
    <a target="_blank" href="https://travis-ci.com/chonyy/handoff-simulator" title="Build Status"><img src="https://travis-ci.com/chonyy/handoff-simulator.svg?branch=master"></a>
    <a target="_blank" href="#" title="language count"><img src="https://img.shields.io/github/languages/count/chonyy/handoff-simulator"></a>
    <a target="_blank" href="#" title="top language"><img src="https://img.shields.io/github/languages/top/chonyy/handoff-simulator?color=orange"></a>
    <a target="_blank" href="http://nodejs.org/download/" title="Node version"><img src="https://img.shields.io/badge/node.js-%3E=_6.0-green.svg"></a>
    <a target="_blank" href="https://opensource.org/licenses/MIT" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
    <a target="_blank" href="#" title="repo size"><img src="https://img.shields.io/github/repo-size/chonyy/handoff-simulator"></a>
    <a target="_blank" href="http://makeapullrequest.com" title="PRs Welcome"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
</p>

> 📶 Wiresless network handoff simulator built with python!

If you are not familiar with the process of handoff, strongly recommend checking out the [handoff-visualizer](https://github.com/chonyy/handoff-visualizer). The visualizer visualize a tuned versoin of this simulation, which makes the process and concept easy to understand. The visualizer is built to make the concept understandable. We **value the data in this simulation project**.

This project is a side project of [handoff-visualizer](https://github.com/chonyy/handoff-visualizer).

## Simulation Structure

<p align=center>
    <img src="img/simulation.PNG">
</p>

A block size is 120 \* 80 (m^2). Cars are assummed to be moving on an extremely thin line between blocks, the line doesn't take up any space. The velocity of the car is 10m/s. In our simultation, we iterate once in a second, the cars moves 10 meter, and all the data are calculated and updated on each iteration. We run for **86400 iterations** to simulate the handoffs in a day.

-   **Velocity** = 36km/hr = 10m/s
-   **Probability of cars entrance** follows [Poisson distribution](https://en.wikipedia.org/wiki/Poisson_distribution)
-   **⋋** = 2 cars/ min [ P(t) = ⋋"e" ^(−"⋋" ) (t is in sec) ]
-   **Probability of cars turning** based on predefined value listed below
-   **Received Power Calculation** explained below

### Car Entrance Distribution

The probability of the entrance follows [Poisson distribution](https://en.wikipedia.org/wiki/Poisson_distribution)<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c22cb4461e100a6db5f815de1f44b1747f160048"> and <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/2debd3f9adf97c8af4919aa69ed4a7121b47a737">

In our simultation

-   **⋋** = 0.0334 cars/ sec
-   **k** = 1

### Received Power

The received power is calculated by the formula below. Read [ScienceDirect](https://www.sciencedirect.com/topics/engineering/received-signal-power) to dig deeper.

-   Base station transmission Pt(mW) = -50 dBm
-   Base = 1mW
-   10log(Pt / Base) = dBm
-   First-meter path loss = 10 dBm
-   **P0 = -50 dBm**
-   **Pd = -50 - 10 - 20log(d(m) / 1m)**

## What is handoff?

<p align=center>
    <img src="img/handoff.PNG" width="636" height="391">
</p>

[Handoff](https://searchmobilecomputing.techtarget.com/definition/handoff) is the **transition** for any given user of signal transmission from one base station to a geographically adjacent base station as the user **moves around**.

Each time a mobile or portable cellular subscriber passes from one cellinto another, the network automatically switches coverage responsibility from one basestation to another. Each base-station transition, as well as the switching processor sequence itself, is called handoff.

## Usage

Idealy

```python
pipenv sync
pipenv run python src/handoff.py
```

Or if you already got the dependencies in the pipfile

```python
python src/handoff.py
```

## Policies parameter value

The different parameters for each policy are listed below.

| Parameters |  Value   |
| ---------- | :------: |
| Threshold  | -110 dBm |
| Entrophy   |  5 dBm   |
| Minimum    | -125 dBm |

## Posssibility of turning

The possibility of changing direction when encountering intersection is listed below.

### Intersection with four roads

| Direction   | Possibility |
| ----------- | :---------: |
| Go straight |     1/2     |
| Turn right  |     1/3     |
| Turn left   |     1/6     |
