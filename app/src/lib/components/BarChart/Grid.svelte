<script>
	import { getContext } from 'svelte';
	import { alpha } from '$lib/stores/alpha';
	import { theme } from '$lib/stores/theme';

	import { max } from 'd3-array';
	import { scaleLinear, scaleSqrt } from 'd3-scale';

	const { data, width, height } = getContext('LayerCake');

	const patternWidth = 4;
	const cy1 = (3 * $height) / 4;
	const cy2 = (1 * $height) / 4;
	const maxAbsDiff = max($data, (d) => Math.abs(d.diffTemp));
	const xScale = scaleLinear().range([(1 / 10) * $width, (9 / 10) * $width]);
	const yScale1 = scaleSqrt().domain([0, maxAbsDiff]).range([0, 1]);
	const yScale2 = scaleLinear()
		.domain([0, 4])
		.range([0, $height / 2]);

	$: yThreshold = yScale2(yScale1.invert($alpha / 100));
	$: rect1Y = [cy1 - yThreshold, cy1 + yThreshold];
	$: rect2Y = [cy2 - yThreshold, cy2 + yThreshold];
</script>

<g style="--legend-color: {$theme.legendColor}">
	<pattern
		id="diagonalLTR"
		width={patternWidth}
		height={patternWidth}
		patternTransform="rotate(45 0 0)"
		patternUnits="userSpaceOnUse"
	>
		<line
			x1="0"
			y1="0"
			x2="0"
			y2={patternWidth}
			style="stroke: var(--legend-color); stroke-width:1"
		/>
	</pattern>

	<pattern
		id="diagonalRTL"
		width={patternWidth}
		height={patternWidth}
		patternTransform="rotate(-45 0 0)"
		patternUnits="userSpaceOnUse"
	>
		<line
			x1="0"
			y1="0"
			x2="0"
			y2={patternWidth}
			style="stroke: var(--legend-color); stroke-width:1"
		/>
	</pattern>

	<rect
		x={xScale(0)}
		y={rect1Y[0]}
		width={xScale(1) - xScale(0)}
		height={rect1Y[1] - rect1Y[0]}
		fill="url(#diagonalLTR)"
	/>

	<rect
		x={xScale(0)}
		y={rect1Y[0]}
		width={xScale(1) - xScale(0)}
		height={rect1Y[1] - rect1Y[0]}
		fill="url(#diagonalRTL)"
	/>

	<rect
		x={xScale(0)}
		y={rect2Y[0]}
		width={xScale(1) - xScale(0)}
		height={rect2Y[1] - rect2Y[0]}
		fill="url(#diagonalLTR)"
	/>

	<rect
		x={xScale(0)}
		y={rect2Y[0]}
		width={xScale(1) - xScale(0)}
		height={rect2Y[1] - rect2Y[0]}
		fill="url(#diagonalRTL)"
	/>
</g>

<style>
	rect {
		fill-opacity: 0.25;
	}
</style>
