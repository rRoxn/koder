<?php get_header(); ?>

<article>
	<?php
	if (have_posts()) : while (have_posts()) : the_post(); ?>
			<section>
				<h1><?php the_title(); ?></h1>
				<div><?php the_content(); ?></div>
			</section>
	<?php endwhile;
	endif; ?>
</article>

<?php get_sidebar(); ?>
<?php get_footer(); ?>