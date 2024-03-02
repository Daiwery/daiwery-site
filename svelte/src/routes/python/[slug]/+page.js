import { error } from '@sveltejs/kit'

export async function load({ params }) {
    try {
        const post = await import(`../../../content/python/${params.slug}.md`);

        return {
            content: post.default,
            metadata: post.metadata
        }
    } catch (e) {
        error(404, `Could not find ${params.slug}`)
    }
}
