<script>
	import { getContext } from 'svelte';
	import { fade } from 'svelte/transition';

	import { max } from 'd3-array';

	import { theme } from '$lib/stores/theme';
	import { diffThreshold } from '$lib/stores/diffThreshold';

	let hidden = true;
	let strength = 1;
	let direction = 1;
	let clicked = false;

	const { data, custom, height } = getContext('LayerCake');

	const trailLength = $data.findIndex((d) => d.fullYear == 1890); // ten years trail
	const pause = 0.5 * trailLength;
	const maxAbsDiff = max($data, (d) => Math.abs(d.diffTemp));

	const isTouchDevice = () => {
		return (
			'ontouchstart' in window ||
			navigator.maxTouchPoints > 0 ||
			navigator.msMaxTouchPoints > 0
		);
	};

	const handleClick = (event) => {
		direction = event.target.id === 'opacity-up' ? 1 : -1;
		$diffThreshold = Math.min(
			Math.max($diffThreshold + direction * strength, 0),
			Math.ceil(maxAbsDiff * 10)
		);
	};

	const show = () => (hidden = false);
	const hide = () => (hidden = true);
</script>

{#if !isTouchDevice() && $custom.currentIndex >= $data.length + 5 * pause}
	<g
		style="--legend-color: {$theme.legendColor}"
		transform="translate(30, {$height / 2}) scale(0.8)"
	>
		<rect
			x="-13"
			y="-90"
			width="50"
			height="180"
			fill="transparent"
			stroke="none"
			on:mouseover={show}
			on:mouseout={hide}
		/>

		{#if !hidden}
			<g transition:fade={{ duration: 150 }}>
				<g transform="translate(0, -52)">
					<circle cx="12" cy="12" r="10" />
					<polyline points="16 12 12 8 8 12" />
					<line x1="12" y1="16" x2="12" y2="8" />
					<rect
						id="opacity-up"
						x="0"
						y="0"
						width="24"
						height="24"
						fill="transparent"
						stroke="none"
						on:mousedown={handleClick}
						on:mouseover={show}
					/>
				</g>

				<text x="36" y="2" on:mouseover={show} fill-opacity={clicked ? 0.5 : 1}>
					± {($diffThreshold / 10).toFixed(2)}°
				</text>

				<g transform="translate(0, 28)">
					<circle cx="12" cy="12" r="10" />
					<polyline points="8 12 12 16 16 12" />
					<line x1="12" y1="8" x2="12" y2="16" />
					<rect
						id="opacity-down"
						x="0"
						y="0"
						width="24"
						height="24"
						fill="transparent"
						stroke="none"
						on:mousedown={handleClick}
						on:mouseover={show}
					/>
				</g>
			</g>
		{/if}
	</g>
{/if}

<style>
	circle,
	line,
	polyline {
		fill: none;
		stroke: var(--legend-color);
		stroke-width: 2;
	}

	line,
	polyline {
		stroke-linecap: round;
		stroke-linejoin: round;
	}

	text {
		font-size: 15px;
		fill: var(--legend-color);
		text-anchor: end;
		alignment-baseline: middle;
		cursor: default;
		user-select: none;
		pointer-events: none;
	}

	#opacity-up,
	#opacity-down {
		cursor: pointer;
	}
</style>
