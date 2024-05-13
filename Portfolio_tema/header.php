<!DOCTYPE html>
<html lang="sv">

<head>
  <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>En fin sida</title>
  <link href="<?php echo get_bloginfo("template_directory"); ?>/style.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" 
	crossorigin="anonymous" referrerpolicy="no-referrer" />  

</head>

<body>
  <div id="container">
    <div id="header">
      <header>
        <h1>Robin internetsida</h1>
        <p>Hejsan din mupp</p>
      </header>
    </div>
    <nav>
      <ul class="wrapper">
        <li class="page_item"><a href="<?php echo home_url(); ?>">Home</a></li>
        <?php wp_list_pages('&title_li=&exclude=63'); ?>
      </ul>
    </nav>