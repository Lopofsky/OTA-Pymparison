from collections import defaultdict
import copy

def get_channels(test_mode=False):
    channels = defaultdict(dict)
    ###################################################################################################################
    channels['Expedia.ie']['referer'] = 'https://www.expedia.ie/'
    channels['Expedia.ie']['yaml_file'] = 'expedia.yml'
    # ---------------------------------------------------------------------------------------------------------
    channels['Expedia.ie']['url'] = {'faliraki_AI_Pool':"""https://www.expedia.ie/Hotel-Search?adults=2&amenities=POOL&d1=2021-8-1&d2=2021-8-8&destination=Faliraki%2C%20Rhodes%2C%20South%20Aegean%2C%20Greece&directFlights=false&endDate=2021-08-08&guestRating=&hotelName=&hotels-destination=Faliraki&latLong=36.34297469760486%2C28.204093470138634&localDateFormat=d%2FM%2Fyyyy&mealPlan=ALL_INCLUSIVE&neighborhood=6052014&partialStay=false&popularFilter=ALL_INCLUSIVE&popularFilter=POOL&regionId=6052014&semdtl=&sort=PRICE_LOW_TO_HIGH&startDate=2021-08-01&theme=&useRewards=false&userIntent="""}
    # ---------------------------------------------------------------------------------------------------------
    channels['Expedia.ie']['url']['Rodos All Inclusive'] = """https://www.expedia.ie/Hotel-Search?adults=2&d1=2021-06-20&d2=2021-06-27&destination=Rhodes%2C%20South%20Aegean%2C%20Greece&directFlights=false&endDate=2021-06-27&hotels-destination=Rhodes%2C%20South%20Aegean%2C%20Greece&latLong=36.443802%2C28.22735&localDateFormat=d%2FM%2Fyyyy&mealPlan=ALL_INCLUSIVE&partialStay=false&popularFilter=ALL_INCLUSIVE&regionId=11286&semdtl=&sort=PRICE_LOW_TO_HIGH&startDate=2021-06-20&theme=&useRewards=false&userIntent="""
    # ---------------------------------------------------------------------------------------------------------
    channels['Expedia.ie']['url']['faliraki_SC_St_Ap all stars'] = """https://www.expedia.ie/Hotel-Search?adults=2&bedroomFilter=0&d1=2021-07-01&d2=2021-07-08&destination=Faliraki%2C%20Rhodes%2C%20South%20Aegean%2C%20Greece&directFlights=false&endDate=2021-07-08&guestRating=&hotelName=&latLong=36.34297469760486%2C28.204093470138634&localDateFormat=d%2FM%2Fyyyy&lodging=HOTEL&lodging=APARTMENT&lodging=APART_HOTEL&neighborhood=6052014&partialStay=false&popularFilter=HOTEL&regionId=6052014&semdtl=&sort=PRICE_LOW_TO_HIGH&startDate=2021-07-01&theme=&useRewards=false&userIntent="""
    # ---------------------------------------------------------------------------------------------------------
    channels['Expedia.ie']['url']['faliraki_BB_Pool above 3 stars'] = """https://www.expedia.ie/Hotel-Search?adults=2&amenities=POOL&d1=2021-8-1&d2=2021-8-8&destination=Faliraki%2C%20Rhodes%2C%20South%20Aegean%2C%20Greece&directFlights=false&endDate=2021-08-08&guestRating=&hotelName=&hotels-destination=Faliraki&latLong=36.34297469760486%2C28.204093470138634&localDateFormat=d%2FM%2Fyyyy&mealPlan=FREE_BREAKFAST&neighborhood=6052014&partialStay=false&popularFilter=POOL&popularFilter=FREE_BREAKFAST&regionId=6052014&semdtl=&sort=PRICE_LOW_TO_HIGH&star=30&star=40&star=50&startDate=2021-08-01&theme=&useRewards=false&userIntent="""
    # ---------------------------------------------------------------------------------------------------------
    channels['Expedia.ie']['url']['city_AI_Pool above 3 stars'] = """https://www.expedia.ie/Hotel-Search?adults=2&amenities=POOL&d1=2021-8-1&d2=2021-8-8&destination=Rhodes%20Town%2C%20Rhodes%2C%20South%20Aegean%2C%20Greece&directFlights=false&endDate=2021-08-08&guestRating=&hotelName=&hotels-destination=Rhodes%20Town%2CFaliraki&latLong=36.433575379700606%2C28.224671199920156&localDateFormat=d%2FM%2Fyyyy&mealPlan=ALL_INCLUSIVE&neighborhood=6052011&partialStay=false&popularFilter=ALL_INCLUSIVE&popularFilter=POOL&regionId=6052011&semdtl=&sort=PRICE_LOW_TO_HIGH&star=30&star=40&star=50&startDate=2021-08-01&theme=&useRewards=false&userIntent="""
    ###################################################################################################################
    channels['Booking.com']['referer'] = 'https://www.booking.com/index.en-gb.html'
    channels['Booking.com']['yaml_file'] = 'booking.yml'
    # ---------------------------------------------------------------------------------------------------------
    channels['Booking.com']['url'] = {'faliraki_AI_Pool':"""https://www.booking.com/searchresults.en-gb.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFyIAQGYAQi4ARjIAQ_YAQHoAQH4AQuIAgGoAgS4At3H1oMGwAIB0gIkOTAzZTNhNWQtODE3Yi00OTE0LWFkYWQtNWFiMTJhYTUzOTA12AIG4AIB&sid=e426602c7a765d583da6088381b13993&tmpl=searchresults&checkin_month=6&checkin_monthday=1&checkin_year=2021&checkout_month=6&checkout_monthday=8&checkout_year=2021&city=900039186&class_interval=1&dest_id=900039186&dest_type=city&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&order=price&raw_dest_type=city&room1=A%2CA&sb_price_type=total&shw_aparth=1&slp_r_match=0&src=searchresults&srpvid=2f8328a9598a0074&ss=Faliraki&ssb=empty&ssne=Faliraki&ssne_untouched=Faliraki&top_ufis=1&sig=v17Up-8Jx6&nflt=mealplan%3D3%3Bmealplan%3D4%3Bhotelfacility%3D301%3B&rsf="""}
    # ---------------------------------------------------------------------------------------------------------
    channels['Booking.com']['url']['Rodos All Inclusive'] = """https://www.booking.com/searchresults.el.html?label=gen173nr-1FCAEoggI46AdIM1gEaFyIAQGYAQi4ARfIAQzYAQHoAQH4AQuIAgGoAgO4AtzCv4QGwAIB0gIkYzFjYmQ3MjYtYTQ1My00MDdkLWI2MGQtYTE4YmU1ZDY2Yjcw2AIG4AIB&sid=76f4a19e3482d3362497601b6d1a00f0&aid=304142&sb=1&sb_lp=1&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.el.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaFyIAQGYAQi4ARfIAQzYAQHoAQH4AQuIAgGoAgO4AtzCv4QGwAIB0gIkYzFjYmQ3MjYtYTQ1My00MDdkLWI2MGQtYTE4YmU1ZDY2Yjcw2AIG4AIB%3Bsid%3D76f4a19e3482d3362497601b6d1a00f0%3Bsb_price_type%3Dtotal%26%3B&ss=%CE%A1%CF%8C%CE%B4%CE%BF%CF%82%2C%20%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%B1&is_ski_area=&checkin_year=2021&checkin_month=6&checkin_monthday=10&checkout_year=2021&checkout_month=6&checkout_monthday=13&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&is_popular_nearby=1&from_sf=1&dest_id=1591&dest_type=region&search_pageview_id=2528522ee6790012&search_selected=true&order=price&nflt=mealplan%3D4%3B"""
    # ---------------------------------------------------------------------------------------------------------
    channels['Booking.com']['url']['faliraki_SC_St_Ap all stars'] = """https://www.booking.com/searchresults.en-gb.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFyIAQGYAQm4ARjIAQ_YAQHoAQH4AQuIAgGoAgS4Aqik64MGwAIB0gIkZjVlYmU3OTAtYzVlZi00Y2JmLTlhOWMtNTUyMzNhYzQ5Njc02AIG4AIB&sid=a841f80d2d2b609b0f9d54f2d53aa3d9&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2021&checkout_month=8&checkout_monthday=8&checkout_year=2021&class_interval=1&dest_id=900039186&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&order=price&percent_htype_apt=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&shw_aparth=1&slp_r_match=0&srpvid=6f23579ef65c00b9&ss=Faliraki&ss_all=0&ssb=empty&sshis=0&ssne=Faliraki&ssne_untouched=Faliraki&top_ufis=1&nflt=ht_beach%3D1%3Bmealplan%3D999%3Bht_id%3D204%3Bht_id%3D201%3Bht_id%3D206%3B&rsf="""
    # ---------------------------------------------------------------------------------------------------------
    channels['Booking.com']['url']['faliraki_BB_Pool above 3 stars'] = """https://www.booking.com/searchresults.en.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFyIAQGYAQi4ARjIAQ_YAQHoAQH4AQuIAgGoAgS4At3H1oMGwAIB0gIkOTAzZTNhNWQtODE3Yi00OTE0LWFkYWQtNWFiMTJhYTUzOTA12AIG4AIB&sid=a841f80d2d2b609b0f9d54f2d53aa3d9&tmpl=searchresults&ac_click_type=b&ac_position=0&checkin_month=6&checkin_monthday=1&checkin_year=2021&checkout_month=6&checkout_monthday=8&checkout_year=2021&class_interval=1&dest_id=900039186&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&order=price&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&srpvid=b9247180f37201b5&ss=Faliraki%2C%20Dodecanese%2C%20Greece&ss_all=0&ss_raw=faliraki&ssb=empty&sshis=0&ssne=%CE%A1%CF%8C%CE%B4%CE%BF%CF%82&ssne_untouched=%CE%A1%CF%8C%CE%B4%CE%BF%CF%82&top_ufis=1&nflt=hotelfacility%3D301%3Bmealplan%3D1%3Bclass%3D3%3Bclass%3D4%3Bclass%3D5%3B&rsf="""
    # ---------------------------------------------------------------------------------------------------------
    channels['Booking.com']['url']['city_AI_Pool above 3 stars'] = """https://www.booking.com/searchresults.en-gb.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFyIAQGYAQi4ARjIAQ_YAQHoAQH4AQuIAgGoAgS4At3H1oMGwAIB0gIkOTAzZTNhNWQtODE3Yi00OTE0LWFkYWQtNWFiMTJhYTUzOTA12AIG4AIB&sid=a841f80d2d2b609b0f9d54f2d53aa3d9&tmpl=searchresults&ac_click_type=b&ac_position=0&checkin_month=6&checkin_monthday=1&checkin_year=2021&checkout_month=6&checkout_monthday=8&checkout_year=2021&city=900039186&class_interval=1&dest_id=213835&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&iata=RHO&inac=0&index_postcard=0&label_click=undef&no_rooms=1&order=price&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=searchresults&srpvid=632d6fc67b740045&ss=Rhodes%20Town%2C%20Dodecanese%2C%20Greece&ss_all=0&ss_raw=rhodes%20town&ssb=empty&sshis=0&ssne=Faliraki&ssne_untouched=Faliraki&top_ufis=1&nflt=class%3D3%3Bclass%3D4%3Bclass%3D5%3Bmealplan%3D4%3Bmealplan%3D3%3Bhotelfacility%3D301%3B&rsf="""
    #'''
    ###################################################################################################################
    '''
    channels['Hotelopia']['referer'] = 'https://www.hotelopia.com/'
    channels['Hotelopia']['yaml_file'] = 'hotelbeds.yml'
    # ---------------------------------------------------------------------------------------------------------
    channels['Hotelopia']['url'] = {'faliraki':"""https://www.hotelopia.com/home.aspx"""}
    '''
    if test_mode:
        c = copy.deepcopy(channels)#{k:v for k,v in channels.items()}
        for channel, data in channels.items():
            for filter_name, url in data['url'].items():
                if filter_name not in ['Rodos All Inclusive']:#, 'faliraki_AI_Pool', 'faliraki_BB_Pool above 3 stars']:
                    del(c[channel]['url'][filter_name])
        return c
    return channels

def test_channel_filters():
    for cond in (True, False):
        data = get_channels(test_mode=cond) if cond == True else get_channels()
        channels = list(data.keys())
        filters = {ch:list(data[ch]['url'].keys()) for ch in channels}
        init, init_name = list(filters.values())[0], list(filters.keys())[0]
        for a_filter, filter_data in filters.items():
            if not all([x==y for x, y in zip(filter_data, init)]): raise Exception("NOT ALL FILTERS HAVE THE SAME NAME! driver channel >{init_name}<, Error Channel: {a_filter}".format(init_name=init_name, a_filter=a_filter))
        return True

if __name__ == '__main__':
    print("Testing mode running!!!!")
    test_channel_filters()