<script>
	import "$lib/styles.css";
	import Header from "$lib/Header.svelte";
</script>

<div id="first-section">
	<div id="header"><Header /></div>

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

<div>
	<h1>Новости и обновления</h1>

	<div id="python">
		<h2>Вышел курс python!</h2>
		<p>Python - это мощный язык программирования.</p>
	</div>
</div>

<footer>
	<p>Политика конфиденциальности</p>
	<p>@2024 Все права защищены</p>
</footer>

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
		width: 50%;
		margin-top: 10%;
		margin-bottom: 10%;
		border: 2px solid rgb(64, 64, 64);
		border-radius: 3rem;
		padding: 2rem;
		font-family: "Caveat Variable";
	}


	h1 {
		font-size: 2rem;
	}

	#python {
		border: 3px solid hotpink;
		border-radius: 40px;
		padding-left: 2%;
	}

	footer p {
		text-align: center;
		font-size: 1rem;
		margin: 0;
	}
</style>
