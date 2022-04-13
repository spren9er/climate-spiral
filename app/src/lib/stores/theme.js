import { readable, writable } from 'svelte/store';

const _themes = {
	light: {
		name: 'light',
		backgroundColor: '#dfdfd3',
		color: '#777777',
		legendColor: '#999999',
		buttonColor: '#999999'
	},
	dark: {
		name: 'dark',
		backgroundColor: '#333333',
		color: '#efefef',
		legendColor: '#cccccc',
		buttonColor: '#cccccc'
	}
};

export const themes = readable(_themes);
export const theme = writable(_themes.dark);
