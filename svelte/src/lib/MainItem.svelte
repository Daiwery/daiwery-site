<script>
	import { tweened } from "svelte/motion";
	import { cubicInOut } from "svelte/easing";
	import viewport from "$lib/useViewportAction";

	export let src = "";
	export let alt = "";

	const v1 = tweened(0, { duration: 1000, easing: cubicInOut });
	const v2 = tweened(0, { duration: 1000, easing: cubicInOut });

	async function animation() {
		await Promise.all([v1.set(5), v2.set(10)]);
	}
</script>

<div class="wrapper-main-item" use:viewport on:enterViewport={() => animation()}>
	<svg>
		<line x1="0" x2="{$v1}rem" y1="0" y2="0" />
		<line x1="0" x2="0" y1="0" y2="{$v1}rem" />
		<line x1="100%" x2="calc(100% - {$v2}rem)" y1="100%" y2="100%" style="stroke-width: 2px" />
		<line x1="100%" x2="100%" y1="100%" y2="calc(100% - {$v2}rem)" />
	</svg>
	<div class="main-item">
		<img {src} class="item-img" {alt} />
		<div class="wrap-item-text">
			<div class="item-text">
				<slot />
				<div class="item-link">
					<a href="/">Перейти</a>
					<img src="right_arrow_icon.svg" alt="The right arrow" />
				</div>
			</div>
		</div>
	</div>
</div>

<style>
	.wrapper-main-item {
		display: flex;
		justify-content: center;
		width: auto;
		max-width: 80rem;
		margin: 1.5rem 1rem;
		position: relative;
	}

	svg {
		position: absolute;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		height: 100%;
		width: 100%;
	}

	svg line {
		fill: none;
		stroke-width: var(--solid-line-width);
		stroke: var(--solid-line-color);
	}

	.main-item {
		display: grid;
		justify-content: center;
		grid-template-columns: 1fr 1fr;
		column-gap: 2rem;
		padding: 1.5rem 1rem;
		margin-right: 3rem;
	}

	.main-item .item-img {
		width: 100%;
		border-radius: 1rem;
	}

	.main-item .wrap-item-text {
		display: flex;
		align-items: center;
	}

	.main-item .item-text :global(h2) {
		font-size: 1.8rem;
		font-weight: bold;
		margin-top: 0;
		margin-bottom: 1rem;
	}

	.main-item .item-text :global(p) {
		font-size: 1.3rem;
		color: rgb(140, 140, 140);
		margin-top: 0;
		margin-bottom: 1rem;
		text-align: justify;
		hyphens: auto;
	}

	@media (max-width: 75rem) {
		.main-item .item-text :global(h2) {
			font-size: 1.5rem;
		}

		.main-item {
			margin-right: 0;
		}
	}

	@media (max-width: 71rem) {
		.wrapper-main-item {
			margin: 0.75rem 0.5rem;
		}

		.main-item .item-text :global(h2) {
			margin-top: 1rem;
			margin-bottom: 0.5rem;
		}

		.main-item {
			grid-template-columns: none;
			padding: 0.75rem 0.5rem;
		}

		.main-item .item-text :global(p) {
			margin-bottom: 0.5rem;
		}
	}

	.main-item .item-text .item-link {
		display: flex;
		align-items: center;
	}

	.main-item .item-text .item-link a {
		color: rgb(255, 255, 255);
		font-size: 1.3rem;
		text-decoration: none;
		margin: 0;
	}

	.main-item .item-text .item-link a:hover {
		text-decoration: underline;
	}

	.main-item .item-text .item-link img {
		width: 1rem;
		filter: invert(1);
		margin-left: 0.25rem;
		padding-top: 0.2rem;
	}
</style>
