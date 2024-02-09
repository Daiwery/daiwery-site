<div id="left">
	<div id="right">
		<div id="top">
			<div id="bottom">
				<slot />
			</div>
		</div>
	</div>
</div>

<style>
	#bottom {
		background-image: linear-gradient(var(--bottom-dash));
		background-position: bottom;
		background-size: var(--bottom-period) var(--bottom-width);
		background-repeat: repeat-x;
		width: 100%;
		height: 100%;

		&::before {
			background-image: linear-gradient(var(--bottom-gradient));
			background-position: bottom;
			background-size: 100% var(--bottom-width);
			background-repeat: repeat-x;
			content: "";
			position: absolute;
			top: 0;
			right: 0;
			bottom: 0;
			left: 0;
		}
	}

	#top {
		background-image: linear-gradient(var(--top-dash));
		background-position: top;
		background-size: var(--top-period) var(--top-width);
		background-repeat: repeat-x;
		width: 100%;
		height: 100%;

		&::before {
			background-image: linear-gradient(var(--top-gradient));
			background-position: top;
			background-size: 100% var(--top-width);
			background-repeat: repeat-x;
			content: "";
			position: absolute;
			top: 0;
			right: 0;
			bottom: 0;
			left: 0;
		}
	}

	#left {
		background-image: linear-gradient(var(--left-dash));
		background-position: left;
		background-size: var(--left-width) var(--left-period);
		background-repeat: repeat-y;
		position: relative;
		width: 100%;
		height: 100%;

		&::before {
			background-image: linear-gradient(var(--left-gradient));
			background-position: left;
			background-size: var(--left-width) 100%;
			background-repeat: repeat-y;
			content: "";
			position: absolute;
			top: 0;
			right: 0;
			bottom: 0;
			left: 0;
		}
	}

	#right {
		background-image: linear-gradient(var(--right-dash));
		background-position: right;
		background-size: var(--right-width) var(--right-period);
		background-repeat: repeat-y;
		position: relative;
		width: 100%;
		height: 100%;

		&::before {
			background-image: linear-gradient(var(--right-gradient));
			background-position: right;
			background-size: var(--right-width) 100%;
			background-repeat: repeat-y;
			content: "";
			position: absolute;
			top: 0;
			right: 0;
			bottom: 0;
			left: 0;
		}
	}
</style>
