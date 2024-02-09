<script>
	import "$lib/styles.css";
	import Header from "$lib/Header.svelte";
	import Footer from "$lib/Footer.svelte";
	import MainItem from "$lib/MainItem.svelte";
	import DashedBorder from "$lib/DashedBorder.svelte";
</script>

<div id="first-section">
	<div id="header">
		<Header>
			<div id="wrap-title">
				<a href="/" id="title">Daiwery</a>
			</div>
		</Header>
	</div>

	<div class="wrap-dashed-1">
		<DashedBorder>
			<div class="dashed-1" />
		</DashedBorder>
	</div>

	<div class="wrap-dashed-2">
		<DashedBorder>
			<div class="dashed-2" />
		</DashedBorder>
	</div>

	<div class="container">
		<p id="slogan">
			Если ты можешь это представить, ты можешь это достичь.
		</p>

		<div class="wrap-dashed-3">
			<div class="wrap-dashed-3-item-1">
				<DashedBorder />
			</div>
			<div class="wrap-dashed-3-item-2">
				<DashedBorder />
			</div>
		</div>

		<div class="container-ul">
			<div class="wrap-dashed-ul">
				<div class="dashed-ul-item1">
					<DashedBorder>
						<div style="height: var(--dash-width)" />
					</DashedBorder>
				</div>
				<div class="wrap-ul">
					<DashedBorder>
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
					</DashedBorder>
				</div>
				<div class="dashed-ul-item2">
					<DashedBorder>
						<div style="height: var(--dash-width);" />
					</DashedBorder>
				</div>
			</div>
		</div>
	</div>
</div>

