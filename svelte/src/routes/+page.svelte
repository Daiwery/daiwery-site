<script>
	import "$lib/styles.css";
    import Header from "$lib/Header.svelte";
</script>

<div id="body">
	<!-- <img src="main-gradient-1.png" alt="The gradient." id="first-gradient" /> -->
	<div id="first-page">
		<Header/>
		<div class="h-line" />

		<div id="slogan">
			<p>Если ты можешь это представить, ты можешь это достичь.</p>
		</div>

		<ul id="topics-about">
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

	<div>
		<div class="h-line" />

		<!-- <img
			src="main-gradient-2.png"
			alt="The gradient."
			id="second-gradient"
		/> -->

		<p id="about" lang="ru">
			Привет, дорогой читатель. Меня зовут Андрей. Мне 22 года, я студент,
			которому интересно познавать новое и делиться этим с другими. Это
			мой личный сайт, на котором я выкладываю свои статьи, иногда курсы,
			блоги и просто размышления на интересные для меня темы. Заваривай
			чай и присаживайся поудобнее.
		</p>

		<div class="h-line" />

		<h1>Новости и обновления</h1>

		<div id="python">
			<h2>Вышел курс python!</h2>
			<p>Python - это мощный язык программирования.</p>
		</div>
	</div>
	
	<footer>
		<p>
			Политика конфиденциальности
		</p>
		<p>
			@2024 Все права защищены
		</p>
	</footer>
</div>

<style>
	#body {
		padding: 0;
		margin: 0;
		position: absolute;
		left: 0;
		right: 0;
		top: 0;
		margin: 0;
	}

	#first-page {
		height: 100dvh;
		position: relative;
	}

	#first-gradient {
		right: 0;
		top: 0;
		width: 60%;
		z-index: -1;
		position: absolute;
	}

	.h-line {
		width: 100%;
		height: 1px;
		background-color: rgb(64, 64, 64);
	}

	#slogan {
		position: absolute;
		top: 30%;
		font-size: 4rem;
		width: 100%;
		text-align: center;
	}

	#slogan p {
		margin: 0;
		font-family: "Caveat Variable";
		line-height: 3rem;
	}

	#topics-about {
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

	#topics-about p {
		padding: 0 0.5rem;
		margin-right: 1rem;
		font-size: 1.3rem;
		color: rgb(158, 158, 158);
	}

	#second-gradient {
		left: 0;
		z-index: -2;
		position: absolute;
		width: 50%;
	}

	#about {
		font-size: 1.5rem;
		text-align: justify;
		hyphens: auto;
	}

	h1 {
		font-size: 2rem;
	}

	#python {
		border: 3px solid hotpink;
		border-radius: 40px;
		padding-left: 2%;
	}


	/* #contacts {
		margin-bottom: 2rem;
	} */

	footer p {
		text-align: center;
		font-size: 1rem;
		margin: 0;
	}
</style>
