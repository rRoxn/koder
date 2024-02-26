<?php get_header(); ?>
<div class="main">
			<div id="startsida">
				<article> 
					<?php 
					if ( have_posts() ) : while ( have_posts() ) : the_post();?>
					<section>
						<h1><?php the_title(); ?></h1>
						<p><?php the_content(); ?></p>
						<P><?php the_author(); ?></p>
					</section>
					<?php endwhile; endif;?>
				</article>
			</div>
<?php get_sidebar(); ?>
<?php get_footer(); ?>