<div class="h-line" />
<div id="second-section">
	<div class="dashed-1">
		<DashedBorder>
			<div style="width: 100%; height: 100%" />
		</DashedBorder>
	</div>

	<div class="dashed-2">
		<DashedBorder>
			<div style="width: 100%; height: 100%" />
		</DashedBorder>
	</div>

	<div id="container-about">
		<div class="wrap-dashed-about-item-1">
			<DashedBorder>
				<div class="dashed-about-item-1" />
			</DashedBorder>
		</div>
		<div id="wrap-about">
			<DashedBorder>
				<p id="about" lang="ru">
					Привет, дорогой читатель. Меня зовут Андрей. Мне 22 года, я
					студент, которому интересно познавать новое и делиться этим
					с другими. Это мой личный сайт, на котором я выкладываю свои
					статьи, иногда курсы, блоги и просто размышления на
					интересные для меня темы. Заваривай чай и присаживайся
					поудобнее.
				</p>
			</DashedBorder>
		</div>
		<div class="wrap-dashed-about-item-2">
			<DashedBorder>
				<div class="dashed-about-item-2" />
			</DashedBorder>
		</div>
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

	#wrap-title {
		display: flex;
		align-items: center;
	}

	#title {
		color: rgb(255, 255, 255);
		font-size: 2.5rem;
		text-decoration: none;
		font-family: "Caveat Variable";
	}

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

	#first-section .container-ul {
		display: flex;
		justify-content: center;
		align-self: end;
	}

	#first-section .wrap-dashed-ul {
		display: grid;
		grid-template-columns: 0.7fr 1fr 0.7fr;
	}

	#first-section .wrap-ul {
		--left-dash: to top, var(--dash);
		--left-period: var(--dash-period);
		--left-width: var(--dash-width);

		--right-dash: to bottom, var(--dash);
		--right-period: var(--dash-period);
		--right-width: var(--dash-width);

		--bottom-dash: to left, var(--dash);
		--bottom-period: var(--dash-period);
		--bottom-width: var(--dash-width);

		--top-dash: to right, var(--dash);
		--top-period: var(--dash-period);
		--top-width: var(--dash-width);
	}

	#first-section .dashed-ul-item1 {
		--top-dash: to left, var(--dash);
		--top-period: var(--dash-period);
		--top-width: var(--dash-width);
		--top-gradient: to right, var(--background-color) 30%,
			rgba(0, 0, 0, 0) 100%;
	}

	#first-section .dashed-ul-item2 {
		align-self: end;
		--bottom-dash: to right, var(--dash);
		--bottom-period: var(--dash-period);
		--bottom-width: var(--dash-width);
		--bottom-gradient: to left, var(--background-color) 30%,
			rgba(0, 0, 0, 0) 100%;
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

	#first-section .wrap-dashed-1 {
		position: absolute;
		left: 0;
		top: 17.5%;
		width: 97.5%;
		--length: 4.5rem;

		--top-dash: to left, var(--dash);
		--top-period: var(--dash-period);
		--top-width: var(--dash-width);
		--top-gradient: to left, rgba(0, 0, 0, 0) var(--length),
			var(--background-color) var(--length), var(--background-color) 75%,
			rgba(0, 0, 0, 0);
		--right-dash: to bottom, var(--dash);
		--right-period: var(--dash-period);
		--right-width: var(--dash-width);
	}
	#first-section .dashed-1 {
		width: 100%;
		height: var(--length);
	}

	#first-section .wrap-dashed-2 {
		position: absolute;
		left: 2.5%;
		bottom: 5%;
		--length: 4.5rem;

		--bottom-dash: to right, var(--dash);
		--bottom-period: var(--dash-period);
		--bottom-width: var(--dash-width);
		--left-dash: to top, var(--dash);
		--left-period: var(--dash-period);
		--left-width: var(--dash-width);
	}

	@media (max-width: 38rem) {
		#first-section .wrap-dashed-2 {
			visibility: hidden;
		}
	}

	#first-section .dashed-2 {
		width: var(--length);
		height: var(--length);
	}

	#first-section .wrap-dashed-3 {
		--length: 3rem;
		height: var(--length);
		display: grid;
		grid-template-columns: 1fr 1fr;
		align-self: center;
	}

	#first-section .wrap-dashed-3-item-1 {
		--bottom-dash: to right, var(--dash);
		--bottom-period: var(--dash-period);
		--bottom-width: var(--dash-width);
		--bottom-gradient: to left, rgba(0, 0, 0, 0),
			var(--background-color) var(--length), var(--background-color) 75%,
			rgba(0, 0, 0, 0);

		--right-dash: to top, var(--dash);
		--right-period: var(--dash-period);
		--right-width: var(--dash-width);
	}

	#first-section .wrap-dashed-3-item-2 {
		--top-dash: to right, var(--dash);
		--top-period: var(--dash-period);
		--top-width: var(--dash-width);
		--top-gradient: to right, rgba(0, 0, 0, 0),
			var(--background-color) var(--length), var(--background-color) 75%,
			rgba(0, 0, 0, 0);
	}

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
	}

	#second-section #wrap-about {
		--length: 8rem;

		--left-dash: to bottom, var(--dash);
		--left-period: var(--dash-period);
		--left-width: var(--dash-width);
		--left-gradient: to bottom, rgba(0, 0, 0, 0) 0,
			rgba(0, 0, 0, 0) var(--length),
			var(--background-color) var(--length);
		--top-dash: to right, var(--dash);
		--top-period: var(--dash-period);
		--top-width: var(--dash-width);
		--top-gradient: to right, rgba(0, 0, 0, 0) 0,
			rgba(0, 0, 0, 0) var(--length),
			var(--background-color) var(--length);

		--bottom-dash: to left, var(--dash);
		--bottom-period: var(--dash-period);
		--bottom-width: var(--dash-width);
		--bottom-gradient: to left, rgba(0, 0, 0, 0) 0,
			rgba(0, 0, 0, 0) var(--length),
			var(--background-color) var(--length);
		--right-dash: to top, var(--dash);
		--right-period: var(--dash-period);
		--right-width: var(--dash-width);
		--right-gradient: to top, rgba(0, 0, 0, 0) 0,
			rgba(0, 0, 0, 0) var(--length),
			var(--background-color) var(--length);
	}

	#second-section .wrap-dashed-about-item-1 {
		--left-dash: to bottom, var(--dash);
		--left-period: var(--dash-period);
		--left-width: var(--dash-width);
		padding-left: 2rem;
	}

	#second-section .dashed-about-item-1 {
		height: var(--margin-top);
		width: 100%;
	}

	#second-section .wrap-dashed-about-item-2 {
		--right-dash: to bottom, var(--dash);
		--right-period: var(--dash-period);
		--right-width: var(--dash-width);
		--right-gradient: to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1) 50%;
	}

	#second-section .dashed-about-item-2 {
		height: var(--margin-bottom);
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

	#second-section .dashed-1 {
		position: absolute;
		bottom: 0;
		top: var(--margin-top);
		left: 5%;

		--length: 7.5rem;
		width: var(--length);

		--left-dash: to top, var(--dash);
		--left-period: var(--dash-period);
		--left-width: var(--dash-width);
		--left-gradient: to bottom, rgba(0, 0, 0, 0),
			var(--background-color) var(--length),
			var(--background-color) calc(100% - var(--length)), rgba(0, 0, 0, 0);

		--top-dash: to right, var(--dash);
		--top-period: var(--dash-period);
		--top-width: var(--dash-width);
		--top-gradient: to right, rgba(0, 0, 0, 0),
			var(--background-color) var(--length);
	}

	@media (max-width: 60rem) {
		#second-section .dashed-1 {
			visibility: hidden;
		}
	}

	#second-section .dashed-2 {
		position: absolute;
		bottom: 0;
		right: 0;
		height: var(--margin-bottom);

		--length: 7.5rem;
		width: var(--length);

		--top-dash: to left, var(--dash);
		--top-period: var(--dash-period);
		--top-width: var(--dash-width);
		--top-gradient: to left, rgba(0, 0, 0, 0),
			var(--background-color) var(--length);
	}

	@media (max-width: 55rem) {
		#second-section .dashed-2 {
			visibility: hidden;
		}
	}
</style>
