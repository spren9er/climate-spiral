<script>
	import { getContext } from 'svelte';
	import { theme } from '$lib/stores/theme';

	import { isMobileDevice } from '$lib/utils/mobile';

	const { width, height, xScale } = getContext('LayerCake');

	export let r;

	const monthNames = [
		'Jan',
		'Feb',
		'Mar',
		'Apr',
		'May',
		'Jun',
		'Jul',
		'Aug',
		'Sep',
		'Oct',
		'Nov',
		'Dec'
	];

	$: cx = $width / 2;
	$: cy = $height / 2;
	$: radius = (1.05 * ($xScale(r) * $width)) / 2;
	$: monthLabels = monthNames.map((month, idx) => {
		const phi = (idx * 2 * Math.PI) / 12;
		const offset = -Math.PI / 2;

		return {
			x: radius * Math.cos(phi + offset),
			y: radius * Math.sin(phi + offset),
			label: month
		};
	});
</script>

{#each monthLabels as { x, y, label }}
	{#if isMobileDevice() || label !== 'Oct'}
		<g style="--legend-color: {$theme.legendColor}">
			<text x={cx + x} y={cy + y}>{label}</text>
			<line
				x1={cx + 0.92 * x}
				y1={cy + 0.92 * y}
				x2={cx + 0.95 * x}
				y2={cy + 0.95 * y}
			/>
		</g>
	{/if}
{/each}

<style>
	line {
		stroke: var(--legend-color);
		stroke-width: 1;
	}

	text {
		font-size: 14px;
		font-family: 'Lato', sans-serif;
		fill: var(--legend-color);
		text-anchor: middle;
		dominant-baseline: central;
		pointer-events: none;
		user-select: none;
	}
</style>
