<script>
	import "$lib/styles.css";
	import Header from "$lib/Header.svelte";
	import Footer from "$lib/Footer.svelte";
	import MainItem from "$lib/MainItem.svelte";
	import { onMount } from "svelte";
	import { tweened } from "svelte/motion";
	import { cubicInOut } from "svelte/easing";
	import { viewport } from "$lib/utils/useViewportAction";
	

	const first_duration = 500;
	const second_duration = 1000;

	// --------------------- Section 1 ---------------------
	const s1_w_ul_v1 = tweened(0, { duration: first_duration, easing: cubicInOut });
	const s1_w_ul_v2 = tweened(0, { duration: first_duration, easing: cubicInOut });
	const s1_w_ul_v3 = tweened(100, { duration: first_duration, easing: cubicInOut });
	const s1_w_ul_v4 = tweened(100, { duration: first_duration, easing: cubicInOut });
	const s1_c_ul_v1 = tweened(100, { duration: first_duration, easing: cubicInOut });
	const s1_c_ul_v2 = tweened(0, { duration: first_duration, easing: cubicInOut });

	const s1_cd_v1 = tweened(0, { duration: first_duration, easing: cubicInOut });
	const s1_cd_v2 = tweened(0, { duration: first_duration, easing: cubicInOut });
	const s1_cd_v3 = tweened(0, { duration: first_duration, easing: cubicInOut });
	const s1_cd_v4 = tweened(100, { duration: first_duration, easing: cubicInOut });

	const s1_d2_v1 = tweened(0, { duration: second_duration, easing: cubicInOut });
	const s1_d2_v2 = tweened(100, { duration: second_duration, easing: cubicInOut });
	const s1_d1_v1 = tweened(0, { duration: second_duration, easing: cubicInOut });
	const s1_d1_v2 = tweened(0, { duration: second_duration, easing: cubicInOut });
	const s1_d1_v3 = tweened(0, { duration: first_duration, easing: cubicInOut });

	onMount(async () => {
		await Promise.all([s1_w_ul_v1.set(100), s1_w_ul_v3.set(0)]);
		await Promise.all([s1_w_ul_v2.set(100), s1_w_ul_v4.set(0)]);
		await Promise.all([s1_c_ul_v1.set(0), s1_c_ul_v2.set(100)]);
	});
	
	onMount(async () => {
		await s1_cd_v1.set(100);
		await s1_cd_v2.set(3);
		await Promise.all([s1_cd_v3.set(25), s1_cd_v4.set(75)]);

		Promise.all([s1_d2_v1.set(100), s1_d2_v2.set(0)]);
		await Promise.all([s1_d1_v1.set(100), s1_d1_v2.set(4.5)]);
		await s1_d1_v3.set(25);
	});

	// --------------------- Section 2 ---------------------
	const s2_w_about_v = tweened(0, { duration: second_duration, easing: cubicInOut });
	const s2_c_about_v1 = tweened(0, { duration: first_duration, easing: cubicInOut });
	const s2_c_about_v2 = tweened(100, { duration: first_duration, easing: cubicInOut });
	const s2_d1_v = tweened(0, { duration: first_duration, easing: cubicInOut });
	const s2_d3_v = tweened(0, { duration: first_duration, easing: cubicInOut });

	async function animation_section2() {
		await s2_w_about_v.set(8);
		await s2_c_about_v1.set(100);
		await s2_c_about_v2.set(0);
		await s2_d1_v.set(7.5);
		await s2_d3_v.set(100);
	}
</script>

