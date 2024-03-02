export const load = async ({ fetch }) => {
	try {
		const response = await fetch(`/api/python`);
		const posts = await response.json();

		return {
			posts
		};
	} catch (e) {
		error(404, `Could not find ${params.slug}`)
	}
};