function fetchAndParseCSV(url) {
	return axios.get(url).then(response => {
		return new Promise((resolve, reject) => {
			Papa.parse(response.data, {
				header: true,
				complete: results => {
					resolve(results.data);
				},
				error: error => {
					reject(error);
				}
			});
		});
	}).catch(error => {
		console.error('Error fetching or parsing the CSV:', error);
		throw error;
	});
}

fetchAndParseCSV('data.csv').then(jsonData => {
	console.log(jsonData); 
}).catch(error => {
	console.error('Error processing the CSV:', error);
});
