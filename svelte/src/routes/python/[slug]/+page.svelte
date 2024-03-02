<script>
	import "$lib/styles.css";
	import Header from "$lib/Header.svelte";
	import Footer from "$lib/Footer.svelte";

	export let data;
</script>

<div id="header">
	<Header>
		<div id="wrap-title">
			<a href="/" id="title">Python</a>
		</div>
	</Header>
</div>

<main>
	<article>
		<header>
			<h1>
				{data.metadata.title}
			</h1>
		</header>
		<svelte:component this={data.content} />
	</article>
</main>

<div class="h-line" />
<Footer />

<style>
	.h-line {
		width: 100%;
		height: var(--solid-line-width);
		background-color: var(--solid-line-color);
	}

	#header {
		position: fixed;
		top: 0;
		width: 100%;
		z-index: 1;
	}

	#wrap-title {
		display: flex;
		align-items: center;
	}

	#title {
		color: rgb(255, 255, 255);
		font-size: calc(var(--header-height) - 2rem);
		text-decoration: none;
		font-family: "Caveat Variable";
	}

	main {
		margin-top: calc(var(--header-height) + 2rem);
	}

	article {
		max-width: 50rem;
		margin-left: auto;
		margin-right: auto;
	}
</style>
