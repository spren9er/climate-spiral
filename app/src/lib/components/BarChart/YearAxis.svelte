<script>
	import { getContext } from 'svelte';
	import { theme } from '$lib/stores/theme';

	import { extent } from 'd3-array';
	import { scaleLinear } from 'd3-scale';

	const { data, width, height } = getContext('LayerCake');

	const tickSize = 10;
	const yOffset = -14;
	const y = 0.93 * $height;
	const xScale = scaleLinear()
		.domain(extent($data, (d) => d.fullYear))
		.range([(1 / 8) * $width, (7 / 8) * $width]);
</script>

{#each new Array(8).fill(0).map((_, idx) => 1880 + 20 * idx) as year}
	<g style="--legend-color: {$theme.legendColor}">
		<text x={xScale(year)} {y}>{year}</text>

		<line
			x1={xScale(year)}
			x2={xScale(year)}
			y1={y + tickSize / 2 + yOffset}
			y2={y - tickSize / 2 + yOffset}
		/>
	</g>
{/each}

<style>
	line {
		stroke: var(--legend-color);
	}

	text {
		font-size: 12px;
		font-family: 'Lato', sans-serif;
		fill: var(--legend-color);
		background-color: black;
		text-anchor: middle;
		alignment-baseline: central;
		pointer-events: none;
		user-select: none;
	}
</style>
