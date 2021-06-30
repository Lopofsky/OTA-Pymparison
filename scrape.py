#[END] ------------------------- CELL -------------------------------------------------------------------------------
from dask.distributed import Client
from seleniumwire import webdriver
from selectorlib import Extractor
from selenium.webdriver.common.keys import Keys
from requests import get
from collections import OrderedDict
from datetime import timedelta, datetime as dt
from time import sleep
from re import sub
import pandas as pd, numpy as np, platform, os, dask, copy, asyncio
from the_channels import get_channels, test_channel_filters

test_mode_channels, test_mode_periods = False, False

end_page_sleep_time, stay, filters2sheets, exception_keys = 0, 7, {}, ['']#['room_type', 'beds', 'number_of_ratings']
fieldnames = ["name", "location", "price", "channel", "period", "rating", ]#"url" #"room_type", "beds", "number_of_ratings", "rating_title", "url", "price_for", 
our = {
  "Stamos All Inclusive":"Booking.com",
  "Castellum Suites - All Inclusive":"ALL CHANNELS",
  "Bivalvia Studios":"Booking.com",
  "Kamari Beach Hotel - All inclusive":"Expedia.ie",
  "Aloe Hotel – Adults Only":"Expedia.ie",
  "Stamos Hotel - All Inclusive":"Expedia.ie",
  "Lido Star Beach":"Expedia.ie",
  "Bivalvia Beach Plus":"Expedia.ie",
  "Kamari Beach Hotel":"Booking.com",
  "Aloe Plus Hotel":"Booking.com",
  "Kouros Home Hotel":"ALL CHANNELS"
}
our_hotels = list([k for k,v in our.items()])
competitors = []#["AFANDOU BLU", "Lymberia Hotel"]
DRIVER_PATH = 'chromedriver.exe' if platform.system() == 'Windows' else os.getcwd()+'/chromedriver'
test_channel_filters()
chrome_options = webdriver.ChromeOptions()
'''
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument('--ignore-ssl-errors')
#chrome_options.add_argument('--headless')
'''
options = {'verify_ssl':True}

def get_periods(stay=7, test_mode=True):
    if test_mode:
        init_periods = ['2021-05-04']# , '2021-08-28', '2021-09-28', '2021-10-28'
        def generate_periods(period):
            start = dt.strptime(period, '%Y-%m-%d').date()
            end = start + timedelta(days=stay)
            return ({'day':str(start.day), 'month':str(start.month), 'year':str(start.year)}, {'day':str(end.day), 'month':str(end.month), 'year':str(end.year)})
        return [generate_periods(period) for period in init_periods]
    else:
        start, end, res, periods = '2021-05-01', '2021-11-01', [], ()
        start = dt.strptime(start, '%Y-%m-%d').date()
        e = dt.strptime(end, '%Y-%m-%d').date()
        end = start + timedelta(days=stay)
        while e > end:
            res.append(({'day':str('{:02d}'.format(start.day)), 'month':str('{:02d}'.format(start.month)), 'year':str('{:02d}'.format(start.year))}, {'day':str('{:02d}'.format(end.day)), 'month':str('{:02d}'.format(end.month)), 'year':str('{:02d}'.format(end.year))}))
            start = end
            end = start + timedelta(days=stay)
        return res

channels, periods = get_channels(test_mode=test_mode_channels), get_periods(stay=stay, test_mode=test_mode_periods)

def channel_url(channel, p, url):
    if channel == 'Booking.com':
        url = sub(r"checkin_year=\w+\&", "checkin_year={s_year}&".format(s_year=p[0]['year']), url)
        url = sub(r"checkin_month=\w+\&", "checkin_month={s_month}&".format(s_month=p[0]['month']), url)
        url = sub(r"checkin_monthday=\w+\&", "checkin_monthday={s_day}&".format(s_day=p[0]['day']), url)
        url = sub(r"checkout_year=\w+\&", "checkout_year={s_year}&".format(s_year=p[1]['year']), url)
        url = sub(r"checkout_month=\w+\&", "checkout_month={s_month}&".format(s_month=p[1]['month']), url)
        url = sub(r"checkout_monthday=\w+\&", "checkout_monthday={s_day}&".format(s_day=p[1]['day']), url)
    elif channel == 'Expedia.ie':
        chin = p[0]['year']+'-'+p[0]['month']+'-'+p[0]['day']
        chout = p[1]['year']+'-'+p[1]['month']+'-'+p[1]['day']
        url = sub(r"d1=(.*?&)", "d1={checkin}&".format(checkin=chin), url)
        url = sub(r"d2=(.*?&)", "d2={checkout}&".format(checkout=chout), url)
        url = sub(r"startDate=(.*?&)", "startDate={checkin}&".format(checkin=chin), url)
        url = sub(r"endDate=(.*?&)", "endDate={checkout}&".format(checkout=chout), url)
    return url

def scrape(channel, url, period, filter_name, driver):
    print("Downloading from Channel: {channel} > Period: {period} | filter_name: {filter_name} | Stay {stay}.".format(channel=channel, period=period, filter_name=filter_name, stay=str(stay)))
    def interceptor(request):
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': channels[channel]['referer'],
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
        }
        request.headers['User-Agent'] = headers['User-Agent']
    driver.request_interceptor = interceptor
    driver.get(url)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
    #driver.find_element_by_xpath("//img[contains(@id,'bannerTop1')]").click()
    sleep(end_page_sleep_time)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
    sleep(end_page_sleep_time)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
    sleep(end_page_sleep_time)
    print("Page Load Completed!")
    text = driver.page_source
    e = Extractor.from_yaml_file(channels[channel]['yaml_file'])
    res = e.extract(text, base_url=channels[channel]['referer'])
    return res

