from django.contrib import admin

from ebiznessapp.models import (Banner, OurService, Statistic, Category, Portfolio, FAQ, Section, Team, Blog, 
  SocialMedia, PricingTable, Testimonial, SiteSettings, Message, Site_smedia, BlogCategory, BlogTag, Comment
)


admin.site.register(Banner)
admin.site.register(OurService)
admin.site.register(Statistic)
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(FAQ)
admin.site.register(Section)
admin.site.register(Team)
admin.site.register(SocialMedia)
admin.site.register(PricingTable)
admin.site.register(Testimonial)
admin.site.register(SiteSettings)
admin.site.register(Message)
admin.site.register(Site_smedia)
admin.site.register(BlogCategory)
admin.site.register(BlogTag)
admin.site.register(Blog)
admin.site.register(Comment)