# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'solstizio89'
insta_password = '$@Hu$8Hu'

comments = ['Nice shot!  ',
        'I love your profile!  ',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use  ?',
        'Love your posts  ',
        'Looks awesome  ',
        'Getting inspired by you  ',
        ':raised_hands: Yes!',
        'I can feel your passion   :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username, password=insta_password, headless_browser=False)

with smart_run(session):
  """ Activity flow """	
  #commenti in inglese	
  #session.set_comments(['Awesome', 'Really Cool', 'I like your stuff','Nice shot!  ','I love your profile!  ','Your feed is an inspiration :thumbsup:','Just incredible :open_mouth:','What camera did you use  ?','Love your posts  ', 'Looks awesome  ','Getting inspired by you  ',':raised_hands: Yes!','I can feel your passion   :muscle:'])

#commenti in italiano
  session.set_comments([#'Awesome dude!','Nice shot!','I love your profile!','Your feed is an inspiration :thumbsup:','Just incredible :open_mouth:','What camera did you use?','Love your posts','Looks awesome','Getting inspired by you',':raised_hands: Yes!','I can feel your passion :muscle:'
        'Spettacolare', 'Veramente bello', 'Mi piace!','Bello scatto!','Complimenti per le foto','Le tue foto sono di ispirazione, grazie','Figo!','Complimenti, che fotocamera hai usato?','Bei post, complimenti','Complimenti, bei post','Di ispirazione, complimenti',':raised_hands: Figo!','Complimenti, continua così! :muscle:', 'Grande!'
        ])
  session.set_do_comment(enabled=True, percentage=80)
  # general settings		
  session.set_dont_include(["deniseluzii", "friend2", "friend3"])		
  
  # activity		
  #session.like_by_tags(["abruzzo","marche"], amount=40)

  session.like_by_tags(['sentiero'], amount=100, interact=True)
  session.follow_by_tags(['meraviglioso'], amount=0)
  
  #session.set_comments(comments)
  #session.join_pods(topic='sports', engagement_mode='no_comments')

  #following
  session.set_do_follow(enabled=True, percentage=50)
  session.set_quota_supervisor(enabled=True, peak_follows_daily=560, peak_follows_hourly=56, peak_unfollows_hourly=49, peak_unfollows_daily=550, sleep_after=["follows_h", "unfollows_d"], stochastic_flow=True, notify_me=True)
  session.set_user_interact(amount=3, randomize=True, percentage=90, media='Photo')
  #salta gli utenti senza immagine del profilo
  session.set_skip_users(skip_private=True, skip_no_profile_pic=True, no_profile_pic_percentage=100)

  session.set_relationship_bounds(enabled=True, potency_ratio=1.34, delimit_by_numbers=True, max_followers=8500, max_following=4490, min_followers=100, min_following=56, min_posts=10, max_posts=1000)
  
  #delay tra le azioni
  session.set_action_delays(enabled=True, like=5.2, randomize=True, random_range_from=70, random_range_to=210)