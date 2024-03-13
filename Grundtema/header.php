<!DOCTYPE html>
<html lang="sv">
<head>
	<meta charset="utf-8" />
	<link href="<?php echo get_bloginfo('template_directory'); ?>/style.css" rel="stylesheet">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" 
	crossorigin="anonymous" referrerpolicy="no-referrer" />
	<title>
		Robins webb
	</title>
</head>
<body>
	<div id="wrapper">
		<header>
		<img id="logotyp" src="http://localhost:8888/wordpress/wp-content/uploads/2024/02/logotyp.png" alt="RRlogotyp" />
			<div id=header-text>
				<h1> Robins Webb  </h1>
				<button id="myButton">Klicka på mig</button>

				
			</div>
		</header>
		<nav>
			<ul>
				<li class="page_item"><a href="<?php echo home_url(); ?>">Home</a></li>
				<?php wp_list_pages( '&title_li=&exclude=63' ); ?>
			</ul>
		</nav>