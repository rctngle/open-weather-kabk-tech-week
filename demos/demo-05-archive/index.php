<?php

function getData($filepath) {
	$header = [];
	$csv = [];
	if (($handle = fopen($filepath, 'r')) !== FALSE) {
		while (($row = fgetcsv($handle, 0, ',')) !== FALSE) {
			if (count($header) == 0) {
				$header = $row;
			} else {
				$entry = [];
				for ($i =0; $i<count($row); $i++) {
					if (isset($header[$i]) && isset($row[$i])) {
						$entry[$header[$i]] = $row[$i];
					}
				}
				$csv[] = $entry;
			}
		}
		fclose($handle);
	}
	

	return $csv;
}

function getFilename($url) {
	$queryString = parse_url($url, PHP_URL_QUERY);
	if($queryString){
		parse_str($queryString, $queryParams);
		if ($queryParams['id']) {
			return $queryParams['id'] . '.jpg';
		}
	}
	return false;
}

$data = getData('data.csv');

// echo "<pre>";
// print_r($data);
// echo "</pre>";


?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>Archive</title>

	<link rel="stylesheet" href="style.css" />

	<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
	
	<script src="script.js"></script>
</head>

<body>

	<div class="entries">
		<?php foreach($data as $entry): ?>

			<?php

			$passFileName = getFilename($entry['Upload the raw image file (optional)']);
			
			$additionalFilenames = [];
			$additionalURLs = explode(',', $entry['Upload additional images. For example, photos of your ground station or you receiving the satellite transmission. (optional)']);
			foreach($additionalURLs as $additionalURLs) {
				$additionalFileName = getFilename(trim($additionalURLs));
				if ($additionalFileName) {
					$additionalFilenames[] = $additionalFileName;
				}
			}

			?>

			<div class="entry">
				<div><?php echo $entry['Describe your location']; ?></div>
				<div>
					<div class="entry__image">
						<?php if ($passFileName): ?>
							<img src="files/<?php echo $passFileName; ?>" />
						<?php endif; ?>
					</div>

					<div class="entry__additionalimages">
						<?php foreach($additionalFilenames as $additionalFilename): ?>
							<img src="files/<?php echo $additionalFilename; ?>" />
						<?php endforeach; ?>
					</div>
				</div>
			</div>

		<?php endforeach; ?>
	</div>
</body>
</html>