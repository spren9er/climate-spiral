<script>
	import { getContext } from 'svelte';
	import { fade } from 'svelte/transition';

	import DiffTempAxis from './DiffTempAxis.svelte';
	import Grid from './Grid.svelte';
	import YearAxis from './YearAxis.svelte';

	const { data, custom } = getContext('LayerCake');

	const trailLength = $data.findIndex((d) => d.fullYear == 1890); // ten years trail
	const pause = 0.5 * trailLength;
</script>

{#if $custom.currentIndex >= $data.length + 5 * pause}
	<g transition:fade={{ duration: 400 }}>
		<Grid />
		<YearAxis />
		<DiffTempAxis />
	</g>
{/if}
