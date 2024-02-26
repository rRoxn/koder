<?php
    /**
    * Template Name: Mallsida
    */
?>  
<?php get_header(); ?>
<div class="main">
			<div id="contentsidor">
				<article> 
					<section>
						<?php 
						if ( have_posts() ) : while ( have_posts() ) : the_post();
							get_template_part( 'content', get_post_format() );
						endwhile; endif; 
						the_content(); ?>
					</section>
				</article>
			</div>

<?php get_footer(); ?>