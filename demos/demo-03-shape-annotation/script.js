document.addEventListener("DOMContentLoaded", () => {
	loadAndAppendSVG('annotations.svg', document.querySelector('.annotations__image'))
		.then(() => {
			addEventListenersToAnnotations()
			addEventListenersToSVGGroups()
		})
})

function loadAndAppendSVG(svgURL, targetElement) {
	return fetch(svgURL)
		.then(response => response.text())
		.then(svgText => {
			const parser = new DOMParser()
			const svgElement = parser.parseFromString(svgText, "image/svg+xml").documentElement
			targetElement.appendChild(svgElement)
		})
}

function addEventListenersToAnnotations() {
    document.querySelectorAll('.annotation').forEach(annotation => {
        annotation.addEventListener('mouseenter', () => toggleActiveClass(annotation.id, 'add'))
        annotation.addEventListener('mouseleave', () => toggleActiveClass(annotation.id, 'remove'))
    })
}

function addEventListenersToSVGGroups() {
    document.querySelectorAll('g').forEach(layer => {
        layer.addEventListener('mouseenter', () => toggleActiveClass(layer.id, 'add'))
        layer.addEventListener('mouseleave', () => toggleActiveClass(layer.id, 'remove'))
    })
}

function toggleActiveClass(id, action) {
    const annotation = document.querySelector(`.annotation#${id}`)
    const shape = document.querySelector(`g#${id}`)

    if (annotation) {
        annotation.classList[action]('active')
    }

    if (shape) {
        shape.classList[action]('active')
    }
}