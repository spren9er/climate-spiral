<script>
	import { assets } from '$app/paths';

	import { setContext } from 'svelte';
	import { writable } from 'svelte/store';
	import { themes, theme } from '$lib/stores/theme';

	import { LayerCake, Svg, WebGL } from 'layercake';
	import { csvParse } from 'd3-dsv';
	import { scaleLinear } from 'd3-scale';

	import BarChart from '$lib/components/BarChart/BarChart.svelte';
	import ClimateSpiral from '$lib/components/ClimateSpiral.svelte';
	import DarkMode from '$lib/components/DarkMode.svelte';
	import MediaControls from '$lib/components/MediaControls.svelte';
	import OpacityControl from '$lib/components/OpacityControl.svelte';
	import RadialChart from '$lib/components/RadialChart/RadialChart.svelte';

	async function load() {
		async function csv(url, stepSize) {
			const response = await fetch(url, {
				method: 'get',
				headers: { 'content-type': 'text/csv;charset=UTF-8' },
			});

			const csvData = await response.text();
			const data = csvParse(csvData).map((row) => {
				return {
					year: +row.year,
					month: +row.month,
					diffTemp: +row.diff_temp,
				};
			});

			return data.slice(0, -1).flatMap((d, i) => {
				const diffTemp = data[i + 1].diffTemp;
				const diffTempScale = scaleLinear().range([d.diffTemp, diffTemp]);

				const yearSteps = 12 * stepSize;
				return new Array(stepSize).fill(0).map((_, j) => {
					const monthStep = j / stepSize;
					const yearStep = (((i % 12) * stepSize + j) % yearSteps) / yearSteps;

					return {
						fullYear: d.year,
						fullMonth: d.month,
						year: d.year + yearStep,
						month: d.month + monthStep - 1,
						diffTemp: diffTempScale(monthStep),
					};
				});
			});
		}

		return await csv(`${assets}/data/data.csv`, 10);
	}

	const initialContext = {
		speedFactor: writable(1),
		speedIcon: writable('1'),
		play: writable(false),
		next: writable(false),
		prev: writable(false),
		rewind: writable(false),
	};

	setContext('MediaControls', initialContext);

	$theme = $themes.dark;
</script>

