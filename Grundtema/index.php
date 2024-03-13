<?php get_header(); ?>
	<div class="main">
		<div id="startsida">
			<article> 
				<h5 class="hiddenheader">Jag syns inte</h5>
				<?php if ( have_posts() ) : while ( have_posts() ) : the_post();?>
					<section>
						<h2><?php the_title(); ?></h2>
							<div><?php the_content(); ?></div>
								<p><?php the_author(); ?></p>
					</section>
				<?php endwhile; endif;?>
			</article>
		</div>
<?php get_sidebar(); ?>
<?php get_footer(); ?>