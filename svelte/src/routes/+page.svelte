<script>
	import "$lib/styles.css";
	import Header from "$lib/Header.svelte";
	import Footer from "$lib/Footer.svelte";
	import MainItem from "$lib/MainItem.svelte";
	import HeaderTitle from "$lib/HeaderTitle.svelte";
</script>

<div id="first-section">
	<div id="header">
		<Header>
			<HeaderTitle />
		</Header>
	</div>

	<div class="dashed-1">
		<svg xmlns="http://www.w3.org/2000/svg">
			<line
				x1="100%"
				y1="0"
				x2="100%"
				y2="100%"
				style="stroke: var(--solid-line-color);"
			/>
			<line
				x1="calc(100% - 4.5rem)"
				y1="0"
				x2="100%"
				y2="0"
				style="stroke: var(--solid-line-color);"
			/>
			<linearGradient
				id="first-section-dashed-1-lg"
				gradientUnits="userSpaceOnUse"
				x1="0"
				y1="0"
				x2="25%"
				y2="0"
			>
				<stop offset="0" />
				<stop offset="100%" style="stop-opacity: 0" />
			</linearGradient>
			<line
				x1="0"
				y1="0"
				x2="25%"
				y2="0"
				style="stroke: url(#first-section-dashed-1-lg);"
			/>
		</svg>
	</div>

	<div class="dashed-2">
		<svg>
			<line x1="0" y1="100%" x2="100%" y2="100%" />
			<line x1="0" y1="100%" x2="0" y2="0" />
		</svg>
	</div>

	<div class="container">
		<p id="slogan">
			Если ты можешь это представить, ты можешь это достичь.
		</p>

		<div class="container-dashed">
			<svg>
				<linearGradient
					id="container-dashed-svg-1-lg-1"
					gradientUnits="userSpaceOnUse"
					x1="0"
					y1="0"
					x2="25%"
					y2="0"
				>
					<stop offset="0" />
					<stop offset="100%" style="stop-opacity: 0" />
				</linearGradient>
				<line
					x1="0"
					x2="25%"
					y1="100%"
					y2="100%"
					style="stroke: url(#container-dashed-svg-1-lg-1);"
				/>
				<linearGradient
					id="container-dashed-svg-1-lg-2"
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
					x2="calc(100% - 3rem)"
					y2="100%"
					style="stroke: url(#container-dashed-svg-1-lg-2);"
				/>
				<line
					x1="100%"
					y1="100%"
					x2="100%"
					y2="0"
					style="stroke: var(--solid-line-color);"
				/>
			</svg>
			<svg>
				<linearGradient
					id="container-dashed-svg-2-lg-1"
					gradientUnits="userSpaceOnUse"
					x1="100%"
					y1="0"
					x2="75%"
					y2="0"
				>
					<stop offset="0" />
					<stop offset="100%" style="stop-opacity: 0" />
				</linearGradient>
				<line
					x1="75%"
					x2="100%"
					y1="0"
					y2="0"
					style="stroke: url(#container-dashed-svg-2-lg-1);"
				/>
				<linearGradient
					id="container-dashed-svg-2-lg-2"
					gradientUnits="userSpaceOnUse"
					x1="0"
					y1="0"
					x2="3rem"
					y2="0"
				>
					<stop offset="0" />
					<stop offset="100%" style="stop-opacity: 0" />
				</linearGradient>
				<line
					x1="0"
					y1="0"
					x2="3rem"
					y2="0"
					style="stroke: url(#container-dashed-svg-2-lg-2);"
				/>
			</svg>
		</div>

		<div class="wrap-container-ul">
			<div class="container-ul">
				<svg class="svg-1" xmlns="http://www.w3.org/2000/svg">
					<linearGradient
						id="container-ul-lg-1"
						gradientUnits="userSpaceOnUse"
						x1="100%"
						y1="100%"
						x2="0"
						y2="100%"
					>
						<stop offset="0" />
						<stop offset="70%" style="stop-opacity: 0" />
					</linearGradient>
					<line
						x1="0"
						y1="0"
						x2="100%"
						y2="0"
						style="stroke: url(#container-ul-lg-1);"
					/>
				</svg>

				<div class="wrap-ul">
					<svg xmlns="http://www.w3.org/2000/svg">
						<rect x="0" y="0" width="100%" height="100%" />
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
					<linearGradient
						id="container-ul-lg-2"
						gradientUnits="userSpaceOnUse"
						x1="0"
						y1="100%"
						x2="100%"
						y2="100%"
					>
						<stop offset="0" />
						<stop offset="70%" style="stop-opacity: 0" />
					</linearGradient>
					<line
						x1="0"
						y1="100%"
						x2="100%"
						y2="100%"
						style="stroke: url(#container-ul-lg-2);"
					/>
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
				id="second-section-dashed-1-lg-1"
				gradientUnits="userSpaceOnUse"
				x1="0"
				x2="7.5rem"
				y1="0"
				y2="0"
			>
				<stop offset="0" />
				<stop offset="100%" style="stop-opacity: 0" />
			</linearGradient>
			<linearGradient
				id="second-section-dashed-1-lg-2"
				gradientUnits="userSpaceOnUse"
				x1="0"
				x2="0"
				y1="0"
				y2="7.5rem"
			>
				<stop offset="0" />
				<stop offset="100%" style="stop-opacity: 0" />
			</linearGradient>
			<linearGradient
				id="second-section-dashed-1-lg-3"
				gradientUnits="userSpaceOnUse"
				x1="0"
				x2="0"
				y1="100%"
				y2="calc(100% - 7.5rem)"
			>
				<stop offset="0" />
				<stop offset="100%" style="stop-opacity: 0" />
			</linearGradient>
			<line
				x1="0"
				x2="7.5rem"
				y1="0"
				y2="0"
				style="stroke: url(#second-section-dashed-1-lg-1);"
			/>
			<line
				x1="0"
				x2="0"
				y1="0"
				y2="7.5rem"
				style="stroke: url(#second-section-dashed-1-lg-2);"
			/>
			<line
				x1="0"
				x2="0"
				y1="100%"
				y2="calc(100% - 7.5rem)"
				style="stroke: url(#second-section-dashed-1-lg-3);"
			/>
		</svg>
	</div>

	<div class="dashed-2">
		<svg>
			<linearGradient
				id="second-section-dashed-2-lg"
				gradientUnits="userSpaceOnUse"
				x1="100%"
				x2="0"
				y1="0"
				y2="0"
			>
				<stop offset="0" />
				<stop offset="100%" style="stop-opacity: 0" />
			</linearGradient>
			<line
				x1="100%"
				x2="0"
				y1="0"
				y2="0"
				style="stroke: url(#second-section-dashed-2-lg);"
			/>
		</svg>
	</div>

	<div class="dashed-3">
		<svg>
			<circle cx="100%" cy="0" r="100%"/>
		</svg>
	</div>

	<div id="container-about">
		<svg class="svg-1">
			<line x1="0" x2="0" y1="0" y2="100%" />
		</svg>
		<div id="wrap-about">
			<svg>
				<line x1="0" x2="8rem" y1="0" y2="0" />
				<line x1="0" x2="0" y1="0" y2="8rem" />
				<line x1="100%" x2="calc(100% - 8rem)" y1="100%" y2="100%" />
				<line x1="100%" x2="100%" y1="100%" y2="calc(100% - 8rem)" />
			</svg>
			<p id="about" lang="ru">
				Привет, дорогой читатель. Меня зовут Андрей. Мне 22 года, я
				студент, которому интересно познавать новое и делиться этим с
				другими. Это мой личный сайт, на котором я выкладываю свои
				статьи, иногда курсы, блоги и просто размышления на интересные
				для меня темы. Заваривай чай и присаживайся поудобнее.
			</p>
		</div>
		<svg class="svg-2">
			<linearGradient
				id="container-about-svg-2-lg"
				gradientUnits="userSpaceOnUse"
				x1="100%"
				y1="100%"
				x2="100%"
				y2="50%"
			>
				<stop offset="0" />
				<stop offset="100%" style="stop-opacity: 0" />
			</linearGradient>
			<line
				x1="100%"
				x2="100%"
				y1="100%"
				y2="0"
				style="stroke: url(#container-about-svg-2-lg);"
			/>
		</svg>
	</div>
