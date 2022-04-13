<script>
	import { theme } from '$lib/stores/theme';

	import { getContext } from 'svelte';

	const { data, custom, width, height } = getContext('LayerCake');

	$: currentIndex = Math.floor($custom.currentIndex);
	$: year =
		currentIndex < $data.length
			? $data[currentIndex].fullYear
			: $data[$data.length - 1].fullYear;
</script>

<text style="--color: {$theme.color}" x={$width / 2} y={$height / 2}
	>{year}</text
>

<style>
	text {
		font-family: 'Lato', sans-serif;
		font-size: 34px;
		fill: var(--color);
		text-anchor: middle;
		alignment-baseline: middle;
		pointer-events: none;
		user-select: none;
	}
</style>
