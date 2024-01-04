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
	
	const container = document.getElementById('annotations')
	
	data.forEach(entry => {
		
		const div = document.createElement('div')
		div.classList.add('annotation')
		
		div.style.left = entry.x + 'px'
		div.style.top = entry.y + 'px'
		div.style.width = entry.width + 'px'
		div.style.height = entry.height + 'px'
		
		div.textContent = entry.annotation

		container.appendChild(div)
	})
}
