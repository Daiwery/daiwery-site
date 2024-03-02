
export const fetchMarkdownPosts = async () => {
    const allPostFiles = import.meta.glob('../../content/python/*.md');
    const iterablePostFiles = Object.entries(allPostFiles);

    const allPosts = await Promise.all(
        iterablePostFiles.map(async ([path, resolver]) => {
            const { metadata } = await resolver();
            const postPath = path.split('/').at(-1)?.replace('.md', '');

            return {
                meta: metadata,
                path: postPath
            };
        })
    );

    return allPosts;
};