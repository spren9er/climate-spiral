<script>
	import { getContext } from 'svelte';
	import { theme } from '$lib/stores/theme';
	import { diffThreshold } from '$lib/stores/diffThreshold';

	import { scaleLinear } from 'd3-scale';

	const { width, height } = getContext('LayerCake');

	const patternWidth = 4;
	const padding = 3;

	$: yScale = scaleLinear()
		.domain([0, 4])
		.range([0, $height / 2]);

	$: rScale = scaleLinear()
		.domain([-2, 2])
		.range([0, $height / 2]);

	$: yThreshold = yScale($diffThreshold / 10);
	$: cx = $width / 2;
	$: cy = $height / 2;
	$: innerRadius = rScale(0) - yThreshold + padding;
	$: outerRadius = rScale(0) + yThreshold - padding;
</script>

{#if $diffThreshold > 0}
	<g
		style="--legend-color: {$theme.legendColor}; --background-color: {$theme.backgroundColor}"
	>
		<pattern
			id="diagonalLTR"
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

		<pattern
			id="diagonalRTL"
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

		<circle
			{cx}
			{cy}
			r={outerRadius}
			fill="url(#diagonalLTR)"
			fill-opacity="0.25"
		/>

		<circle
			{cx}
			{cy}
			r={outerRadius}
			fill="url(#diagonalRTL)"
			fill-opacity="0.25"
			stroke={$theme.legendColor}
			stroke-opacity="0.1"
		/>

		<circle
			{cx}
			{cy}
			r={innerRadius}
			fill={$theme.backgroundColor}
			fill-opacity="1.0"
			stroke={$theme.legendColor}
			stroke-opacity="0.1"
		/>
	</g>
{/if}
