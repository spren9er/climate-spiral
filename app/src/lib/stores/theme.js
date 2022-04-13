import { readable, writable } from 'svelte/store';

const _themes = {
	light: {
		name: 'light',
		backgroundColor: '#fafafa',
		color: '#777777',
		legendColor: '#cccccc'
	},
	dark: {
		name: 'dark',
		backgroundColor: '#333333',
		color: '#efefef',
		legendColor: '#cccccc'
	}
};

export const themes = readable(_themes);
export const theme = writable(_themes.dark);
