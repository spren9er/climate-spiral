<script>
	import { getContext } from 'svelte';
	import { theme } from '$lib/stores/theme';

	const { width, height, xScale } = getContext('LayerCake');

	export let r;
	export let label;

	$: cx = $width / 2;
	$: cy = $height / 2;
	$: radius = $xScale(r) * cx;
	$: angle = 90 - (Math.acos(16 / radius) * 180) / Math.PI;
</script>

{#if angle}
	<g style="--legend-color: {$theme.legendColor}">
		<g transform="rotate({angle}, {cx}, {cy})">
			<path d="M {cx} {cy - radius} a {radius} {radius} 0 0 1 0 {2 * radius}" />
		</g>
		<g transform="rotate({-angle}, {cx}, {cy})">
			<path
				d="M {cx} {cy + radius} a {radius} {radius} 0 0 1 0 {-2 * radius}"
			/>
		</g>
		<text x={cx} y={cy - radius}>{label}</text>
	</g>
{/if}

<style>
	path {
		fill: transparent;
		stroke: var(--legend-color);
		stroke-width: 1.25;
		stroke-dasharray: '75, 100';
	}

	text {
		font-size: 14px;
		font-family: 'Lato', sans-serif;
		fill: var(--legend-color);
		text-anchor: middle;
		alignment-baseline: central;
		pointer-events: none;
		user-select: none;
	}
</style>
