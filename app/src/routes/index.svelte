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
	import RadialChart from '$lib/components/RadialChart/RadialChart.svelte';
	import Spinner from '$lib/components/Spinner.svelte';

	async function load() {
		async function csv(url, stepSize) {
			const response = await fetch(url, {
				method: 'get',
				headers: { 'content-type': 'text/csv;charset=UTF-8' }
			});

			const csvData = await response.text();
			const data = csvParse(csvData).map((row) => {
				return {
					year: +row.year,
					month: +row.month,
					diffTemp: +row.diff_temp
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
						diffTemp: diffTempScale(monthStep)
					};
				});
			});
		}

		return await csv(`${assets}/data/nasa.csv`, 10);
	}

	const initialContext = {
		speedFactor: writable(1),
		speedIcon: writable('4'),
		play: writable(false),
		next: writable(false),
		prev: writable(false),
		rewind: writable(false)
	};

	setContext('MediaControls', initialContext);

	$theme = $themes.dark;
</script>

<svelte:head>
	{#if $theme.name === 'light'}
		<link rel="stylesheet" href="stylesheets/light-theme.css" />
	{/if}
</svelte:head>

{#await load()}
	<Spinner />
{:then data}
	<div
		id="wrapper"
		style="--color: {$theme.color}; --background-color: {$theme.backgroundColor}"
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
					</Svg>

					<WebGL>
						<ClimateSpiral />
					</WebGL>

					<Svg>
						<BarChart />
					</Svg>
				</LayerCake>
			</div>

			<div id="media-controls">
				<MediaControls />
			</div>

			<div id="text">
				<p>
					The <i>Climate Spiral</i> is a data visualization originally designed
					by climate scientist
					<a href="https://twitter.com/ed_hawkins">Ed Hawkins</a>
					from the National Centre for Atmospheric Science, University of Reading.
				</p>

				<p>
					Above visualization is a remake of a spiral available at
					<a href="https://svs.gsfc.nasa.gov/4975"
						>https://svs.gsfc.nasa.gov/4975</a
					>
					and which was created by
					<a href="https://twitter.com/marksubbarao">Mark SubbaRao</a> and NASA SVS
					in 2022. Description from original website:
				</p>

				<p>
					The visualization presents monthly global temperature anomalies
					between the years 1880-2021. These temperatures are based on the GISS
					Surface Temperature Analysis (GISTEMP v4), an estimate of global
					surface temperature change. Anomalies are defined relative to a base
					period of 1951-1980. The data file used to create this visualization
					can be accessed <a
						href="https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
						>here</a
					>.
				</p>
			</div>

			<div id="twitter-handle">
				<a href="https://twitter.com/spren9er">@spren9er</a>
			</div>
		</div>
	</div>
{/await}

<style>
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
		padding-top: 50px;
		font-size: 44px;
		font-weight: normal;
	}

	#text {
		margin: 20px 0;
	}

	p {
		width: 500px;
		margin: 5px 0;
		font-size: 13px;
		color: var(--color);
		margin-left: -250px;
		left: 50%;
		position: relative;
		-webkit-text-size-adjust: none;
	}

	p a,
	p a:visited {
		color: var(--color);
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

	#twitter-handle {
		text-align: center;
		padding: 10px 0 20px 0;
	}

	#twitter-handle a,
	#twitter-handle a:visited {
		font-size: 10px;
		font-weight: bold;
		text-decoration: none;
		color: var(--color);
	}
</style>
