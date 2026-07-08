# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EasywpInternal(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=191)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'easywp_internal'


class WpActionschedulerActions(models.Model):
    action_id = models.BigAutoField(primary_key=True)
    hook = models.CharField(max_length=191)
    status = models.CharField(max_length=20)
    scheduled_date_gmt = models.DateTimeField(blank=True, null=True)
    scheduled_date_local = models.DateTimeField(blank=True, null=True)
    priority = models.PositiveIntegerField()
    args = models.CharField(max_length=191, blank=True, null=True)
    schedule = models.TextField(blank=True, null=True)
    group_id = models.PositiveBigIntegerField()
    attempts = models.IntegerField()
    last_attempt_gmt = models.DateTimeField(blank=True, null=True)
    last_attempt_local = models.DateTimeField(blank=True, null=True)
    claim_id = models.PositiveBigIntegerField()
    extended_args = models.CharField(max_length=8000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_actionscheduler_actions'


class WpActionschedulerClaims(models.Model):
    claim_id = models.BigAutoField(primary_key=True)
    date_created_gmt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_actionscheduler_claims'


class WpActionschedulerGroups(models.Model):
    group_id = models.BigAutoField(primary_key=True)
    slug = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_actionscheduler_groups'


class WpActionschedulerLogs(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    action_id = models.PositiveBigIntegerField()
    message = models.TextField()
    log_date_gmt = models.DateTimeField(blank=True, null=True)
    log_date_local = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_actionscheduler_logs'


class WpAddonlibraryAddons(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    alias = models.CharField(max_length=128, blank=True, null=True)
    addontype = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordering = models.IntegerField()
    templates = models.TextField(blank=True, null=True)
    config = models.TextField(blank=True, null=True)
    catid = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    test_slot1 = models.TextField(blank=True, null=True)
    test_slot2 = models.TextField(blank=True, null=True)
    test_slot3 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_addonlibrary_addons'


class WpAddonlibraryCategories(models.Model):
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    ordering = models.IntegerField()
    params = models.TextField()
    type = models.TextField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_addonlibrary_categories'


class WpBrizyLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.TextField()
    message = models.TextField()
    context = models.TextField()
    session_id = models.TextField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_brizy_logs'


class WpCommentmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    comment_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_commentmeta'


class WpComments(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.PositiveBigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_comments'


class WpDuplicatorBackups(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    hash = models.CharField(max_length=50)
    archive_name = models.CharField(max_length=350)
    status = models.IntegerField()
    progress = models.FloatField()
    flags = models.CharField(max_length=167)
    package = models.TextField()
    owner = models.CharField(max_length=60)
    version = models.CharField(max_length=30)
    created = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_duplicator_backups'


class WpDuplicatorEntities(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=100)
    value_1 = models.CharField(max_length=255)
    value_2 = models.CharField(max_length=255)
    value_3 = models.CharField(max_length=255)
    value_4 = models.CharField(max_length=255)
    value_5 = models.CharField(max_length=255)
    data = models.TextField()
    version = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_duplicator_entities'


class WpEEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_e_events'


class WpENotes(models.Model):
    id = models.BigAutoField(primary_key=True)
    route_url = models.TextField(blank=True, null=True, db_comment='Clean url where the note was created.')
    route_title = models.CharField(max_length=255, blank=True, null=True)
    route_post_id = models.PositiveBigIntegerField(blank=True, null=True, db_comment='The post id of the route that the note was created on.')
    post_id = models.PositiveBigIntegerField(blank=True, null=True)
    element_id = models.CharField(max_length=60, blank=True, null=True, db_comment='The Elementor element ID the note is attached to.')
    parent_id = models.PositiveBigIntegerField()
    author_id = models.PositiveBigIntegerField(blank=True, null=True)
    author_display_name = models.CharField(max_length=250, blank=True, null=True, db_comment='Save the author name when the author was deleted.')
    status = models.CharField(max_length=20)
    position = models.TextField(blank=True, null=True, db_comment='A JSON string that represents the position of the note inside the element in percentages. e.g. {x:10, y:15}')
    content = models.TextField(blank=True, null=True)
    is_resolved = models.IntegerField()
    is_public = models.IntegerField()
    last_activity_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_e_notes'


class WpENotesUsersRelations(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=60, db_comment='The relation type between user and note (e.g mention, watch, read).')
    note_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_e_notes_users_relations'


class WpESubmissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=60, blank=True, null=True)
    hash_id = models.CharField(unique=True, max_length=60)
    main_meta_id = models.PositiveBigIntegerField(db_comment='Id of main field. to represent the main meta field')
    post_id = models.PositiveBigIntegerField()
    referer = models.CharField(max_length=500)
    referer_title = models.CharField(max_length=300, blank=True, null=True)
    element_id = models.CharField(max_length=20)
    form_name = models.CharField(max_length=60)
    campaign_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    user_ip = models.CharField(max_length=46)
    user_agent = models.TextField()
    actions_count = models.IntegerField(blank=True, null=True)
    actions_succeeded_count = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20)
    is_read = models.IntegerField()
    meta = models.TextField(blank=True, null=True)
    created_at_gmt = models.DateTimeField()
    updated_at_gmt = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_e_submissions'


class WpESubmissionsActionsLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    submission_id = models.PositiveBigIntegerField()
    action_name = models.CharField(max_length=60)
    action_label = models.CharField(max_length=60, blank=True, null=True)
    status = models.CharField(max_length=20)
    log = models.TextField(blank=True, null=True)
    created_at_gmt = models.DateTimeField()
    updated_at_gmt = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_e_submissions_actions_log'


class WpESubmissionsValues(models.Model):
    id = models.BigAutoField(primary_key=True)
    submission_id = models.PositiveBigIntegerField()
    key = models.CharField(max_length=60, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_e_submissions_values'


class WpEbFormSettings(models.Model):
    block_id = models.CharField(unique=True, max_length=24)
    title = models.TextField()
    fields = models.TextField()
    form_options = models.TextField()
    settings = models.TextField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_eb_form_settings'


class WpLinks(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.PositiveBigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_links'


class WpOptions(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    option_name = models.CharField(unique=True, max_length=191)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wp_options'


class WpPostViews(models.Model):
    pk = models.CompositePrimaryKey('type', 'period', 'id')
    id = models.PositiveBigIntegerField()
    type = models.PositiveIntegerField()
    period = models.CharField(max_length=8)
    count = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_post_views'
        unique_together = (('id', 'type', 'period', 'count'),)


class WpPostmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    post_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_postmeta'


class WpPosts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.PositiveBigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.PositiveBigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_posts'


class WpRevsliderCss(models.Model):
    handle = models.TextField()
    settings = models.TextField(blank=True, null=True)
    hover = models.TextField(blank=True, null=True)
    advanced = models.TextField(blank=True, null=True)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_revslider_css'


class WpRevsliderCssBkp(models.Model):
    handle = models.TextField()
    settings = models.TextField(blank=True, null=True)
    hover = models.TextField(blank=True, null=True)
    advanced = models.TextField(blank=True, null=True)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_revslider_css_bkp'


class WpRevsliderLayerAnimations(models.Model):
    handle = models.TextField()
    params = models.TextField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_revslider_layer_animations'


class WpRevsliderLayerAnimationsBkp(models.Model):
    handle = models.TextField()
    params = models.TextField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_revslider_layer_animations_bkp'


class WpRevsliderNavigations(models.Model):
    name = models.CharField(max_length=191)
    handle = models.CharField(max_length=191)
    type = models.CharField(max_length=191)
    css = models.TextField()
    markup = models.TextField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_revslider_navigations'


class WpRevsliderNavigationsBkp(models.Model):
    name = models.CharField(max_length=191)
    handle = models.CharField(max_length=191)
    type = models.CharField(max_length=191)
    css = models.TextField()
    markup = models.TextField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_revslider_navigations_bkp'


class WpRevsliderSliders(models.Model):
    title = models.TextField()
    alias = models.TextField(blank=True, null=True)
    params = models.TextField()
    settings = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'wp_revslider_sliders'


class WpRevsliderSlidersBkp(models.Model):
    title = models.TextField()
    alias = models.TextField(blank=True, null=True)
    params = models.TextField()
    settings = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'wp_revslider_sliders_bkp'


class WpRevsliderSlides(models.Model):
    slider_id = models.IntegerField()
    slide_order = models.IntegerField()
    params = models.TextField()
    layers = models.TextField()
    settings = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_revslider_slides'


class WpRevsliderSlidesBkp(models.Model):
    slider_id = models.IntegerField()
    slide_order = models.IntegerField()
    params = models.TextField()
    layers = models.TextField()
    settings = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_revslider_slides_bkp'


class WpRevsliderStaticSlides(models.Model):
    slider_id = models.IntegerField()
    params = models.TextField()
    layers = models.TextField()
    settings = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_revslider_static_slides'


class WpRevsliderStaticSlidesBkp(models.Model):
    slider_id = models.IntegerField()
    params = models.TextField()
    layers = models.TextField()
    settings = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_revslider_static_slides_bkp'


class WpTermRelationships(models.Model):
    pk = models.CompositePrimaryKey('object_id', 'term_taxonomy_id')
    object_id = models.PositiveBigIntegerField()
    term_taxonomy_id = models.PositiveBigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_relationships'


class WpTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigAutoField(primary_key=True)
    term_id = models.PositiveBigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.PositiveBigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_taxonomy'
        unique_together = (('term_id', 'taxonomy'),)


class WpTermmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    term_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_termmeta'


class WpTerms(models.Model):
    term_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_terms'


class WpUsermeta(models.Model):
    umeta_id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_usermeta'


class WpUsers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=255)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=255)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'wp_users'


class WpWcAdminNoteActions(models.Model):
    action_id = models.BigAutoField(primary_key=True)
    note_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    query = models.TextField()
    status = models.CharField(max_length=255)
    actioned_text = models.CharField(max_length=255)
    nonce_action = models.CharField(max_length=255, blank=True, null=True)
    nonce_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wc_admin_note_actions'


class WpWcAdminNotes(models.Model):
    note_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    locale = models.CharField(max_length=20)
    title = models.TextField()
    content = models.TextField()
    content_data = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    date_reminder = models.DateTimeField(blank=True, null=True)
    is_snoozable = models.IntegerField()
    layout = models.CharField(max_length=20)
    image = models.CharField(max_length=200, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_read = models.IntegerField()
    icon = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'wp_wc_admin_notes'


class WpWcCategoryLookup(models.Model):
    pk = models.CompositePrimaryKey('category_tree_id', 'category_id')
    category_tree_id = models.PositiveBigIntegerField()
    category_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wc_category_lookup'


class WpWcCustomerLookup(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=60)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100, blank=True, null=True)
    date_last_active = models.DateTimeField(blank=True, null=True)
    date_registered = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=2)
    postcode = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'wp_wc_customer_lookup'


class WpWcDownloadLog(models.Model):
    download_log_id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField()
    permission_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wc_download_log'


class WpWcOrderAddresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.PositiveBigIntegerField()
    address_type = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    address_1 = models.TextField(blank=True, null=True)
    address_2 = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    postcode = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=320, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wc_order_addresses'
        unique_together = (('address_type', 'order_id'),)


class WpWcOrderCouponLookup(models.Model):
    pk = models.CompositePrimaryKey('order_id', 'coupon_id')
    order_id = models.PositiveBigIntegerField()
    coupon_id = models.BigIntegerField()
    date_created = models.DateTimeField()
    discount_amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wp_wc_order_coupon_lookup'


class WpWcOrderOperationalData(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.PositiveBigIntegerField(unique=True, blank=True, null=True)
    created_via = models.CharField(max_length=100, blank=True, null=True)
    woocommerce_version = models.CharField(max_length=20, blank=True, null=True)
    prices_include_tax = models.IntegerField(blank=True, null=True)
    coupon_usages_are_counted = models.IntegerField(blank=True, null=True)
    download_permission_granted = models.IntegerField(blank=True, null=True)
    cart_hash = models.CharField(max_length=100, blank=True, null=True)
    new_order_email_sent = models.IntegerField(blank=True, null=True)
    order_key = models.CharField(max_length=100, blank=True, null=True)
    order_stock_reduced = models.IntegerField(blank=True, null=True)
    date_paid_gmt = models.DateTimeField(blank=True, null=True)
    date_completed_gmt = models.DateTimeField(blank=True, null=True)
    shipping_tax_amount = models.DecimalField(max_digits=26, decimal_places=8, blank=True, null=True)
    shipping_total_amount = models.DecimalField(max_digits=26, decimal_places=8, blank=True, null=True)
    discount_tax_amount = models.DecimalField(max_digits=26, decimal_places=8, blank=True, null=True)
    discount_total_amount = models.DecimalField(max_digits=26, decimal_places=8, blank=True, null=True)
    recorded_sales = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wc_order_operational_data'


class WpWcOrderProductLookup(models.Model):
    order_item_id = models.PositiveBigIntegerField(primary_key=True)
    order_id = models.PositiveBigIntegerField()
    product_id = models.PositiveBigIntegerField()
    variation_id = models.PositiveBigIntegerField()
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    product_qty = models.IntegerField()
    product_net_revenue = models.FloatField()
    product_gross_revenue = models.FloatField()
    coupon_amount = models.FloatField()
    tax_amount = models.FloatField()
    shipping_amount = models.FloatField()
    shipping_tax_amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wp_wc_order_product_lookup'


class WpWcOrderStats(models.Model):
    order_id = models.PositiveBigIntegerField(primary_key=True)
    parent_id = models.PositiveBigIntegerField()
    date_created = models.DateTimeField()
    date_created_gmt = models.DateTimeField()
    date_paid = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    num_items_sold = models.IntegerField()
    total_sales = models.FloatField()
    tax_total = models.FloatField()
    shipping_total = models.FloatField()
    net_total = models.FloatField()
    returning_customer = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=200)
    customer_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wc_order_stats'


class WpWcOrderTaxLookup(models.Model):
    pk = models.CompositePrimaryKey('order_id', 'tax_rate_id')
    order_id = models.PositiveBigIntegerField()
    tax_rate_id = models.PositiveBigIntegerField()
    date_created = models.DateTimeField()
    shipping_tax = models.FloatField()
    order_tax = models.FloatField()
    total_tax = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wp_wc_order_tax_lookup'


class WpWcOrders(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=26, decimal_places=8, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=26, decimal_places=8, blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    billing_email = models.CharField(max_length=320, blank=True, null=True)
    date_created_gmt = models.DateTimeField(blank=True, null=True)
    date_updated_gmt = models.DateTimeField(blank=True, null=True)
    parent_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    payment_method_title = models.TextField(blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    customer_note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wc_orders'


class WpWcOrdersMeta(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wc_orders_meta'


class WpWcProductAttributesLookup(models.Model):
    pk = models.CompositePrimaryKey('product_or_parent_id', 'term_id', 'product_id', 'taxonomy')
    product_id = models.BigIntegerField()
    product_or_parent_id = models.BigIntegerField()
    taxonomy = models.CharField(max_length=32)
    term_id = models.BigIntegerField()
    is_variation_attribute = models.IntegerField()
    in_stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wc_product_attributes_lookup'


class WpWcProductDownloadDirectories(models.Model):
    url_id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=256)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wc_product_download_directories'


class WpWcProductMetaLookup(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    global_unique_id = models.CharField(max_length=100, blank=True, null=True)
    virtual = models.IntegerField(blank=True, null=True)
    downloadable = models.IntegerField(blank=True, null=True)
    min_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    onsale = models.IntegerField(blank=True, null=True)
    stock_quantity = models.FloatField(blank=True, null=True)
    stock_status = models.CharField(max_length=100, blank=True, null=True)
    rating_count = models.BigIntegerField(blank=True, null=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    total_sales = models.BigIntegerField(blank=True, null=True)
    tax_status = models.CharField(max_length=100, blank=True, null=True)
    tax_class = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wc_product_meta_lookup'


class WpWcRateLimits(models.Model):
    rate_limit_id = models.BigAutoField(primary_key=True)
    rate_limit_key = models.CharField(unique=True, max_length=200)
    rate_limit_expiry = models.PositiveBigIntegerField()
    rate_limit_remaining = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wc_rate_limits'


class WpWcReservedStock(models.Model):
    pk = models.CompositePrimaryKey('order_id', 'product_id')
    order_id = models.BigIntegerField()
    product_id = models.BigIntegerField()
    stock_quantity = models.FloatField()
    timestamp = models.DateTimeField()
    expires = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_wc_reserved_stock'


class WpWcTaxRateClasses(models.Model):
    tax_rate_class_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'wp_wc_tax_rate_classes'


class WpWcWebhooks(models.Model):
    webhook_id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=200)
    name = models.TextField()
    user_id = models.PositiveBigIntegerField()
    delivery_url = models.TextField()
    secret = models.TextField()
    topic = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    date_created_gmt = models.DateTimeField()
    date_modified = models.DateTimeField()
    date_modified_gmt = models.DateTimeField()
    api_version = models.SmallIntegerField()
    failure_count = models.SmallIntegerField()
    pending_delivery = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wc_webhooks'


class WpWoocommerceApiKeys(models.Model):
    key_id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    description = models.CharField(max_length=200, blank=True, null=True)
    permissions = models.CharField(max_length=10)
    consumer_key = models.CharField(max_length=64)
    consumer_secret = models.CharField(max_length=43)
    nonces = models.TextField(blank=True, null=True)
    truncated_key = models.CharField(max_length=7)
    last_access = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_api_keys'


class WpWoocommerceAttributeTaxonomies(models.Model):
    attribute_id = models.BigAutoField(primary_key=True)
    attribute_name = models.CharField(max_length=200)
    attribute_label = models.CharField(max_length=200, blank=True, null=True)
    attribute_type = models.CharField(max_length=20)
    attribute_orderby = models.CharField(max_length=20)
    attribute_public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_attribute_taxonomies'


class WpWoocommerceDownloadableProductPermissions(models.Model):
    permission_id = models.BigAutoField(primary_key=True)
    download_id = models.CharField(max_length=36)
    product_id = models.PositiveBigIntegerField()
    order_id = models.PositiveBigIntegerField()
    order_key = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    downloads_remaining = models.CharField(max_length=9, blank=True, null=True)
    access_granted = models.DateTimeField()
    access_expires = models.DateTimeField(blank=True, null=True)
    download_count = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_downloadable_product_permissions'


class WpWoocommerceLog(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField()
    level = models.SmallIntegerField()
    source = models.CharField(max_length=200)
    message = models.TextField()
    context = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_log'


class WpWoocommerceOrderItemmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    order_item_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_order_itemmeta'


class WpWoocommerceOrderItems(models.Model):
    order_item_id = models.BigAutoField(primary_key=True)
    order_item_name = models.TextField()
    order_item_type = models.CharField(max_length=200)
    order_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_order_items'


class WpWoocommercePaymentTokenmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    payment_token_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_payment_tokenmeta'


class WpWoocommercePaymentTokens(models.Model):
    token_id = models.BigAutoField(primary_key=True)
    gateway_id = models.CharField(max_length=200)
    token = models.TextField()
    user_id = models.PositiveBigIntegerField()
    type = models.CharField(max_length=200)
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_payment_tokens'


class WpWoocommerceSessions(models.Model):
    session_id = models.BigAutoField(primary_key=True)
    session_key = models.CharField(unique=True, max_length=32)
    session_value = models.TextField()
    session_expiry = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_sessions'


class WpWoocommerceShippingZoneLocations(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    zone_id = models.PositiveBigIntegerField()
    location_code = models.CharField(max_length=200)
    location_type = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_shipping_zone_locations'


class WpWoocommerceShippingZoneMethods(models.Model):
    zone_id = models.PositiveBigIntegerField()
    instance_id = models.BigAutoField(primary_key=True)
    method_id = models.CharField(max_length=200)
    method_order = models.PositiveBigIntegerField()
    is_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_shipping_zone_methods'


class WpWoocommerceShippingZones(models.Model):
    zone_id = models.BigAutoField(primary_key=True)
    zone_name = models.CharField(max_length=200)
    zone_order = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_shipping_zones'


class WpWoocommerceTaxRateLocations(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    location_code = models.CharField(max_length=200)
    tax_rate_id = models.PositiveBigIntegerField()
    location_type = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_tax_rate_locations'


class WpWoocommerceTaxRates(models.Model):
    tax_rate_id = models.BigAutoField(primary_key=True)
    tax_rate_country = models.CharField(max_length=2)
    tax_rate_state = models.CharField(max_length=200)
    tax_rate = models.CharField(max_length=8)
    tax_rate_name = models.CharField(max_length=200)
    tax_rate_priority = models.PositiveBigIntegerField()
    tax_rate_compound = models.IntegerField()
    tax_rate_shipping = models.IntegerField()
    tax_rate_order = models.PositiveBigIntegerField()
    tax_rate_class = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_tax_rates'


class WpYoastIndexable(models.Model):
    permalink = models.TextField(blank=True, null=True)
    permalink_hash = models.CharField(max_length=40, blank=True, null=True)
    object_id = models.BigIntegerField(blank=True, null=True)
    object_type = models.CharField(max_length=32)
    object_sub_type = models.CharField(max_length=32, blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    post_parent = models.BigIntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    breadcrumb_title = models.TextField(blank=True, null=True)
    post_status = models.CharField(max_length=20, blank=True, null=True)
    is_public = models.IntegerField(blank=True, null=True)
    is_protected = models.IntegerField(blank=True, null=True)
    has_public_posts = models.IntegerField(blank=True, null=True)
    number_of_pages = models.PositiveIntegerField(blank=True, null=True)
    canonical = models.TextField(blank=True, null=True)
    primary_focus_keyword = models.CharField(max_length=191, blank=True, null=True)
    primary_focus_keyword_score = models.IntegerField(blank=True, null=True)
    readability_score = models.IntegerField(blank=True, null=True)
    is_cornerstone = models.IntegerField(blank=True, null=True)
    is_robots_noindex = models.IntegerField(blank=True, null=True)
    is_robots_nofollow = models.IntegerField(blank=True, null=True)
    is_robots_noarchive = models.IntegerField(blank=True, null=True)
    is_robots_noimageindex = models.IntegerField(blank=True, null=True)
    is_robots_nosnippet = models.IntegerField(blank=True, null=True)
    twitter_title = models.TextField(blank=True, null=True)
    twitter_image = models.TextField(blank=True, null=True)
    twitter_description = models.TextField(blank=True, null=True)
    twitter_image_id = models.CharField(max_length=191, blank=True, null=True)
    twitter_image_source = models.TextField(blank=True, null=True)
    open_graph_title = models.TextField(blank=True, null=True)
    open_graph_description = models.TextField(blank=True, null=True)
    open_graph_image = models.TextField(blank=True, null=True)
    open_graph_image_id = models.CharField(max_length=191, blank=True, null=True)
    open_graph_image_source = models.TextField(blank=True, null=True)
    open_graph_image_meta = models.TextField(blank=True, null=True)
    link_count = models.IntegerField(blank=True, null=True)
    incoming_link_count = models.IntegerField(blank=True, null=True)
    prominent_words_version = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    blog_id = models.BigIntegerField()
    language = models.CharField(max_length=32, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    schema_page_type = models.CharField(max_length=64, blank=True, null=True)
    schema_article_type = models.CharField(max_length=64, blank=True, null=True)
    has_ancestors = models.IntegerField(blank=True, null=True)
    estimated_reading_time_minutes = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    object_last_modified = models.DateTimeField(blank=True, null=True)
    object_published_at = models.DateTimeField(blank=True, null=True)
    inclusive_language_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_yoast_indexable'


class WpYoastIndexableHierarchy(models.Model):
    pk = models.CompositePrimaryKey('indexable_id', 'ancestor_id')
    indexable_id = models.PositiveIntegerField()
    ancestor_id = models.PositiveIntegerField()
    depth = models.PositiveIntegerField(blank=True, null=True)
    blog_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_yoast_indexable_hierarchy'


class WpYoastMigrations(models.Model):
    version = models.CharField(unique=True, max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_yoast_migrations'


class WpYoastPrimaryTerm(models.Model):
    post_id = models.BigIntegerField(blank=True, null=True)
    term_id = models.BigIntegerField(blank=True, null=True)
    taxonomy = models.CharField(max_length=32)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    blog_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_yoast_primary_term'


class WpYoastSeoLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    post_id = models.PositiveBigIntegerField(blank=True, null=True)
    target_post_id = models.PositiveBigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=8, blank=True, null=True)
    indexable_id = models.PositiveIntegerField(blank=True, null=True)
    target_indexable_id = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    size = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=32, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_yoast_seo_links'
