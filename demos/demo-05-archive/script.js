document.addEventListener("DOMContentLoaded", event => {
	axios.get('data.csv').then(response => {
		return new Promise((resolve, reject) => {
			Papa.parse(response.data, {
				header: true,
				dynamicTyping: true,
				complete: results => {
					plotAnnotations(results.data)
				},
				error: error => {
					reject(error)
				}
			})
		})
	}).catch(error => {
		console.error('Error fetching or parsing the CSV:', error)
		throw error
	})
})

function plotAnnotations(data) {
	
	const container = document.querySelector('.entries')
	
	data.forEach(entry => {
		console.log(entry)
		const div = document.createElement('div')
		
		div.classList.add('entry')
		

		const passFilename = '';

		div.innerHTML = `
			<div>${entry['Describe your location']}</div>
			<div class="entry__image">
				<img src="${passFilename}">
			</div>
		`

		container.appendChild(div)
	})
}
