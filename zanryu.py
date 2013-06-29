# -*- coding: utf-8
# @author usa


import mechanize
import urlparse
import time


# login page url
login_page = 'https://vu8.sfc.keio.ac.jp/sfc-sfs/'


# make browser object
br = mechanize.Browser()
br.set_handle_robots(False)


#open login page
br.open(login_page)


# select form
br.select_form(nr=0)
br['u_login'] = username
br['u_pass'] = password
br.submit()


# get top page url
top_url = br.response().geturl()
par = urlparse.parse_qs(urlparse.urlparse(top_url).query)


# go to lab url
lab_url = 'https://vu9.sfc.keio.ac.jp/sfc-sfs/sfs_class/faculty/f_class_top.cgi?lang=ja&id=' + str(par['id']).strip('[]').strip('\'')+ '&yc=2013_27339&ks=00102&type=s'


# go to zanryu form
br.open(lab_url)
br.select_form(nr=0)
br.submit()


# fill out zanryu form
br.select_form(nr=0)
br['stay_phone'] = phone_num
br['stay_p_phone'] = parent_phone_num
br['stay_time'] = '11:00'
br['selectRoom'] = ['6']
#br['selectFloor'] = ['s1']
br['stay_room_other'] = '103'
br['stay_reason'] = 'Term Project'
br.submit()


print br.response().read()
