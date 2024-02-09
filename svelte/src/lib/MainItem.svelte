<script>
	import DashedBorder from "./DashedBorder.svelte";

	export let src = "";
	export let alt = "";
</script>

<div class="wrapper-main-item">
	<DashedBorder>
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
	</DashedBorder>
</div>

<style>
	.wrapper-main-item {
		display: flex;
		justify-content: center;
		width: auto;
		max-width: 80rem;
		margin: 1.5rem 1rem;

		--length-1: 5rem;
		--length-2: 10rem;

		--left-dash: to bottom, var(--dash);
		--left-period: var(--dash-period);
		--left-width: var(--dash-width);
		--left-gradient: to bottom, rgba(0, 0, 0, 0) 0,
			rgba(0, 0, 0, 0) var(--length-1),
			var(--background-color) var(--length-1);
		--top-dash: to right, var(--dash);
		--top-period: var(--dash-period);
		--top-width: var(--dash-width);
		--top-gradient: to right, rgba(0, 0, 0, 0) 0,
			rgba(0, 0, 0, 0) var(--length-1),
			var(--background-color) var(--length-1);

		--bottom-dash: to left, var(--dash);
		--bottom-period: var(--dash-period);
		--bottom-width: var(--dash-width);
		--bottom-gradient: to left, rgba(0, 0, 0, 0) 0,
			rgba(0, 0, 0, 0) var(--length-2),
			var(--background-color) var(--length-2);
		--right-dash: to top, var(--dash);
		--right-period: var(--dash-period);
		--right-width: var(--dash-width);
		--right-gradient: to top, rgba(0, 0, 0, 0) 0,
			rgba(0, 0, 0, 0) var(--length-2),
			var(--background-color) var(--length-2);
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
