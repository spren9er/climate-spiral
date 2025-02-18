# Global Climate Spiral

## Introduction

The _Climate Spiral_ is a data visualization originally designed
by climate scientist [Ed Hawkins](https://x.com/ed_hawkins)
from the National Centre for Atmospheric Science, University of Reading in 2016.

This visualization is an interactive version of a climate spiral available at [https://svs.gsfc.nasa.gov/4975](https://svs.gsfc.nasa.gov/4975) and which was created by [Mark SubbaRao](https://bsky.app/profile/marksubbarao.bsky.social) and NASA SVS in March 2022. Description from original website:

_The visualization presents monthly global temperature anomalies
between the years 1880-2021. These temperatures are based on the GISS
Surface Temperature Analysis (GISTEMP v4), an estimate of global
surface temperature change. Anomalies are defined relative to a base
period of 1951-1980. The data file used to create this visualization
can be accessed [here](https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv)._

The climate spiral has been modified in several ways in comparison to the original:

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

It is available at [https://climate-spiral.spren9er.de](https://climate-spiral.spren9er.de). See also corresponding posts on [X](https://x.com/spren9er/status/1516291303931322369) or [Bluesky](https://bsky.app/profile/spren9er.bsky.social/post/3lb2jegfchh2c).