<div id="first-section">
	<div id="header">
		<Header>
			<div id="wrap-title">
				<a href="/" id="title">Daiwery</a>
			</div>			
		</Header>
	</div>

	<div class="dashed-1">
		<svg xmlns="http://www.w3.org/2000/svg">
			<line x1="100%" y1="0" x2="100%" y2="{$s1_d1_v1}%" />
			<line x1="calc(100% - {$s1_d1_v2}rem)" y1="0" x2="100%" y2="0" />
			<linearGradient id="first-section-dashed-1-lg" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="25%" y2="0">
				<stop offset="0" />
				<stop offset="100%" style="stop-opacity: 0" />
			</linearGradient>
			<line x1="0" y1="0" x2="{$s1_d1_v3}%" y2="0" style="stroke: url(#first-section-dashed-1-lg);" />
		</svg>
	</div>

	<div class="dashed-2">
		<svg>
			<line x1="0" y1="100%" x2="{$s1_d2_v1}%" y2="100%" />
			<line x1="0" y1="100%" x2="0" y2="{$s1_d2_v2}%" />
		</svg>
	</div>

	<div class="container">
		<p id="slogan">Если ты можешь это представить, ты можешь это достичь.</p>

		<div class="container-dashed">
			<svg>
				<linearGradient id="cd-svg-1-lg-1" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="25%" y2="0">
					<stop offset="0" />
					<stop offset="100%" style="stop-opacity: 0" />
				</linearGradient>
				<line x1="0" x2="{$s1_cd_v3}%" y1="100%" y2="100%" style="stroke: url(#cd-svg-1-lg-1);" />
				<linearGradient
					id="cd-svg-1-lg-2"
					gradientUnits="userSpaceOnUse"
					x1="100%"
					y1="0"
					x2="calc(100% - 3rem)"
					y2="0"
				>
					<stop offset="0" />
					<stop offset="100%" style="stop-opacity: 0" />
				</linearGradient>
				<line
					x1="100%"
					y1="100%"
					x2="calc(100% - {$s1_cd_v2}rem)"
					y2="100%"
					style="stroke: url(#cd-svg-1-lg-2);"
				/>
				<line x1="100%" y1="0" x2="100%" y2="{$s1_cd_v1}%" />
			</svg>
			<svg>
				<linearGradient id="cd-svg-2-lg-1" gradientUnits="userSpaceOnUse" x1="100%" y1="0" x2="75%" y2="0">
					<stop offset="0" />
					<stop offset="100%" style="stop-opacity: 0" />
				</linearGradient>
				<line x1="{$s1_cd_v4}%" x2="100%" y1="0" y2="0" style="stroke: url(#cd-svg-2-lg-1);" />
				<linearGradient id="cd-svg-2-lg-2" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="3rem" y2="0">
					<stop offset="0" />
					<stop offset="100%" style="stop-opacity: 0" />
				</linearGradient>
				<line x1="0" y1="0" x2="{$s1_cd_v2}rem" y2="0" style="stroke: url(#cd-svg-2-lg-2);" />
			</svg>
		</div>

		<div class="wrap-container-ul">
			<div class="container-ul">
				<svg class="svg-1" xmlns="http://www.w3.org/2000/svg">
					<linearGradient id="c-ul-lg-1" gradientUnits="userSpaceOnUse" x1="100%" y1="100%" x2="0" y2="100%">
						<stop offset="0" />
						<stop offset="70%" style="stop-opacity: 0" />
					</linearGradient>
					<line x1="{$s1_c_ul_v1}%" y1="0" x2="100%" y2="0" style="stroke: url(#c-ul-lg-1);" />
				</svg>

				<div class="wrap-ul">
					<svg xmlns="http://www.w3.org/2000/svg">
						<line x1="0" y1="0" x2="0" y2="{$s1_w_ul_v1}%" />
						<line x1="0" y1="100%" x2="{$s1_w_ul_v2}%" y2="100%" />
						<line x1="100%" y1="100%" x2="100%" y2="{$s1_w_ul_v3}%" />
						<line x1="100%" y1="0" x2="{$s1_w_ul_v4}%" y2="0" />
					</svg>
					<ul>
						<li>
							<p>Наука</p>
						</li>
						<li>
							<p>Программирование</p>
						</li>
						<li>
							<p>Блог</p>
						</li>
					</ul>
				</div>

				<svg class="svg-2" xmlns="http://www.w3.org/2000/svg">
					<linearGradient id="c-ul-lg-2" gradientUnits="userSpaceOnUse" x1="0" y1="100%" x2="100%" y2="100%">
						<stop offset="0" />
						<stop offset="70%" style="stop-opacity: 0" />
					</linearGradient>
					<line x1="0" y1="100%" x2="{$s1_c_ul_v2}%" y2="100%" style="stroke: url(#c-ul-lg-2);" />
				</svg>
			</div>
		</div>
	</div>
</div>

