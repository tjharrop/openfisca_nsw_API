port = 4000
workers = 7
bind = '0.0.0.0:{}'.format(port)
country_package = 'openfisca_nsw_base'
extensions = ['openfisca_nsw_ess_nabers', 'openfisca-nsw-rules-kids-vouchers', 'openfisca_nsw_API']
