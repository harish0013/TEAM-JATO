import scrapy
import json
import re
from autoscout.items import VehicleDetailsItem

class VehicleDetailsSpider(scrapy.Spider):
    name = "copy"
    start_urls = [
        'https://www.autoscout24.de/lst?atype=C&cy=D&desc=0&hasleasing=true&ocs_listing=include&sort=standard&source=homepage_search-mask&ustate=N%2CU']

    leasing_durations = [12, 24, 36, 48, 60, 72]
    leasing_rates = [50, 100, 200, 300, 400, 500, 600, 700]

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def finance(self, string):
        pattern = r'\d*\.\d*'
        match = re.search(pattern, string)
        return float(match.group()) if match else 0

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
                item['VersionName'] = f"{item['Make']} {item['Model']} {item['Trim']} {item['Powertrain']}"
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
                item['Insurance'] = 'Not Available'
                item['InsuranceDescription'] = 'Not Available'
                item['ReimbursementMileageRetail'] = listing['lease']['mileage']
                yield item
