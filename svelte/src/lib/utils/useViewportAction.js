let intersectionObserver;

function ensureIntersectionObserver(threshold) {
	if (intersectionObserver) return;
	intersectionObserver = new IntersectionObserver(
		(entries) => {
			entries.forEach(entry => {
				console.log(entry)
				const eventName = entry.isIntersecting ? 'enterViewport' : 'exitViewport';
				entry.target.dispatchEvent(new CustomEvent(eventName));
			});
		}, {threshold: threshold}
	);
}

export function viewport(element, threshold) {
	ensureIntersectionObserver(threshold);
	intersectionObserver.observe(element);
	return {
		destroy() {
			intersectionObserver.unobserve(element);
		}
	}
}

