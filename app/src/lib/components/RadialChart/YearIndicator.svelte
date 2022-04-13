<script>
	import { theme } from '$lib/stores/theme';

	import { max, mean } from 'd3-array';
	import { scaleDiverging, scaleLinear } from 'd3-scale';

	import { getContext } from 'svelte';

	const { data, custom, width, height } = getContext('LayerCake');

	const fullWidth = 80;
	const indicatorHeight = 5;
	const indicatorWidth = 20;

	$: maxAbsDiff = max($data, (d) => Math.abs(d.diffTemp));

	$: colorScale = scaleDiverging()
		.domain([-maxAbsDiff, 0, maxAbsDiff])
		.range(['#053061', '#ffffff', '#67001f']);

	$: posScale = scaleLinear()
		.domain([-maxAbsDiff, maxAbsDiff])
		.range([$width / 2 - fullWidth / 2, $width / 2 + fullWidth / 2]);

	$: currentIndex = Math.floor($custom.currentIndex);
	$: year =
		currentIndex < $data.length
			? $data[currentIndex].fullYear
			: $data[$data.length - 1].fullYear;
	$: avgDiffTempYear = mean(
		$data.filter((d) => d.fullYear == year).map((d) => d.diffTemp)
	);
	$: fill = colorScale(avgDiffTempYear);
</script>

<g transform="translate(0, 20)">
	<line
		x1={$width / 2 - fullWidth / 2}
		x2={$width / 2 + fullWidth / 2}
		y1={$height / 2 + indicatorHeight}
		y2={$height / 2 + indicatorHeight}
		stroke={$theme.legendColor}
		stroke-width={indicatorHeight}
		stroke-opacity={0.3}
	/>

	<rect
		x={posScale(avgDiffTempYear) - indicatorWidth / 2}
		y={$height / 2 + indicatorHeight / 2}
		width={indicatorWidth}
		height={indicatorHeight}
		{fill}
		fill-opacity={1}
	/>

	<line
		x1={$width / 2}
		x2={$width / 2}
		y1={$height / 2 + indicatorHeight / 2 - 1.5}
		y2={$height / 2 + (3 * indicatorHeight) / 2 + 1.5}
		stroke={$theme.color}
	/>
</g>
