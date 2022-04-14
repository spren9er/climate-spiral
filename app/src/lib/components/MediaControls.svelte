<script>
	import { getContext } from 'svelte';
	import { theme } from '$lib/stores/theme';

	const { speedFactor, speedIcon, play, next, prev, rewind } =
		getContext('MediaControls');

	const switchSpeedFactor = () => {
		switch ($speedFactor) {
			case 0.25:
				$speedFactor = 0.5;
				$speedIcon = '½';
				break;
			case 0.5:
				$speedFactor = 1;
				$speedIcon = '1';
				break;
			case 1:
				$speedFactor = 2;
				$speedIcon = '2';
				break;
			case 2:
				$speedFactor = 4;
				$speedIcon = '4';
				break;
			case 4:
				$speedFactor = 0.25;
				$speedIcon = '¼';
				break;
		}
	};
</script>

<div
	style="--button-color: {$theme.buttonColor}; --background-color: {$theme.backgroundColor}"
>
	<div id="button-bar">
		<button
			class="btn-rewind"
			on:click={() => {
				$rewind = true;
				$play = true;
			}}
			title="Rewind"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				width="12"
				height="12"
				viewBox="0 0 24 24"
				fill="none"
				stroke={$theme.buttonColor}
				stroke-width="2"
				stroke-linecap="round"
				stroke-linejoin="round"
				class="feather feather-rewind"
			>
				<polygon points="11 19 2 12 11 5 11 19" />
				<polygon points="22 19 13 12 22 5 22 19" />
			</svg>
		</button>

		<button
			class="btn-prev"
			on:click={() => ($prev = true)}
			title="Previous Frame"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				width="12"
				height="12"
				viewBox="0 0 24 24"
				fill="none"
				stroke={$theme.buttonColor}
				stroke-width="2"
				stroke-linecap="round"
				stroke-linejoin="round"
				class="feather feather-skip-back"
				style="transform: translate(-2px, 0);"
			>
				<polygon points="19 20 9 12 19 4 19 20" />
			</svg>
		</button>

		<button
			class="btn-play"
			on:click={() => {
				if ($rewind) $rewind = false;
				$play = !$play;
			}}
			title="Play / Pause"
		>
			{#if $play}
				<svg
					xmlns="http://www.w3.org/2000/svg"
					width="12"
					height="12"
					viewBox="0 0 24 24"
					fill="none"
					stroke={$theme.buttonColor}
					stroke-width="2"
					stroke-linecap="round"
					stroke-linejoin="round"
					class="feather feather-pause"
				>
					<rect x="6" y="4" width="4" height="16" />
					<rect x="14" y="4" width="4" height="16" />
				</svg>
				<span class="text">PAUSE</span>
			{:else}
				<svg
					xmlns="http://www.w3.org/2000/svg"
					width="12"
					height="12"
					viewBox="0 0 24 24"
					fill="none"
					stroke={$theme.buttonColor}
					stroke-width="2"
					stroke-linecap="round"
					stroke-linejoin="round"
					class="feather feather-play"
				>
					<polygon points="5 3 19 12 5 21 5 3" />
				</svg>
				<span class="text">PLAY</span>
			{/if}
		</button>

		<button class="btn-next" on:click={() => ($next = true)} title="Next Frame">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				width="12"
				height="12"
				viewBox="0 0 24 24"
				fill="none"
				stroke={$theme.buttonColor}
				stroke-width="2"
				stroke-linecap="round"
				stroke-linejoin="round"
				class="feather feather-skip-forward"
			>
				<polygon points="5 4 15 12 5 20 5 4" />
			</svg>
		</button>

		<button
			class="btn-speed-factor"
			on:click={() => switchSpeedFactor()}
			title="Speed Factor"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				width="12"
				height="12"
				viewBox="0 0 24 24"
				><text
					x="12"
					y="12"
					fill={$theme.buttonColor}
					text-anchor="middle"
					dominant-baseline="central"
				>
					{`${$speedIcon}x`}
				</text>
			</svg>
		</button>
	</div>
</div>

<style>
	#button-bar {
		margin: -6px 0 6px 0;
	}

	button {
		width: 28px;
		height: 26px;
		margin: 2px;
		padding: 0;
		background: var(--background-color);
		border: 1px solid var(--button-color);
		border-radius: 3px;
		cursor: pointer;
		color: var(--button-color);
	}

	button svg {
		margin: 3px 0 0 4px;
		width: 12px;
		height: 12px;
		padding: 0;
	}

	button.btn-play {
		width: 76px;
	}

	button.btn-play .text {
		position: relative;
		top: -2px;
		font-size: 11px;
		line-height: 11px;
	}

	button.btn-play svg {
		margin-left: 0;
	}

	button.btn-rewind svg {
		padding-right: 4px;
	}

	button.btn-prev svg {
		padding-right: 3px;
	}

	button.btn-next svg {
		padding-right: 1px;
	}

	button.btn-speed-factor svg {
		padding-right: 4px;
	}

	button.btn-speed-factor text {
		font-size: 20px;
	}
</style>