<div class="h-line" />
<div id="second-section">
	<div class="dashed-1">
		<svg>
			<linearGradient
				id="s2-dashed-1-lg-1"
				gradientUnits="userSpaceOnUse"
				x1="0"
				x2="{$s2_d1_v}rem"
				y1="0"
				y2="0"
			>
				<stop offset="0" />
				<stop offset="100%" style="stop-opacity: 0" />
			</linearGradient>
			<linearGradient
				id="s2-dashed-1-lg-2"
				gradientUnits="userSpaceOnUse"
				x1="0"
				x2="0"
				y1="0"
				y2="{$s2_d1_v}rem"
			>
				<stop offset="0" />
				<stop offset="100%" style="stop-opacity: 0" />
			</linearGradient>
			<linearGradient
				id="s2-dashed-1-lg-3"
				gradientUnits="userSpaceOnUse"
				x1="0"
				x2="0"
				y1="100%"
				y2="calc(100% - {$s2_d1_v}rem)"
			>
				<stop offset="0" />
				<stop offset="100%" style="stop-opacity: 0" />
			</linearGradient>
			<line x1="0" x2="7.5rem" y1="0" y2="0" style="stroke: url(#s2-dashed-1-lg-1);" />
			<line x1="0" x2="0" y1="0" y2="7.5rem" style="stroke: url(#s2-dashed-1-lg-2);" />
			<line x1="0" x2="0" y1="100%" y2="calc(100% - 7.5rem)" style="stroke: url(#s2-dashed-1-lg-3);" />
		</svg>
	</div>

	<div class="dashed-2">
		<svg>
			<linearGradient id="s2-dashed-2-lg" gradientUnits="userSpaceOnUse" x1="100%" x2="0" y1="0" y2="0">
				<stop offset="0" />
				<stop offset="100%" style="stop-opacity: 0" />
			</linearGradient>
			<line x1="100%" x2="{$s2_c_about_v2}%" y1="0" y2="0" style="stroke: url(#s2-dashed-2-lg);" />
		</svg>
	</div>

	<div class="dashed-3">
		<svg>
			<circle cx="100%" cy="0" r="{$s2_d3_v}%" />
		</svg>
	</div>

	<div id="container-about">
		<svg class="svg-1">
			<line x1="0" x2="0" y1="0" y2="{$s2_c_about_v1}%" />
		</svg>
		<div id="wrap-about">
			<svg>
				<line x1="0" x2="{$s2_w_about_v}rem" y1="0" y2="0" />
				<line x1="0" x2="0" y1="0" y2="{$s2_w_about_v}rem" />
				<line x1="100%" x2="calc(100% - {$s2_w_about_v}rem)" y1="100%" y2="100%" />
				<line x1="100%" x2="100%" y1="100%" y2="calc(100% - {$s2_w_about_v}rem)" />
			</svg>
			<p id="about" lang="ru" use:viewport={0.9} on:enterViewport={() => animation_section2()}>
				Привет, дорогой читатель. Меня зовут Андрей. Мне 22 года, я студент, которому интересно познавать новое
				и делиться этим с другими. Это мой личный сайт, на котором я выкладываю свои статьи, иногда курсы, блоги
				и просто размышления на интересные для меня темы. Заваривай чай и присаживайся поудобнее.
			</p>
		</div>
		<svg class="svg-2">
			<linearGradient id="c-about-svg-2-lg" gradientUnits="userSpaceOnUse" x1="100%" y1="100%" x2="100%" y2="50%">
				<stop offset="0" />
				<stop offset="100%" style="stop-opacity: 0" />
			</linearGradient>
			<line x1="100%" x2="100%" y1="100%" y2="{$s2_c_about_v2}%" style="stroke: url(#c-about-svg-2-lg);" />
		</svg>
	</div>
</div>

<div class="h-line" />
<div id="third-section">
	<MainItem src="test.png" alt="test">

		## Бесплатный курс по Python

		Python -- это мощный язык программирования, находящий свое применение в web-разработке, в научных
		вычислениях, как скриптовый язык и в других самых разных областях.
		
	</MainItem>
