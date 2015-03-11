from django.conf.urls import patterns, url

from .views import (
    picturegallery,
    dashboard,
    events,
    approvals,
    suggestions,
    vidly_media,
    comments,
    loggedsearches,
    users,
    groups,
    channels,
    locations,
    regions,
    templates,
    tags,
    recruitmentmessages,
    surveys,
    flatpages,
    url_transforms,
    cronlogger,
    permissions,
    autocompeter,
)


urlpatterns = patterns(
    '',
    url(r'^/?$', dashboard.dashboard, name='dashboard'),
    url(r'^data/$', dashboard.dashboard_data, name='dashboard_data'),
    url(r'^users/(?P<id>\d+)/$', users.user_edit, name='user_edit'),
    url(r'^users/$', users.users, name='users'),
    url(r'^users/data/$', users.users_data, name='users_data'),
    url(r'^groups/(?P<id>\d+)/$', groups.group_edit, name='group_edit'),
    url(r'^groups/remove/(?P<id>\d+)/$', groups.group_remove,
        name='group_remove'),
    url(r'^groups/new/$', groups.group_new, name='group_new'),
    url(r'^groups/$', groups.groups, name='groups'),
    url(r'^events/request/$', events.event_request, name='event_request'),
    url(r'^events/(?P<id>\d+)/$', events.event_edit, name='event_edit'),
    url(r'^events/(?P<id>\d+)/privacy-vidly-mismatch/$',
        events.event_privacy_vidly_mismatch,
        name='event_privacy_vidly_mismatch'),
    url(r'^events/(?P<id>\d+)/assignment/$',
        events.event_assignment,
        name='event_assignment'),
    url(r'^events/(?P<id>\d+)/transcript/$',
        events.event_transcript,
        name='event_transcript'),
    url(r'^events/(?P<id>\d+)/upload/$',
        events.event_upload,
        name='event_upload'),
    url(r'^events/(?P<id>\d+)/vidly-submissions/$',
        events.event_vidly_submissions,
        name='event_vidly_submissions'),
    url(r'^events/(?P<id>\d+)/vidly-submissions/submission'
        r'/(?P<submission_id>\d+)/$',
        events.event_vidly_submission,
        name='event_vidly_submission'),
    url(r'^events/(?P<id>\d+)/comments/$',
        events.event_comments,
        name='event_comments'),
    url(r'^events/(?P<id>\d+)/comments/configuration/$',
        events.event_discussion,
        name='event_discussion'),
    url(r'^events/(?P<id>\d+)/stop-live/$', events.event_stop_live,
        name='stop_live_event'),
    url(r'^events/(?P<id>\d+)/survey/$', events.event_survey,
        name='event_survey'),
    url(r'^events/(?P<id>\d+)/tweets/$', events.event_tweets,
        name='event_tweets'),
    url(r'^events/(?P<id>\d+)/tweets/new/$', events.new_event_tweet,
        name='new_event_tweet'),
    url(r'^events/all/tweets/$', events.all_event_tweets,
        name='all_event_tweets'),
    url(r'^events/archive/(?P<id>\d+)/$', events.event_archive,
        name='event_archive'),
    url(r'^events/archive/(?P<id>\d+)/auto/$',
        events.event_archive_auto,
        name='event_archive_auto'),
    url(r'^events/duplicate/(?P<duplicate_id>\d+)/$', events.event_request,
        name='event_duplicate'),
    url(r'^events/vidlyurltoshortcode/(?P<id>\d+)/',
        events.vidly_url_to_shortcode,
        name='vidly_url_to_shortcode'),
    url(r'^events/hits/$', events.event_hit_stats, name='event_hit_stats'),
    url(r'^events/assignments/$',
        events.event_assignments,
        name='event_assignments'),
    url(r'^events/assignments.ics$',
        events.event_assignments_ical,
        name='event_assignments_ical'),
    url(r'^events/$', events.events, name='events'),
    url(r'^events/data/$', events.events_data, name='events_data'),
    url(r'^events/redirect_thumbnail/(?P<id>\d+)/$',
        events.redirect_event_thumbnail,
        name='redirect_event_thumbnail'),
    url(r'^surveys/$', surveys.surveys_, name='surveys'),
    url(r'^surveys/new/$', surveys.survey_new, name='survey_new'),
    url(r'^surveys/(?P<id>\d+)/$', surveys.survey_edit, name='survey_edit'),
    url(r'^surveys/(?P<id>\d+)/delete/$', surveys.survey_delete,
        name='survey_delete'),
    url(r'^surveys/(?P<id>\d+)/questions/$', surveys.survey_questions,
        name='survey_questions'),
    url(r'^surveys/(?P<id>\d+)/question/(?P<question_id>\d+)/$',
        surveys.survey_question_edit,
        name='survey_question_edit'),
    url(r'^surveys/(?P<id>\d+)/question/(?P<question_id>\d+)/delete/$',
        surveys.survey_question_delete,
        name='survey_question_delete'),
    url(r'^surveys/(?P<id>\d+)/question/new/$',
        surveys.survey_question_new,
        name='survey_question_new'),

    url(r'^comments/$', comments.all_comments, name='all_comments'),
    url(r'^comments/(?P<id>\d+)/$',
        comments.comment_edit,
        name='comment_edit'),
    url(r'^events-autocomplete/$', events.event_autocomplete,
        name='event_autocomplete'),
    url(r'^channels/new/$', channels.channel_new, name='channel_new'),
    url(r'^channels/(?P<id>\d+)/$', channels.channel_edit,
        name='channel_edit'),
    url(r'^channels/remove/(?P<id>\d+)/$', channels.channel_remove,
        name='channel_remove'),
    url(r'^channels/$', channels.channels, name='channels'),
    url(r'^templates/env-autofill/$', templates.template_env_autofill,
        name='template_env_autofill'),
    url(r'^templates/new/$', templates.template_new, name='template_new'),
    url(r'^templates/(?P<id>\d+)/$', templates.template_edit,
        name='template_edit'),
    url(r'^templates/remove/(?P<id>\d+)/$', templates.template_remove,
        name='template_remove'),
    url(r'^templates/$', templates.templates, name='templates'),
    url(r'^tags/$', tags.tags, name='tags'),
    url(r'^tags/data/$', tags.tags_data, name='tags_data'),
    url(r'^tags/(?P<id>\d+)/$', tags.tag_edit, name='tag_edit'),
    url(r'^tags/remove/(?P<id>\d+)/$', tags.tag_remove, name='tag_remove'),
    url(r'^tags/merge/(?P<id>\d+)/$', tags.tag_merge, name='tag_merge'),
    url(r'^locations/new/$', locations.location_new, name='location_new'),
    url(r'^locations/(?P<id>\d+)/$', locations.location_edit,
        name='location_edit'),
    url(r'^locations/remove/(?P<id>\d+)/$', locations.location_remove,
        name='location_remove'),
    url(r'^locations/tz/$', locations.location_timezone,
        name='location_timezone'),
    url(r'^locations/$', locations.locations, name='locations'),
    url(r'^regions/new/$', regions.region_new, name='region_new'),
    url(r'^regions/(?P<id>\d+)/$', regions.region_edit,
        name='region_edit'),
    url(r'^regions/remove/(?P<id>\d+)/$', regions.region_remove,
        name='region_remove'),
    url(r'^regions/$', regions.regions, name='regions'),
    url(r'^approvals/$', approvals.approvals, name='approvals'),
    url(r'^approvals/reconsider/$', approvals.approval_reconsider,
        name='approval_reconsider'),
    url(r'^approvals/(?P<id>\d+)/$', approvals.approval_review,
        name='approval_review'),
    url(r'^pages/$', flatpages.flatpages, name='flatpages'),
    url(r'^pages/new/$', flatpages.flatpage_new, name='flatpage_new'),
    url(r'^pages/(?P<id>\d+)/$', flatpages.flatpage_edit,
        name='flatpage_edit'),
    url(r'^pages/remove/(?P<id>\d+)/$', flatpages.flatpage_remove,
        name='flatpage_remove'),
    url(r'^suggestions/$', suggestions.suggestions, name='suggestions'),
    url(r'^suggestions/(?P<id>\d+)/$', suggestions.suggestion_review,
        name='suggestion_review'),
    url(r'^vidly/$', vidly_media.vidly_media,
        name='vidly_media'),
    url(r'^vidly/webhook/$', vidly_media.vidly_media_webhook,
        name='vidly_media_webhook'),
    url(r'^vidly/status/$', vidly_media.vidly_media_status,
        name='vidly_media_status'),
    url(r'^vidly/info/$', vidly_media.vidly_media_info,
        name='vidly_media_info'),
    url(r'^vidly/resubmit/$', vidly_media.vidly_media_resubmit,
        name='vidly_media_resubmit'),
    url(r'^urltransforms/$', url_transforms.url_transforms,
        name='url_transforms'),
    url(r'^urltransforms/new/$', url_transforms.url_match_new,
        name='url_match_new'),
    url(r'^urltransforms/run/$', url_transforms.url_match_run,
        name='url_match_run'),
    url(r'^urltransforms/(?P<id>\d+)/remove/$',
        url_transforms.url_match_remove,
        name='url_match_remove'),
    url(r'^urltransforms/(?P<id>\d+)/add/$', url_transforms.url_transform_add,
        name='url_transform_add'),
    url(r'^urltransforms/(?P<id>\d+)/(?P<transform_id>\d+)/remove/$',
        url_transforms.url_transform_remove,
        name='url_transform_remove'),
    url(r'^urltransforms/(?P<id>\d+)/(?P<transform_id>\d+)/edit/$',
        url_transforms.url_transform_edit,
        name='url_transform_edit'),
    url(r'^cron-pings/$',
        cronlogger.cron_pings,
        name='cron_pings'),
    url(r'^curated-groups-autocomplete/',
        groups.curated_groups_autocomplete,
        name='curated_groups_autocomplete'),
    url(r'^insufficient-permissions/',
        permissions.insufficient_permissions,
        name='insufficient_permissions'),
    url(r'^recruitmentmessages/$',
        recruitmentmessages.recruitmentmessages,
        name='recruitmentmessages'),
    url(r'^recruitmentmessages/new/$',
        recruitmentmessages.recruitmentmessage_new,
        name='recruitmentmessage_new'),
    url(r'^recruitmentmessages/(?P<id>\d+)/$',
        recruitmentmessages.recruitmentmessage_edit,
        name='recruitmentmessage_edit'),
    url(r'^recruitmentmessages/(?P<id>\d+)/delete/$',
        recruitmentmessages.recruitmentmessage_delete,
        name='recruitmentmessage_delete'),
    url(r'^loggedsearches/$',
        loggedsearches.loggedsearches,
        name='loggedsearches'),
    url(r'^loggedsearches/stats/$',
        loggedsearches.loggedsearches_stats,
        name='loggedsearches_stats'),
    url(r'^picturegallery/$',
        picturegallery.picturegallery,
        name='picturegallery'),
    url(r'^picturegallery/data/$',
        picturegallery.picturegallery_data,
        name='picturegallery_data'),
    url(r'^picturegallery/add/$',
        picturegallery.picture_add,
        name='picture_add'),
    url(r'^picturegallery/(?P<id>\d+)/$',
        picturegallery.picture_edit,
        name='picture_edit'),
    url(r'^picturegallery/(?P<id>\d+)/delete/$',
        picturegallery.picture_delete,
        name='picture_delete'),
    url(r'^picturegallery/(?P<id>\d+)/delete-all/$',
        picturegallery.picture_delete_all,
        name='picture_delete_all'),
    url(r'^picturegallery/(?P<id>\d+)/redirect_thumbnail/$',
        picturegallery.redirect_picture_thumbnail,
        name='redirect_picture_thumbnail'),
    url(r'^picturegallery/(?P<id>\d+)/event_associate/$',
        picturegallery.picture_event_associate,
        name='picture_event_associate'),
    url(r'^cronlogger/$',
        cronlogger.cronlogger_home,
        name='cronlogger'),
    url(r'^cronlogger/data/$',
        cronlogger.cronlogger_data,
        name='cronlogger_data'),
    url(r'^autocompeter/$',
        autocompeter.autocompeter_home,
        name='autocompeter'),
    url(r'^autocompeter/stats/$',
        autocompeter.autocompeter_stats,
        name='autocompeter_stats'),
    url(r'^autocompeter/test/$',
        autocompeter.autocompeter_test,
        name='autocompeter_test'),
)
