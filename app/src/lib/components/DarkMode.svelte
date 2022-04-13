<script>
	import { theme, themes } from '$lib/stores/theme';
</script>

<div id="dark-mode" style="--background-color: {$theme.color}">
	{#if $theme.name == 'dark'}
		<button on:click={() => ($theme = $themes.light)} title="Light Mode">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				width="14"
				height="14"
				viewBox="0 0 24 24"
				fill="none"
				stroke={$theme.backgroundColor}
				stroke-width="2"
				stroke-linecap="round"
				stroke-linejoin="round"
			>
				<circle cx="12" cy="12" r="5" />
				<line x1="12" y1="1" x2="12" y2="3" />
				<line x1="12" y1="21" x2="12" y2="23" />
				<line x1="4.22" y1="4.22" x2="5.64" y2="5.64" />
				<line x1="18.36" y1="18.36" x2="19.78" y2="19.78" />
				<line x1="1" y1="12" x2="3" y2="12" />
				<line x1="21" y1="12" x2="23" y2="12" />
				<line x1="4.22" y1="19.78" x2="5.64" y2="18.36" />
				<line x1="18.36" y1="5.64" x2="19.78" y2="4.22" />
			</svg>
		</button>
	{:else}
		<button on:click={() => ($theme = $themes.dark)} title="Dark Mode">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				width="14"
				height="14"
				viewBox="0 0 24 24"
				fill={$theme.backgroundColor}
				stroke={$theme.backgroundColor}
				stroke-width="2"
				stroke-linecap="round"
				stroke-linejoin="round"
				class="feather feather-moon"
				><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
			</svg>
		</button>
	{/if}
</div>

<style>
	button {
		position: absolute;
		width: 44px;
		height: 40px;
		z-index: 2;
		right: 0;
		padding-top: 3px;
		padding-left: 5px;
		top: 120px;
		border: none;
		border-radius: 10px 0 0 10px;
		border: 1px solid var(--background-color);
		background-color: var(--background-color);
		cursor: pointer;
	}
</style>
