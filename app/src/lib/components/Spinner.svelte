<svg class="spinner" viewBox="0 0 40 40">
	<circle class="path" cx="20" cy="20" r="16" fill="none" stroke-width="3" />
</svg>

<style>
	.spinner {
		animation: rotate 2s linear infinite;
		z-index: 2;
		position: absolute;
		top: 50%;
		left: 50%;
		margin: -20px 0 0 -20px;
		width: 40px;
		height: 40px;
	}
	.spinner .path {
		stroke: #ffffff;
		opacity: 0.6;
		stroke-linecap: round;
		animation: dash 1.5s ease-in-out infinite;
	}
	@keyframes rotate {
		100% {
			transform: rotate(360deg);
		}
	}
	@keyframes dash {
		0% {
			stroke-dasharray: 1, 150;
			stroke-dashoffset: 0;
		}
		50% {
			stroke-dasharray: 90, 150;
			stroke-dashoffset: -35;
		}
		100% {
			stroke-dasharray: 90, 150;
			stroke-dashoffset: -124;
		}
	}
</style>