</div>

<div class="h-line" />
<div id="third-section">
	<MainItem src="test.png" alt="test">
		<h2>
			New! Раскрой свои навыки программирования на этом бесплатном курсе
			по Python
		</h2>
		<p>
			Python - это мощный язык программирования, находящий свое применение
			в web-разработке, в научных вычислениях, как скриптовый язык и в
			других самых разных областях. Этот язык невероятно удобен и
			лаконичен, и поэтому является одним из самых популярных и
			востребованных языков в современном IT.
		</p>
	</MainItem>
</div>

<div class="h-line" />
<Footer />

<style>
	.h-line {
		width: 100%;
		height: 1px;
		background-color: var(--solid-line-color);
	}

	#header {
		position: fixed;
		top: 0;
		width: 100%;
		z-index: 1;
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

	#first-section .wrap-ul svg rect {
		fill: none;
		stroke: var(--dashed-line-color);
		stroke-width: var(--dashed-line-width);
		stroke-dasharray: var(--line-dasharray);
	}

	#first-section .container-ul svg line {
		fill: none;
		stroke-width: var(--dashed-line-width);
		stroke-dasharray: var(--line-dasharray);
	}

	#first-section .container-ul .svg-1 {
		height: var(--dashed-line-width);
		width: 100%;
	}

	#first-section .container-ul .svg-2 {
		height: var(--dashed-line-width);
		width: 100%;
		align-self: end;
	}

	#first-section .container-ul linearGradient stop {
		stop-color: var(--dashed-line-color);
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

	#first-section .dashed-1 svg line {
		stroke-dasharray: var(--line-dasharray);
		fill: none;
		stroke-width: var(--dashed-line-width);
	}

	#first-section .dashed-1 svg linearGradient stop {
		stop-color: var(--dashed-line-color);
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

	#first-section .dashed-2 svg line {
		stroke-dasharray: var(--line-dasharray);
		fill: none;
		stroke-width: var(--dashed-line-width);
		stroke: var(--solid-line-color);
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

	#first-section .container-dashed svg line {
		stroke-dasharray: var(--line-dasharray);
		fill: none;
		stroke-width: var(--dashed-line-width);
	}

	#first-section .container-dashed svg linearGradient stop {
		stop-color: var(--dashed-line-color);
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

	#second-section #wrap-about svg line {
		stroke-dasharray: var(--line-dasharray);
		fill: none;
		stroke-width: var(--dashed-line-width);
		stroke: var(--solid-line-color);
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
		width: var(--dashed-line-width);
		padding-left: 2rem;
	}

	#second-section #container-about .svg-1 line {
		stroke-dasharray: var(--line-dasharray);
		fill: none;
		stroke-width: var(--dashed-line-width);
		stroke: var(--solid-line-color);
	}

	#second-section #container-about .svg-2 {
		height: var(--margin-bottom);
		width: 100%;
		align-self: end;
	}

	#second-section #container-about .svg-2 line {
		stroke-dasharray: var(--line-dasharray);
		fill: none;
		stroke-width: var(--dashed-line-width);
	}

	#second-section #container-about .svg-2 linearGradient stop {
		stop-color: var(--dashed-line-color);
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

	#second-section .dashed-1 svg line {
		stroke-dasharray: var(--line-dasharray);
		fill: none;
		stroke-width: var(--dashed-line-width);
	}

	#second-section .dashed-1 svg linearGradient stop {
		stop-color: var(--dashed-line-color);
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

	#second-section .dashed-2 svg line {
		stroke-dasharray: var(--line-dasharray);
		fill: none;
		stroke-width: var(--dashed-line-width);
	}

	#second-section .dashed-2 svg linearGradient stop {
		stop-color: var(--dashed-line-color);
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

	#second-section .dashed-3 svg circle {
		stroke-dasharray: var(--line-dasharray);
		fill: none;
		stroke-width: var(--dashed-line-width);
		stroke: var(--solid-line-color);
	}

	/* ---------------------- Third Section ---------------------- */

	#third-section {
		display: flex;
		align-items: center;
		justify-content: center;
	}
</style>
