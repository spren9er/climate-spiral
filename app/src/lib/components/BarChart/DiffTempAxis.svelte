<script>
	import { getContext } from 'svelte';
	import { theme } from '$lib/stores/theme';

	import { scaleLinear } from 'd3-scale';

	const { width, height } = getContext('LayerCake');

	const yScale = scaleLinear()
		.domain([-4, 4])
		.range([-$height / 2, $height / 2]);
</script>

<g style="--legend-color: {$theme.legendColor}">
	{#each [[-3, '+1'], [-2, '0'], [-1, '-1'], [1, '-1'], [2, '0'], [3, '+1']] as [y, label]}
		<line
			x1={(1 / 10) * $width}
			x2={(9 / 10) * $width}
			y1={$height / 2 + yScale(y)}
			y2={$height / 2 + yScale(y)}
		/>

		<text dx={21} dy={-1} x={(9 / 10) * $width} y={$height / 2 + yScale(y)}
			>{label}°</text
		>
	{/each}
</g>

<style>
	line {
		stroke: var(--legend-color);
	}

	text {
		font-size: 12px;
		font-family: 'Lato', sans-serif;
		fill: var(--legend-color);
		background-color: black;
		text-anchor: end;
		alignment-baseline: central;
		pointer-events: none;
		user-select: none;
	}
</style>