<svelte:head>
	{#if $theme.name === 'light'}
		<link rel="stylesheet" href="stylesheets/light-theme.css" />
	{/if}
</svelte:head>

{#await load() then data}
	<div
		id="wrapper"
		style="--color: {$theme.color}; --background-color: {$theme.backgroundColor}; --legend-color: {$theme.legendColor}"
	>
		<DarkMode />

		<div id="content">
			<h2>Global Climate Spiral</h2>

			<div id="chart-container">
				<LayerCake
					{data}
					x="diffTemp"
					y="month"
					z="year"
					xDomain={[-2, 2]}
					yDomain={[0, 12]}
					zDomain={[0, data.length - 1]}
					xRange={[0, 1]}
					yRange={[0, 2 * Math.PI]}
					zRange={[-0.75, 0.75]}
					custom={{ currentIndex: 0 }}
				>
					<Svg>
						<RadialChart />
						<BarChart />
					</Svg>

					<WebGL>
						<ClimateSpiral />
					</WebGL>

					<Svg>
						<OpacityControl />
					</Svg>
				</LayerCake>
			</div>

			<div id="media-controls">
				<MediaControls />
			</div>

			<div id="text">
				<p id="last-update">
					last updated on 2025/01/14 (data from 01/1880 to 12/2024)
				</p>

				<p>
					The <i>Climate Spiral</i> is a data visualization originally designed
					by climate scientist
					<a href="https://x.com/ed_hawkins">Ed Hawkins</a>
					from the National Centre for Atmospheric Science, University of Reading
					in 2016.
				</p>

				<p>
					Above visualization is an interactive version of a climate spiral
					created by
					<a href="https://bsky.app/profile/marksubbarao.bsky.social">
						Mark SubbaRao
					</a>
					and NASA SVS in March 2022. The original version is available at
					<a href="https://svs.gsfc.nasa.gov/4975">
						https://svs.gsfc.nasa.gov/4975
					</a>. Description from website:
				</p>

				<p>
					<i
						>The visualization presents monthly global temperature anomalies
						between the years 1880-2021. These temperatures are based on the
						GISS Surface Temperature Analysis (GISTEMP v4), an estimate of
						global surface temperature change. Anomalies are defined relative to
						a base period of 1951-1980. The data file used to create this
						visualization can be accessed <a
							href="https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
							>here</a
						>.
					</i>
				</p>

				<p>
					The present climate spiral has been modified in several ways in
					comparison to its original:
				</p>

				<h4>Radial Chart</h4>

				<ul>
					<li>
						A diverging color scale with two linear gradients (blue to white and
						white to red) is used
					</li>
					<li>
						Average temperature difference per year is shown in the center of
						the chart
					</li>
					<li>
						Only last ten years are taken into account when animating lines
						(older ones are faded out)
					</li>
					<li>
						Starting from year 2000, animation slows down slightly to emphasize
						the more recent development
					</li>
				</ul>

				<h4>Time Series</h4>

				<ul>
					<li>Animation does not stop and spiral keeps on rotating</li>
					<li>
						Chart has been rotated by 90 degrees (showing years on x-axis and
						temperature differences on y-axis)
					</li>
				</ul>

				<p>
					One can control the animation by standard media controls (play, pause,
					rewind). It is possible to change the speed factor (ranging from ¼x to
					4x) to slow down or accelerate the animation. Additionally, one can go
					through the animation stepwise by clicking on left and right arrow
					buttons.
				</p>

				<p>
					Also, for both projections there is a threshold parameter available on
					the left hand side to exclude lines which are close to the baseline
					(not available for mobile phones). It is helpful if one wants to put
					more focus on extreme values.
				</p>

				<p>
					Finally, one can switch between dark and light mode on the top right
					corner.
				</p>
			</div>

			<div id="website-link">
				<a href="https://spren9er.de">@spren9er</a>
			</div>
		</div>
	</div>
{/await}

<style>
	/* bebas-neue-regular - latin */
	@font-face {
		font-family: 'Bebas Neue';
		font-style: normal;
		font-weight: 400;
		src: url('/fonts/bebas-neue-v9-latin-regular.eot');
		src:
			local(''),
			url('/fonts/bebas-neue-v9-latin-regular.eot?#iefix')
				format('embedded-opentype'),
			url('/fonts/bebas-neue-v9-latin-regular.woff2') format('woff2'),
			url('/fonts/bebas-neue-v9-latin-regular.woff') format('woff'),
			url('/fonts/bebas-neue-v9-latin-regular.ttf') format('truetype'),
			url('/fonts/bebas-neue-v9-latin-regular.svg#BebasNeue') format('svg');
	}
	/* lato-regular - latin */
	@font-face {
		font-family: 'Lato';
		font-style: normal;
		font-weight: 400;
		src: url('/fonts/lato-v23-latin-regular.eot');
		src:
			local(''),
			url('/fonts/lato-v23-latin-regular.eot?#iefix')
				format('embedded-opentype'),
			url('/fonts/lato-v23-latin-regular.woff2') format('woff2'),
			url('/fonts/lato-v23-latin-regular.woff') format('woff'),
			url('/fonts/lato-v23-latin-regular.ttf') format('truetype'),
			url('/fonts/lato-v23-latin-regular.svg#Lato') format('svg');
	}
	/* lato-italic - latin */
	@font-face {
		font-family: 'Lato';
		font-style: italic;
		font-weight: 400;
		src: url('/fonts/lato-v23-latin-italic.eot');
		src:
			local(''),
			url('/fonts/lato-v23-latin-italic.eot?#iefix') format('embedded-opentype'),
			url('/fonts/lato-v23-latin-italic.woff2') format('woff2'),
			url('/fonts/lato-v23-latin-italic.woff') format('woff'),
			url('/fonts/lato-v23-latin-italic.ttf') format('truetype'),
			url('/fonts/lato-v23-latin-italic.svg#Lato') format('svg');
	}
	/* lato-700 - latin */
	@font-face {
		font-family: 'Lato';
		font-style: normal;
		font-weight: 700;
		src: url('/fonts/lato-v23-latin-700.eot');
		src:
			local(''),
			url('/fonts/lato-v23-latin-700.eot?#iefix') format('embedded-opentype'),
			url('/fonts/lato-v23-latin-700.woff2') format('woff2'),
			url('/fonts/lato-v23-latin-700.woff') format('woff'),
			url('/fonts/lato-v23-latin-700.ttf') format('truetype'),
			url('/fonts/lato-v23-latin-700.svg#Lato') format('svg');
	}

	:global(html),
	:global(body) {
		font-family: 'Lato', sans-serif;
		margin: 0;
		padding: 0;
		width: 100%;
		height: 100%;
		background-color: #333333;
	}

	#wrapper {
		height: 100%;
		background-color: var(--background-color);
	}

	#content {
		width: 700px;
		margin-left: -350px;
		left: 50%;
		height: 100%;
		position: relative;
	}

	h2 {
		font-family: 'Bebas Neue', cursive;
		margin: 0;
		padding: 0;
		color: var(--color);
		text-align: center;
		padding-top: 70px;
		font-size: 44px;
		font-weight: normal;
	}

	#text {
		margin: 20px 0;
	}

	p,
	h4,
	ul {
		width: 570px;
		margin: 10px 0;
		font-size: 13px;
		line-height: 18px;
		color: var(--color);
		margin-left: -285px;
		left: 50%;
		position: relative;
		text-align: left;
		-webkit-text-size-adjust: none;
	}

	ul {
		padding-left: 20px;
	}

	ul li {
		width: 540px;
	}

	p a,
	p a:visited {
		color: var(--color);
		font-weight: bold;
	}

	p#last-update {
		font-size: 10px;
		color: var(--legend-color);
		opacity: 0.5;
		text-align: right;
		border-top: 1px solid var(--legend-color);
		font-style: italic;
	}

	h4 {
		font-weight: bold;
	}

	#chart-container {
		padding: 0;
		width: 700px;
		height: 700px;
	}

	#media-controls {
		display: flex;
		justify-content: center;
		align-items: center;
		justify-items: center;
		width: 700px;
	}

	#website-link {
		text-align: center;
		padding: 10px 0 25px 0;
	}

	#website-link a,
	#website-link a:visited {
		font-size: 11px;
		font-weight: bold;
		text-decoration: none;
		color: var(--color);
	}
</style>
