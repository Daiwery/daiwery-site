<footer>
	<a id="privacy" href="/">Политика конфиденциальности</a>
    <p id="copyright">Все права защищены © 2024 Daiwery</p>
    <div id="contacts">
        <img src="telegram_icon.svg" alt="Telegram." />
        <img src="email_icon.svg" alt="Mail." />
        <img src="github_icon.svg" alt="Github." />
    </div>
</footer>


<style>
    footer {
        margin: 2rem 2rem 1rem 2rem;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
    }

    #privacy {
        font-size: 1rem;
        color: rgb(185, 184, 184);
        margin: 0;
        text-decoration: none;
    }

    #privacy:hover {
        text-decoration: underline;
    }

    #contacts {
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }

    #contacts img {
        width: 1.3rem;
        padding: 0 1.2rem 0 0;
        filter: invert(1);
    }

    #copyright {
        font-size: 1rem;
        color: rgb(140, 140, 140);
        text-align: center;
        margin: 0;
    }
</style>
