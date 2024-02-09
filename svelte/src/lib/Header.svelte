<nav>
    <slot/>

    <a id="brand" href="/">
        <img src="favicon.svg" alt="The main icon." />
    </a>

    <ul>
        <li>
            <a href="/">Блог</a>
        </li>
        <li>
            <a href="/">Курс</a>
        </li>
    </ul>

</nav>
<div class="h-line" />

<style>
    nav {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        padding: 1rem 4rem 1rem 4rem;
        backdrop-filter: blur(5px);
    }

    @media (max-width: 35rem) {
        nav {
            padding: 1rem 1rem 1rem 1rem;
        }
    }

    ul {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        list-style: none;
        padding: 0;
    }

    ul a {
        padding: 0 0 0 2rem;
        color: rgb(205, 205, 205);
        font-size: 1rem;
        text-decoration: none;
        text-transform: uppercase;
    }

    ul a:hover {
        text-decoration: underline;
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

    .h-line {
		width: 100%;
		height: 1px;
		background-color: var(--solid-line-color);
	}
</style>