def ff(writer_i, filter_name_i):
    writer, filter_name = copy.deepcopy(writer_i), copy.deepcopy(filter_name_i)
    driver = webdriver.Chrome(options=chrome_options, seleniumwire_options=options, executable_path=DRIVER_PATH)
    try:
        for channel in channels:
            for p in periods:
                period = "{s_year}-{s_month}-{s_day}".format(s_year=p[0]['year'], s_month=p[0]['month'], s_day=p[0]['day'])
                url = channel_url(channel, p, channels[channel]['url'][filter_name])
                data, count = scrape(channel, url, period, filter_name, driver), 0
                if data and 'hotels' in data and data['hotels'] is not None:
                    for h in data['hotels']:
                        record, dont_write_flag = {'period': dt.strptime(period, '%Y-%m-%d').date(), 'channel':channel}, 0
                        for k,v in h.items():
                            if (k == 'name' and str(v).strip() in ('NoneType', 'None', '')): dont_write_flag = 1
                            elif dont_write_flag == 0 and k not in exception_keys:
                                if type(v) == list: v = v[count] if count+1 <= len(v) else None
                                if k not in ('price', 'period'): record[k] = v
                                elif k == 'price': record[k] = float(v.replace("€", '').replace(',', '').replace(' ', '').replace(' ', '')) if v is not None else "NULL"
                            else: pass
                        if dont_write_flag == 0: 
                            count += 1
                            for key in fieldnames:
                                v = record[key]
                                del record[key]
                                record[key] = v
                            for key in fieldnames:
                                writer[key].append(record[key])
    except Exception as e: raise e
    finally: driver.quit()
    return {filter_name:writer}

filters, agg_data = channels[list(channels.keys())[0]]['url'].keys(), []
if __name__ == '__main__':
    #client = Client()  # start local workers as processes # or
    client = Client(asynchronous=False, processes=True, threads_per_worker=len(filters), n_workers=4)  # start local workers as threads
    for filter_name in filters:
        print("************ filter_name =", filter_name)
        writer = {k:[] for k in fieldnames}
        #agg_data.append(dask.delayed(ff)(writer_i=writer, filter_name_i=filter_name))
        agg_data.append(client.submit(ff, writer_i=writer, filter_name_i=filter_name))
    print("************ LOOP END!!!!!!")
    #futures = dask.persist(*agg_data)
    print("------------starto!!!!")
    #[END] ------------------------- CELL -------------------------------------------------------------------------------

    #[START] ------------------------- CELL -------------------------------------------------------------------------------
    filters2sheets = {}
    for f in agg_data:#futures:
        #x = f.result()
        filters2sheets.update(f.result())
    print(filters2sheets)
    #[END] ------------------------- CELL -------------------------------------------------------------------------------

    #[START] ------------------------- CELL -------------------------------------------------------------------------------
    prod_date = str(dt.now().date())
    env_filename = 'Test Mode Scraping Report' if True in (test_mode_periods, test_mode_channels) else 'Full Price Scraping Report'
    xlsx_writer = pd.ExcelWriter(env_filename+' {prod_date}.xlsx'.format(prod_date=prod_date), engine = 'xlsxwriter')
    for a_filter, writer_data in filters2sheets.items():
        df = pd.DataFrame(writer_data)
        def custom_style(s):
            flag = -1
            if s[0].strip() in our_hotels: return ['text_wrap: True; background-color: green;' for x in s]
            elif s[0].strip() in competitors: return ['text_wrap: True; background-color: red' for x in s]
            else: return ['text_wrap: True;' for x in s]
        channel_names = list(channels.keys())
        #df.style.set_properties(**{'text-align': 'center', 'white-space': 'nowrap'})
        df.style.apply(custom_style, axis=1).set_properties(**{'text-align':'center', 'align':'center', 'white-space':'nowrap'}).to_excel(xlsx_writer, sheet_name=a_filter, index=False, header=True, startrow=5)
        workbook  = xlsx_writer.book
        worksheet = xlsx_writer.sheets[a_filter]
        worksheet.set_column('A:Z', 15)
        for idx, channel in enumerate(channel_names): 
            worksheet.write(0, idx, channel+" Filter URL", workbook.add_format({'bold': True, 'font_color': 'black'}))
            worksheet.write(1, idx, channels[channel]['url'][a_filter], workbook.add_format({'text_wrap': True}))
        worksheet.write(2, 0, "Channel Name", workbook.add_format({'bold': True, 'font_color': 'red'}))
        worksheet.write(3, 0, "Not Found (ours):", workbook.add_format({'bold': True, 'font_color': 'red'}))
        worksheet.write(4, 0, "^ Found Periods:", workbook.add_format({'bold': True, 'font_color': 'red'}))
        missing_our_hotels = list(set(our_hotels) - (set(our_hotels) - set(writer_data['name'])))
        comp = set(writer_data['name']) 
        diff = set(our_hotels)-(set(our_hotels) - set(writer_data['name']))
        for idx, hotel_name in enumerate(missing_our_hotels):
            worksheet.write(2, idx+1, our[hotel_name])
            worksheet.write(3, idx+1, hotel_name)
            weight = len(channels.keys()) if our[hotel_name] == 'ALL CHANNELS' else 1
            period_completeness = writer_data['name'].count(hotel_name)/(len(periods))/weight
            completeness_color = 'green' if period_completeness == 1 else 'red'
            found_periods_format = workbook.add_format({'bold': True, 'font_color': completeness_color})
            found_periods_format.set_num_format(10)
            worksheet.write(4, idx+1, period_completeness, found_periods_format)
    xlsx_writer.save()
    xlsx_writer.close()
    #[END] ------------------------- CELL -------------------------------------------------------------------------------