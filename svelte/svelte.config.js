import adapter from "@sveltejs/adapter-static";
import { mdsvex } from "mdsvex";

export default {
	kit: {
		adapter: adapter({
			fallback : "index.html"
		})
	},
	extensions: [".svelte", ".md"],
	preprocess: mdsvex({ extensions: [".svelte", ".md"] }),
};