<script>
	import { getContext } from 'svelte';
	import { diffThreshold } from '$lib/stores/diffThreshold';
	import { theme } from '$lib/stores/theme';

	import { scaleLinear } from 'd3-scale';

	const { width, height } = getContext('LayerCake');

	const patternWidth = 4;
	const padding = 2;
	const cy1 = (3 * $height) / 4;
	const cy2 = (1 * $height) / 4;
	const xScale = scaleLinear().range([(1 / 10) * $width, (9 / 10) * $width]);
	const yScale = scaleLinear()
		.domain([0, 4])
		.range([0, $height / 2]);

	$: yThreshold = yScale($diffThreshold / 10);
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
			style="stroke: var(--legend-color); stroke-width: 1"
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
			style="stroke: var(--legend-color); stroke-width: 1"
		/>
	</pattern>

	<rect
		x={xScale(0)}
		y={rect1Y[0] + padding}
		width={xScale(1) - xScale(0)}
		height={rect1Y[1] - rect1Y[0] - 2 * padding}
		fill="url(#diagonalLTR)"
	/>

	<rect
		x={xScale(0)}
		y={rect1Y[0] + padding}
		width={xScale(1) - xScale(0)}
		height={rect1Y[1] - rect1Y[0] - 2 * padding}
		fill="url(#diagonalRTL)"
	/>

	<rect
		x={xScale(0)}
		y={rect2Y[0] + padding}
		width={xScale(1) - xScale(0)}
		height={rect2Y[1] - rect2Y[0] - 2 * padding}
		fill="url(#diagonalLTR)"
	/>

	<rect
		x={xScale(0)}
		y={rect2Y[0] + padding}
		width={xScale(1) - xScale(0)}
		height={rect2Y[1] - rect2Y[0] - 2 * padding}
		fill="url(#diagonalRTL)"
	/>

	<line
		class="border"
		x1={xScale(0)}
		x2={xScale(1)}
		y1={rect1Y[0] + padding}
		y2={rect1Y[0] + padding}
	/>

	<line
		class="border"
		x1={xScale(0)}
		x2={xScale(1)}
		y1={rect1Y[1] - padding}
		y2={rect1Y[1] - padding}
	/>

	<line
		class="border"
		x1={xScale(0)}
		x2={xScale(1)}
		y1={rect2Y[0] + padding}
		y2={rect2Y[0] + padding}
	/>

	<line
		class="border"
		x1={xScale(0)}
		x2={xScale(1)}
		y1={rect2Y[1] - padding}
		y2={rect2Y[1] - padding}
	/>
</g>

<style>
	rect {
		fill-opacity: 0.25;
	}

	line.border {
		stroke-width: 1;
		stroke: var(--legend-color);
		stroke-opacity: 0.1;
	}
</style>
