<script>
	let count = 1;

	// the `$:` means 're-run whenever these values change'
	$: doubled = count * 6;
	$: quadrupled = doubled * 12;

	function handleClick() {
		count += 1;
	}
</script>

<button on:click={handleClick}>
	Count: {count}
</button>

<p>{count} * 6 = {doubled}</p>
<p>{doubled} * 12 = {quadrupled}</p>