</div>

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

	svg line {
		fill: none;
		stroke: var(--solid-line-color);
		stroke-width: var(--solid-line-width);
	}

	linearGradient stop {
		stop-color: var(--solid-line-color);
	}

	svg circle {
		fill: none;
		stroke-width: var(--solid-line-width);
		stroke: var(--solid-line-color);
	}

	/* ---------------------- First Section ---------------------- */

	#first-section {
		height: 100vh;
		position: relative;
	}

	#first-section .container {
		position: absolute;
		top: 30%;
		position: absolute;
		bottom: 5%;
		width: 100%;
		display: grid;
	}

	#first-section #slogan {
		width: 100%;
		margin: 0;
		font-family: "Caveat Variable";
		line-height: 3rem;
		font-size: 4rem;
		text-align: center;
	}

	#first-section .wrap-container-ul {
		display: flex;
		justify-content: center;
		align-self: end;
	}

	#first-section .container-ul {
		display: grid;
		grid-template-columns: 0.7fr 1fr 0.7fr;
	}

	#first-section ul {
		display: flex;
		list-style: none;
		margin: 0;
		padding: 0;
		justify-content: center;
		font-family: "Caveat Variable";
	}

	#first-section ul p {
		padding: 0.5rem 1rem;
		font-size: 1.3rem;
		color: rgb(158, 158, 158);
		margin: 0;
	}

	#first-section .wrap-ul {
		position: relative;
	}

	#first-section .wrap-ul svg {
		position: absolute;
		width: 100%;
		height: 100%;
	}

	#first-section .container-ul .svg-1 {
		height: var(--solid-line-width);
		width: 100%;
	}

	#first-section .container-ul .svg-2 {
		height: var(--solid-line-width);
		width: 100%;
		align-self: end;
	}

	#first-section .dashed-1 {
		position: absolute;
		left: 0;
		top: 17.5%;
		width: 97.5%;
		height: 4.5rem;
	}

	#first-section .dashed-1 svg {
		width: 100%;
		height: 100%;
	}

	#first-section .dashed-2 {
		position: absolute;
		left: 2.5%;
		bottom: 5%;
		width: 4.5rem;
		height: 4.5rem;
	}

	@media (max-width: 38rem) {
		#first-section .dashed-2 {
			visibility: hidden;
		}
	}

	#first-section .dashed-2 svg {
		width: 100%;
		height: 100%;
	}

	#first-section .container-dashed {
		height: 3rem;
		display: grid;
		grid-template-columns: 1fr 1fr;
		align-self: center;
	}

	#first-section .container-dashed svg {
		height: 100%;
		width: 100%;
	}

	/* ---------------------- Second Section ---------------------- */

	#second-section {
		display: flex;
		align-items: center;
		justify-content: center;
		position: relative;

		--margin-top: 5rem;
		--margin-bottom: 5rem;
	}

	#second-section #container-about {
		margin-left: 1rem;
		margin-right: 1rem;
		display: grid;
	}

	#second-section #wrap-about {
		position: relative;
	}

	#second-section #wrap-about svg {
		position: absolute;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		height: 100%;
		width: 100%;
	}

	#second-section #about {
		font-size: 2rem;
		text-align: justify;
		hyphens: auto;
		max-width: 35rem;
		padding: 1rem;
		margin: 0;
		font-family: "Caveat Variable";
	}

	#second-section #container-about .svg-1 {
		height: var(--margin-top);
		width: var(--solid-line-width);
		padding-left: 2rem;
	}

	#second-section #container-about .svg-2 {
		height: var(--margin-bottom);
		width: 100%;
		align-self: end;
	}

	#second-section .dashed-1 {
		position: absolute;
		bottom: 0;
		top: var(--margin-top);
		left: 5%;
		width: 7.5rem;
	}

	@media (max-width: 60rem) {
		#second-section .dashed-1 {
			visibility: hidden;
		}
	}

	#second-section .dashed-1 svg {
		width: 100%;
		height: 100%;
	}

	#second-section .dashed-2 {
		position: absolute;
		bottom: 0;
		right: 0;
		height: var(--margin-bottom);
		width: 7.5rem;
	}

	@media (max-width: 55rem) {
		#second-section .dashed-2 {
			visibility: hidden;
		}
	}

	#second-section .dashed-2 svg {
		width: 100%;
		height: 100%;
	}

	#second-section .dashed-3 {
		position: absolute;
		top: 0;
		right: 0;
		height: 12rem;
		width: 12rem;
	}

	@media (max-width: 62.5rem) {
		#second-section .dashed-3 {
			visibility: hidden;
		}
	}

	#second-section .dashed-3 svg {
		width: 100%;
		height: 100%;
	}

	/* ---------------------- Third Section ---------------------- */

	#third-section {
		display: flex;
		align-items: center;
		justify-content: center;
	}
</style>
