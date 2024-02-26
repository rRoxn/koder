<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<link href="<?php echo get_bloginfo('template_directory'); ?>/style.css" rel="stylesheet">
	<title>
	</title>
</head>
<body>
	<div id="wrapper">
		<header>
			<div>
				<h1> Robins Webb  </h1>

			</div>
		</header>
		<nav>
			<ul>
				<li class="page_item"><a href="<?php echo home_url(); ?>">Home</a></li>
				<?php wp_list_pages( '&title_li=&exclude=63' ); ?>
			</ul>
		</nav>