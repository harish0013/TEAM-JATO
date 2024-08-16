import scrapy
import json
import re
from autoscout.items import VehicleDetailsItem

class VehicleDetailsSpider(scrapy.Spider):
    name = "vehicle_details"
    start_urls = [
        'https://www.autoscout24.de/lst?atype=C&cy=D&desc=0&hasleasing=true&ocs_listing=include&sort=standard&source=homepage_search-mask&ustate=N%2CU']

    leasing_durations = [12, 24, 36, 48, 60, 72]
    leasing_rates = [50, 100, 200, 300, 400, 500, 600, 700]

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse,meta={'item_type':'car_data'})

    def finance(self, string):
        pattern = r'\d*\.\d*'
        match = re.search(pattern, string)
        if match:
            return float(match.group())
        else:
            return 0

    def calculate_emi(self, price, delivery_cost, duration, interest_rate):
        principal = price - delivery_cost
        if principal <= 0 or duration <= 0:
            return 0
        monthly_interest_rate = interest_rate / 100 / 12
        number_of_months = duration
        if monthly_interest_rate > 0:
            EMI = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_months) / (
                    (1 + monthly_interest_rate) ** number_of_months - 1)
        else:
            EMI = principal / number_of_months
        return EMI

    def parse(self, response):
        script_content = response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        if script_content:
            json_data = json.loads(script_content)
            page_props = json_data['props']['pageProps']

            if isinstance(page_props, list):
                page_props = page_props[0]

            listings = page_props.get('listings', [])
            for listing in listings:
                item = VehicleDetailsItem()
                item['Make'] = listing['vehicle'].get('make', 'Not Available')
                item['Model'] = listing['vehicle'].get('model', 'Not Available')
                item['Trim'] = listing['vehicle'].get('modelVersionInput', 'Not Available')
                item['Derivative'] = listing['vehicle'].get('modelVersionInput', 'Not Available')
                item['DerivativeTranslatedEnglish'] = listing['vehicle'].get('modelVersionInput', 'Not Available')
                item['Powertrain'] = listing['vehicleDetails'][3]['data'] if len(listing['vehicleDetails']) > 3 else 'Not Available'
                item['VersionName'] = f"{item['Make']}{item['Model']}{item['Trim']}{item['Derivative']}{item['Powertrain']}"
                item['VersionNameTranslatedEnglish'] = f"{item['Make']}{item['Model']}{item['Trim']}{item['Derivative']}{item['Powertrain']}"
                item['Currency'] = 'EURO'
                item['Price'] = listing['price'].get('priceFormatted', '0')
                item['DeliveryCost'] = listing['leasing']['bestOffer'].get('downPayment', '0')
                item['Country'] = listing['location'].get('countryCode', 'Not Available')
                item['Date'] = "07.08.2023"
                item['CustomerType'] = listing['leasing']['bestOffer'].get('targetGroup', 'Not Available')
                item['MonthlyPaymentType'] = listing['seller'].get('type', 'Not Available')
                item['ProductName'] = listing['vehicle'].get('offerType', 'Not Available')
                item['MonthlyPaymentProviderName'] = listing['seller'].get('companyName', 'Not Available')
                item['MonthlyPaymentProviderType'] = listing['seller'].get('type', 'Not Available')
                item['ContractDuration'] = listing['leasing']['bestOffer'].get('duration', 'Not Available')
                item['YearlyMileageKm'] = listing['leasing']['bestOffer'].get('includedMileage', '0')
                item['DepositRetail'] = listing['leasing']['bestOffer'].get('downPayment', '0')
                item['DataSource'] = "Market"
                item['OtherSource'] = "Market"
                item['VehiclePriceReference'] = 'MSRP'

                listing_url = listing.get('url', '')
                item['URL'] = f'https://www.autoscout24.de{listing_url}' if listing_url else 'Not Available'

                if isinstance(item['YearlyMileageKm'], str):
                    item['YearlyMileageKm'] = item['YearlyMileageKm'].replace(" km", "").replace(",", "")
                    try:
                        item['YearlyMileageKm'] = float(item['YearlyMileageKm'])
                    except ValueError:
                        item['YearlyMileageKm'] = 0

                item['YearlyMileageMiles'] = item['YearlyMileageKm'] * 0.621371

                if isinstance(item['ContractDuration'], str):
                    item['ContractDuration'] = item['ContractDuration'].replace(" Monate", "")
                    try:
                        item['ContractDuration'] = int(item['ContractDuration'])
                    except ValueError:
                        item['ContractDuration'] = 0

                item['TotalContractMileageKm'] = item['ContractDuration'] * item['YearlyMileageKm']
                item['TotalContractMileageMiles'] = item['TotalContractMileageKm'] * 0.621371

                price_value = self.finance(item['Price'])
                deliverycost_value = self.finance(item['DeliveryCost'])
                item['DepositPercentOfPrice'] = (deliverycost_value / price_value) * 100 if price_value > 0 else 0

                for duration in self.leasing_durations:
                    for rate in self.leasing_rates:
                        item['MonthlyPaymentEMI'] = self.calculate_emi(price_value, deliverycost_value, duration, rate)
                        yield item.copy()

            taxonomy = page_props.get('taxonomy', {})
            if isinstance(taxonomy, dict):
                body_types = taxonomy.get('bodyType', [])
                body_paintings = taxonomy.get('bodyPainting', [])
                for tax in body_types:
                    yield {'bodyType': tax['label']}
                for tax in body_paintings:
                    yield {'builtoption': tax['label']}
                for tax in body_paintings:
                    yield {'productdescription': tax['label']}

        for page_number in range(1, 21):
            next_page = f'https://www.autoscout24.de/lst?atype=C&cy=D&desc=0&hasleasing=true&ocs_listing=include&page={page_number}&search_id=glt8pad308&sort=standard&source=listpage_pagination&ustate=N%2CU'
            yield scrapy.Request(url=next_page, callback=self.parse)

        container = response.css('article.cldt-summary-full-item.listing-impressions-tracking.list-page-item.ListItem_article__qyYw7')
        for con in container:
            next_url = con.css('a.ListItem_title__ndA4s.ListItem_title_new_design__QIU2b.Link_link__Ajn7I::attr(href)').get()
            next_page = f"https://www.autoscout24.de{next_url}"
            yield scrapy.Request(url=next_page, callback=self.spec_parse)

    def spec_parse(self, response):
        for script in response.css('script'):
            script_content = script.xpath('text()').get()
            if script_content:
                try:
                    json_data = json.loads(script_content)
                    noofdoors = json_data['offers']['itemOffered']['numberOfDoors']
                    yield {'NumberOfDoors': noofdoors}
                except:
                    pass