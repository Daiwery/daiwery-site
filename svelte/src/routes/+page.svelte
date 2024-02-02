<script>
	import "$lib/styles.css";
	import Header from "$lib/Header.svelte";
	import Footer from "$lib/Footer.svelte";
</script>

<div id="first-section">
	<div id="header">
		<Header>
			<div id="wrap-title">
				<a href="/" id="title">Daiwery</a>
			</div>
		</Header>
	</div>

	<p id="slogan">Если ты можешь это представить, ты можешь это достичь.</p>

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

<div class="h-line" />
<div id="second-section">
	<p id="about" lang="ru">
		Привет, дорогой читатель. Меня зовут Андрей. Мне 22 года, я студент,
		которому интересно познавать новое и делиться этим с другими. Это мой
		личный сайт, на котором я выкладываю свои статьи, иногда курсы, блоги и
		просто размышления на интересные для меня темы. Заваривай чай и
		присаживайся поудобнее.
	</p>
</div>

<div class="h-line" />
<div id="third-section">
	<div class="wrapper-main-item">
		<div class="main-item">
			<img src="test.png" class="item-img" alt="test" />
			<div class="wrap-item-text">
				<div class="item-text">
					<h2 lang="ru">
						Раскрой свои навыки программирования на этом бесплатном
						курсе по Python
					</h2>
					<p lang="ru">
						Python - это мощный язык программирования, находящий
						свое применение в web-разработке, в научных вычислениях,
						как скриптовый язык и в других самых разных областях.
						Этот язык невероятно удобен и лаконичен, и поэтому
						является одним из самых популярных и востребованных
						языков в современном IT.
					</p>
					<div class="item-link">
						<a href="/">Перейти</a>
						<img src="right_arrow_icon.svg" alt="The right arrow" />
					</div>
				</div>
			</div>
		</div>
	</div>
</div>

<div class="h-line" />
<Footer />

<style>
	.h-line {
		width: 100%;
		height: 1px;
		background-color: rgb(64, 64, 64);
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
		background: linear-gradient(45deg, black, rgb(25, 25, 25));
	}

	#first-section #slogan {
		position: absolute;
		top: 30%;
		width: 100%;
		margin: 0;
		font-family: "Caveat Variable";
		line-height: 3rem;
		font-size: 4rem;
		text-align: center;
	}

	#first-section ul {
		display: flex;
		list-style: none;
		position: absolute;
		bottom: 5%;
		margin: 0;
		padding: 0;
		width: 100%;
		justify-content: center;
		font-family: "Caveat Variable";
	}

	#first-section ul p {
		padding: 0 1rem;
		font-size: 1.3rem;
		color: rgb(158, 158, 158);
	}

	#second-section {
		display: flex;
		align-items: center;
		justify-content: center;
	}

	#second-section #about {
		font-size: 2rem;
		text-align: justify;
		hyphens: auto;
		max-width: 35rem;
		border: 2px solid rgb(64, 64, 64);
		border-radius: 3rem;
		padding: 1rem;
		font-family: "Caveat Variable";
		margin: 5rem 1rem 5rem 1rem;
	}

	.wrapper-main-item {
		display: flex;
		justify-content: center;
		width: auto;
		max-width: 80rem;
		margin: 3rem 2rem;
	}

	.main-item {
		display: grid;
		justify-content: center;
		grid-template-columns: 1fr 1fr;
		column-gap: 2rem;
	}

	.main-item .item-img {
		width: 100%;
		border-radius: 1rem;
	}

	.main-item .wrap-item-text {
		display: flex;
		align-items: center;
	}

	.main-item .item-text h2 {
		font-size: 1.8rem;
		font-weight: bold;
		margin-top: 0;
		margin-bottom: 1rem;
	}

	.main-item .item-text p {
		font-size: 1.3rem;
		color: rgb(140, 140, 140);
		margin-top: 0;
		margin-bottom: 1rem;
		text-align: justify;
		hyphens: auto;
	}

	@media (max-width: 75rem) {
		.main-item .item-text h2 {
			font-size: 1.5rem;
		}
	}

	@media (max-width: 71rem) {
		.main-item .item-text h2 {
			margin-top: 1rem;
			margin-bottom: 0.5rem;
		}

		.main-item {
			grid-template-columns: none;
		}

		.main-item .item-text p {
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
