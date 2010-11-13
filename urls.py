from django.conf.urls.defaults import *
import os

# Our URL patterns for tictactoe project
urlpatterns = patterns('',
    # Welcome/Index/Main view for tictactoe
    (r'^$', 'tic_tac_toe.views.index'),
    (r'^index.html$', 'tic_tac_toe.views.index'),
    
    # Game view for tictactoe
    url(r'^game/(?P<user>\w+)/$', 'tic_tac_toe.views.game', name='game-home'),
    url(r'^easy_game/(?P<user>\w+)/$', 'tic_tac_toe.views.game', 
        kwargs={'difficulty': 'easy'}, name='game-home-easy'),

    
    # Game Over View for tictactoe
    url(r'^game/(?P<user>\w+)/game_over/$', 'tic_tac_toe.views.game_over', name='game-over'),

    # Move Action for tictactoe
    (r'^game/(?P<user>\w+)/move/(?P<position>\d{1})/$', 'tic_tac_toe.views.move'),
    
    # Reset game state for tictactoe
    (r'^game/(?P<user>\w+)/new_game/$', 'tic_tac_toe.views.new_game'),
    
    # Change difficulty for tictacttoe
    (r'^game/(?P<user>\w+)/change_difficulty/$', 'tic_tac_toe.views.change_difficulty'),
 
    # For serving static media like CSS (for quick demoability)
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.getcwd(), 'media'), 'show_indexes': True}),
)
