<script>
	import { getContext } from 'svelte';
	import { fade } from 'svelte/transition';

	import MonthLabels from './MonthLabels.svelte';
	import RadialAxis from './RadialAxis.svelte';
	import RadialGrid from './RadialGrid.svelte';
	import YearLabel from './YearLabel.svelte';
	import YearIndicator from './YearIndicator.svelte';

	export const { data, custom } = getContext('LayerCake');

	const trailLength = $data.findIndex((d) => d.fullYear == 1890); // ten years trail
	const pause = 0.5 * trailLength;
</script>

{#if $custom.currentIndex < $data.length + pause}
	<g transition:fade={{ duration: 400 }}>
		<RadialGrid />

		<MonthLabels r={1.4} />

		<RadialAxis r={-1} label={'-1°'} />
		<RadialAxis r={0} label={'0°'} />
		<RadialAxis r={1} label={'+1°'} />

		{#if $custom.currentIndex > 0}
			<YearLabel />
			<YearIndicator />
		{/if}
	</g>
{/if}
