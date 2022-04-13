import { tweened } from 'svelte/motion';
import { cubicInOut } from 'svelte/easing';

export const alpha = tweened(0, {
	duration: 800,
	easing: cubicInOut
});
