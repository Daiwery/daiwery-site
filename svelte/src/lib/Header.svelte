<nav>
    <ul>
        <li>
            <a href="/">Блог</a>
        </li>
        <li>
            <a href="/">Курс</a>
        </li>
        <!-- <li>
            <a href="/">Обо мне</a>
        </li> -->
    </ul>

    <div id="brand">
        <img src="favicon.svg" alt="The main icon." />
    </div>

    <div id="contacts">
        <img src="telegram_icon.svg" alt="Telegram." />
        <img src="email_icon.svg" alt="Mail." />
        <img src="github_icon.svg" alt="Github." />
    </div>
</nav>
<div class="h-line" />

<style>
    nav {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        padding: 1rem 4rem 1rem 4rem;
        backdrop-filter: blur(5px);
    }

    ul {
        display: flex;
        align-items: center;
        list-style: none;
        padding: 0;
    }

    ul a {
        padding: 0 1rem;
        color: rgb(205, 205, 205);
        font-size: 1rem;
        text-decoration: none;
        text-transform: uppercase;
    }

    #brand {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    #brand img {
        height: 2.5rem;
        filter: invert(1);
    }

    #contacts {
        display: flex;
        align-items: center;
        justify-content: end;
    }

    #contacts img {
        width: 1.3rem;
        padding: 0 0.6rem;
        filter: invert(1);
    }

    .h-line {
		width: 100%;
		height: 1px;
		background-color: rgb(64, 64, 64);
	}
</style>
