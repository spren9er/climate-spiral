# Global Climate Spiral

## Introduction

The _Climate Spiral_ is a data visualization originally designed
by climate scientist [Ed Hawkins](https://twitter.com/ed_hawkins)
from the National Centre for Atmospheric Science, University of Reading in 2016.

This visualization is an interactive version of a climate spiral available at [https://svs.gsfc.nasa.gov/4975](https://svs.gsfc.nasa.gov/4975) and which was created by [Mark SubbaRao](https://twitter.com/marksubbarao) and NASA SVS in March 2022. Description from original website:

_The visualization presents monthly global temperature anomalies
between the years 1880-2021. These temperatures are based on the GISS
Surface Temperature Analysis (GISTEMP v4), an estimate of global
surface temperature change. Anomalies are defined relative to a base
period of 1951-1980. The data file used to create this visualization
can be accessed [here](https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv)._

The climate spiral has been modified in several ways in comparison to the orginal:

#### Radial Chart

- Starting from year 2000 animation slows down a little bit
- A diverging color scale with two linear gradients (blue to white, white to red) is used
- Average temperature difference per year is added and shown in the center of the chart
- Only last ten years are taken into account when displaying lines (older ones are faded out)

#### Time Series

- Animation doesn't stop and spiral keeps on rotating
- Chart has been rotated by 90 degrees (showing years on x-axis and temperature differences on y-axis)

One can control the animation by standard media controls. It is possible to change the speed factor (ranging from ¼x to 4x) to slow down or accelerate the animation. Additionally, one can go through the animation stepwise by clicking on left and right arrow buttons.

Also, for both charts there is a threshold parameter available on the left hand side to exclude some lines which are close to the baseline in order to focus on extreme values (not available on mobile phones).

Finally, one can switch between dark and light mode on the top right corner.

## #30DayChartChallenge 2022

This project was done as part of _#30DayChartChallenge 2022_ covering

- Day 19 (Time Series - Global Change)
- Day 22 (Time Series - Animation)

It is available at [https://climate-spiral.spren9er.de](https://climate-spiral.spren9er.de).

### Tweet

#### 1 (Introduction)

```
Global Climate Spiral

#30DayChartChallenge
#Day19 Time Series - Global Change
#Day22 Time Series - Animation

Full interactive visualization available at

https://climate-spiral.spren9er.de

[1/n]
```

1x animated gif showing whole animation from start to end (fast)

#### 2 (Credit)

```
The climate spiral is a data visualization originally designed by @ed_hawkins in 2016.
This present visualization is an interactive version of a climate spiral created by @marksubbarao and NASA SVS in March 2022

https://svs.gsfc.nasa.gov/4975

[2/n]
```

#### 3 (Feature 1: Focus on Extreme Values)

```
There are some additional features available compared to the original version.
It is possible to hide lines which are close to the baseline in order to put more emphasis on extreme values (not available on mobile phones).

[3/n]
```

1x animated gif showing application of threshold parameter

#### 4 (Feature 2: Dark & Light Mode)

```
Additionally, there is also a light mode available

[4/n]
```

2x light mode image (radial chart and time series)

#### 5 (Tech Stack)

```
Created with @sveltejs, #sveltekit, #d3, #layercake, #regl & #webgl
@MadeWithSvelte @d3js_org

[5/n]
```