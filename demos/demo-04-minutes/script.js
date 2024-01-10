window.addEventListener('DOMContentLoaded', e=>{
	mapboxgl.accessToken = 'pk.eyJ1IjoiYW5lY2RvdGUxMDEiLCJhIjoiY2oxMGhjbmpsMDAyZzJ3a2V0ZTBsNThoMiJ9.1Ce55CnAaojzkqgfX70fAw';
	const map = new mapboxgl.Map({
		style: 'mapbox://styles/anecdote101/clqz7jsyn018101qw4k0h5rlx?fresh=true',
		container: 'map',
		center: [-6, 58.87],
		zoom: 3
	});
})