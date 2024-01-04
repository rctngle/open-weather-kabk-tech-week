function fetchCSV(url) {
	fetch(url)
	.then(response => response.text())
	.then(data => {
		const jsonData = csvToJSON(data)
		return jsonData
	})
	.catch(error => console.error('Error fetching the CSV:', error))
}

function csvToJSON(csv) {
	const lines = csv.split('\n')
	const headers = lines[0].split(',')

	return lines.slice(1).map(line => {
		const data = line.split(',')
		return headers.reduce((obj, nextKey, index) => {
			obj[nextKey] = data[index]
			return obj
		}, {})
	})
}

const csvUrl = 'path/to/your/csvfile.csv'
fetchCSV(csvUrl);
